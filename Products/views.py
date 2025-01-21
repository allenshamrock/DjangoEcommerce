from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,VariationCategory,Variation,ReviewRating,ProductGallery
from django.conf import settings
from django.urls import reverse 
from .forms import ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

ALLOWED_HOSTS = settings.ALLOWED_HOSTS
# Create your views here.
def product_detail(request,category_slug,product_slug):
    try:
        product = get_object_or_404(Product,category__slug=category_slug, slug=product_slug)

    except Exception as e:
        raise e
    
    variation_categories = VariationCategory.objects.filter(variations__product = product).distinct()
    variations = Variation.objects.filter(product=product,is_active=True)

    # Fetch the product's gallery image
    gallery = ProductGallery.objects.filter(product=product)
    # Get the reviews
    reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    full_stars = range(int(product.average_review()))
    empty_stars = range(5 - int(product.average_review()))
    total_reviews = reviews.count()

    review_summary = {
        '5':reviews.filter(rating=5).count(),
        '4':reviews.filter(rating=4).count(),
        '3':reviews.filter(rating=3).count(),
        '2':reviews.filter(rating=2).count(),
        '1':reviews.filter(rating=1).count()

    }

# Calculating the percentage of each rating
    if total_reviews > 0:
        for key in review_summary:
            review_summary[key] = (review_summary[key] / total_reviews) * 100
    else:
        for key in review_summary:
            review_summary[key] = 0
    
    context = {
        'product':product,
        'gallery':gallery,
        'reviews':reviews,
        'full_stars':full_stars,
        'empty_stars':empty_stars,
        'variation_categories':variation_categories,
        'variations':variations,
        'review_summary':review_summary or {}
    }

    print(context)

    return render(request ,'products/product_detail.html',context)

#{Security guard for our website} Validates the url if it comes from our allowed hosts
def is_safe_url(url,allowed_hosts):
    from urllib.parse import urlparse
    url = url.strip()
    if url == '':
        return False
    url_obj = urlparse(url)
    return url_obj.netloc in allowed_hosts

    """
   This decorator allows only login user or registered users to leave a review
    """
@login_required  
def submit_review(request,product_id):
    # Get product instance to retrieve the category slug & product slug
    product = get_object_or_404(Product,id=product_id)
    category_slug = product.category.slug
    product_slug = product.slug

    # Get the referer URL or fallback to the product detail page
    referer_url = request.META.get('HTTP_REFERER',reverse('product_detail',args=[category_slug,product_slug]))

    # Validate the referer URL to ensure its safe
    if not is_safe_url(referer_url, allowed_hosts={request.get_host()}):
        referer_url = reverse('product_detail',args=[category_slug,product_slug]) 
    
    # If this is a Post request we need to process the from data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = ReviewForm(request.POST)
        # Check whether its valid
        if form.is_valid():
            review,created = ReviewRating.objects.update_or_create(
            user = request.user,
            product_id = product_id,
            defaults={
                'subject':form.cleaned_data['subject'],
                'rating':form.cleaned_data['rating'],
                'subject':form.cleaned_data['subject'],
                'ip':request.META.get('REMOTE_ADDR')
            }
            )

            if created:
                messages.success(request,'Thank you!, Your review has been submitted')
            
            else:
                messages.success(request, 'Thank you!,your review has been updated')
        else:
            messages.error(request, 'There was an error with your submission')
            return redirect(referer_url)
    
    return redirect(referer_url)

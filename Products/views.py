from django.shortcuts import render,get_object_or_404
from .models import Product,VariationCategory,Variation,ReviewRating,ProductGallery
# Create your views here.
def product_detail(request,category_slug,product_slug):
    try:
        product = get_object_or_404(Product,category__slug=category_slug, slug=product_slug)

    except Exception as e:
        raise e
    
    variation_category = VariationCategory.objects.filter(variations__product = product).distinct()
    variations = Variation.objects.filter(product=product,is_active=True)

    gallery = ProductGallery.objects.filter(product=product)
    reviews = ReviewRating.objects.filter(product=product.id, status=True)

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
        for key in reviews:
            review_summary[key] = (review_summary[key] / total_reviews) * 100
    
    context = {
        'product':product,
        'gallery':gallery,
        'reviews':reviews,
        'full_stars':full_stars,
        'empty_stars':empty_stars,
        'variation_category':variation_category,
        'variations':variations,
        'review_summary':review_summary
    }

    return render(request ,'products/product_detail.html',context)
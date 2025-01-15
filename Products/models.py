from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse


class Category(models.Model):
    """
    Represents a product category.
    """

    category_name = models.CharField(max_length=255)
    slug = models.SlugField(unique= True)


    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'
        indexes = [
            models.Index(fields = ['id','slug'])
        ]

    def __str__(self):
        return self.category_name

class Product(models.Model):
    """
    Represents a product with details like name, description, price, stock, and discount.
    """

    DISCOUNT_TYPE_CHOICES = [
        ('amount','Amount'),
        ('percent','Percentage')

    ]
    product_name = models.CharField(max_length=255)
    slug= models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_type =models.CharField(max_length=10, choices= DISCOUNT_TYPE_CHOICES, blank=True, null = True,help_text='Optional')
    discount = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null = True,help_text='Optional' )
    category = models.ForeignKey(Category,on_delete=models.CASCADE ,related_name='products')
    image = models.ImageField(upload_to='products/images')
    stock = models.PositiveIntegerField()
    available= models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural ='Products'
        ordering=('-created',)
        indexes = [
            models.Index(fields=['id','slug'])
        ]

    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

        """
        Calculates the average rating for the product.
        """

    def average_review(self):
        reviews = ReviewRating.objects.filter(product=self,status=True)
        average = reviews.aggregate(average=models.Avg('rating'))
        return float(average['average']) if average['average'] is not None else 0
    
class VariationCategory(models.Model):
    """
    Represents a category of product variations (e.g., size, color).
    """

    name = models.CharField(max_length=100,unique=True)
    display_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Variation Category'
        verbose_name_plural = 'Variation Categories'
        indexes = [
            models.Index(fields=['id','name'])
        ]

    def __str__(self):
        return self.display_name

class Variation(models.Model):
    """
    Represents a specific variation of a product (e.g., Red, Large).
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variations' )
    variation_category = models.ForeignKey(VariationCategory, on_delete=models.CASCADE,related_name='variations')
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Variation'
        verbose_name_plural = 'Variations'
        indexes = [
            models.Index(fields=['id','variation_category'])

        ]
    def __str__(self):
        return f'{self.variation_value} ({self.variation_category})'

class ProductGallery(models.Model):
    """
    Represents a gallery of images for a product.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='gallery')
    image = models.ImageField(upload_to='product/gallery')

    class Meta:
        verbose_name= 'Product Gallery'
        verbose_name_plural = 'Product Galleries'
    
    def __str__(self):
        return self.product.product_name
        
class ReviewRating(models.Model):
    """
    Represents a review and rating given by a user for a product.
    """

    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.FloatField()
    ip = models.CharField(max_length=255)
    status = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product Review'
        verbose_name_plural = 'Product Reviews'
        indexes = [
            models.Index(fields=['id','product','user'])

        ]
        ordering = ('-created_at',)


    def __str__(self):
        return f'{self.user.username} {self.product.product_name}'


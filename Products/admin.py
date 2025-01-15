from django.contrib import admin
from .models import Category,Product,VariationCategory,Variation,ProductGallery,ReviewRating

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(VariationCategory)
admin.site.register(Variation)
admin.site.register(ProductGallery)
admin.site.register(ReviewRating)

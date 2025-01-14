from django.contrib import admin
from .models import Category,Product,VariationCategory,Variations,ProductGallery

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(VariationCategory)
admin.site.register(Variations)
admin.site.register(ProductGallery)

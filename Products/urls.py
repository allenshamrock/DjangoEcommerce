from django.urls import path
from . import views

urlpatterns = [
   path('category/<slug:category_slug>/product/<slug:product_slug>/', views.product_detail, name='product_detail'),
   path('submit_review/<int:product_id>/', views.submit_review, name='submit_review')
]
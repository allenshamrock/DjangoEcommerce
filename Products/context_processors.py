from  .models import Category

# To display data in templates without having to write views
def categories(request):
    return {
        'categories':Category.objects.all()
    }
from django.shortcuts import render
from .models import Builder
from django.views.generic.edit import CreateView
# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')



def builders_index(request):
    builders = Builder.objects.all() # Retrieve all cats
    return render(request, 'builders/index.html', 
    { 
        'builders': builders 
    }
)

def builders_detail(request, builder_id):
  builder = Builder.objects.get(id=builder_id)
  return render(request, 'builders/detail.html', { 'builder': builder })

class BuilderCreate(CreateView):
  model = Builder
  fields =  ['name', 'region', 'house_type', 'rating','budget_category', 'appliances_included']
  # ['Name', 'Region', 'House_Type', 'Rating','Budget_Category', 'Appliances_Included']
 
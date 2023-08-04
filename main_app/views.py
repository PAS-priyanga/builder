from django.shortcuts import render
from .models import Builder
from .forms import PropertyDetailsForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
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
  propertydetails_form = PropertyDetailsForm()
  return render(request, 'builders/detail.html', { 'builder': builder ,"propertydetails_form" : propertydetails_form})

class BuilderCreate(CreateView):
  model = Builder
  fields =  ['name', 'region', 'house_type', 'rating','budget_category', 'appliances_included']
  # ['Name', 'Region', 'House_Type', 'Rating','Budget_Category', 'Appliances_Included']
 
class BuilderUpdate(UpdateView):
  model = Builder
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['appliances_included', 'rating']

class BuilderDelete(DeleteView):
  model = Builder
  success_url = '/builders'

def add_propertydetails(request, builder_id):
  form = PropertyDetailsForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_propertydetail = form.save(commit=False)
    new_propertydetail.builder_id = builder_id
    new_propertydetail.save()
  return redirect('detail', builder_id=builder_id)
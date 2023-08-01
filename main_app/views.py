from django.shortcuts import render
builders = [
    {"region": "Northern",
    "house_type": "Ranch",
    "rating": "5",
    "budget_category": "low",
    "name": "kb house",
    "appliances_included": False
    },
        {"region": "western",
    "house_type": "single family",
    "rating": "5",
    "budget_category": "high",
    "name": "cresleigh",
    "appliances_included": True
    },
        {"region": "southern",
    "house_type": "condo",
    "rating": "4",
    "budget_category": "high",
    "name": "premier",
    "appliances_included": False
    },
]
# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

def builders_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'builders/index.html', {
    'builders': builders
  })
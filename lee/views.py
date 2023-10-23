from django.http import HttpResponse
from django.template import loader

# Create your views here.


def bb(request):
  template = loader.get_template('bb.html')
  return HttpResponse(template.render())
  

def kate(request):
  template = loader.get_template('kate.html')
  return HttpResponse(template.render())


def pro(request):
  template = loader.get_template('pro.html')
  return HttpResponse(template.render())
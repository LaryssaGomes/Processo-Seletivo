from django.shortcuts import render

# Create your views here.
def home_page(request):
    title_btn = 'Currículo'
    return render(request, 'home.html', {'title_btn': title_btn})

def curriculo(request):
    return render(request, 'curriculo.html', )
from django.shortcuts import render

# Create your views here.


def about_us(request):
    """ A view to return the index page """

    return render(request, 'about_us/about_us.html')

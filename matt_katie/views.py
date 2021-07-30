from django.shortcuts import render


def error_404(request, exception):
    return render(request, 'matt_katie/404.html', status=404)


def error_500(request):
    return render(request, 'matt_katie/500.html')

from django.contrib import admin
from django.urls import path
from contact import views as contact_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact_views.contact_view, name='contact'),
]
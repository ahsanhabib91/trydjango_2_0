"""trydjango_2_0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, about_view, get_pdf
from products.views import product_create_view, product_detail_view, render_initial_data, dynamic_lookup_view
from testingapp.views import get_country

urlpatterns = [
    # path('', home_view, name='home'),
    path('', get_country),
    # path('about/', about_view),
    # path('contact/', contact_view),
    # path('create/', product_create_view),
    # path('initial/', render_initial_data),
    # path('product/', product_detail_view),
    # path('products/<int:id>/', dynamic_lookup_view, name='product'),
    # path('get_pdf/', get_pdf),
    # path('admin/', admin.site.urls),
]

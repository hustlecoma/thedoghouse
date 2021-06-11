"""SoloProjectApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# adding Order fixes throw error on line 28
from customer.views import Index, About, Order, OrderConfirmation, OrderPayConfirmation, Menu, MenuSearch

urlpatterns = [
   # url(r'^admin/', admin.site.urls),
   path('admin/', admin.site.urls),
   path('accounts/', include('allauth.urls')),
   path('restaurant/', include('restaurant.urls')),
   path('', Index.as_view(), name='index'),
   path('about/', About.as_view(), name='about'),
   path('menu/', Menu.as_view(), name='menu'),
   path('menu/search/', MenuSearch.as_view(), name='menu-search'),
   #35m 18s - this line throws error
   path('order/', Order.as_view(), name='order'),
   path('order-confirmation/<int:pk>', OrderConfirmation.as_view(), name='order-confirmation'),
   path('payment-confirmation/', OrderPayConfirmation.as_view(), name='payment-confirmation'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
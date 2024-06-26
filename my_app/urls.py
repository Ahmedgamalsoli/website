"""
URL configuration for my_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from item.views import Item
from cart.views import add_to_cart,cart , checkout

urlpatterns = [
    path('', include('core.urls')),
    path('cart/', include('cart.urls')),
    path('items/', include('item.urls')), 
    path('order/', include('order.urls')),
    path('inbox/', include('conversation.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL , document_root =settings.MEDIA_ROOT)

admin.site.site_header = "NA Store Admin"
admin.site.site_title = "NA Store"
admin.site.index_title = "Welcome to NA Store administrator"
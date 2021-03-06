from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),     # social accounts > migrate    
    path('cart/', include('cart.urls')),
    path('coupon/', include('coupon.urls')),
    path('order/', include('order.urls')),
    path('', include('shop.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
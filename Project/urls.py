# my_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView  # new
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import HomeView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('accounts.urls')),  # new
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('blog/', include('blogs.urls')),
                  path('forums/', include('forums.urls')),
                  path('', HomeView.as_view(), name='home'),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('', include('products.urls')),
                  path('cart', include('cart.urls')),
                  path('orders/', include('orders.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

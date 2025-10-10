from django.contrib import admin
from django.urls import path
from . import views  
from django.contrib.auth import views as auth_views


admin.site.site_header = ' shailu header'
admin.site.site_title = ' shailu title'
admin.site.index_title = ' shailu index'

urlpatterns = [
    path('', views.index , name = 'home'),
    path('about', views.about , name = 'about'),
    path('contact', views.contact , name = 'contact'),
    path('details/<int:id>', views.details , name = 'details'),
    path('upload_product',views.upload_product,name='upload_product'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),



]

from django.conf import settings
from django.conf.urls.static import static

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
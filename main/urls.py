from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from main_page import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('aboutme/', views.about_me, name='information_about_me'),
    path('mypet/', views.about_my_pets, name='my_pet'),
    path('system_time/', views.system_time, name='time'),
    path('', include('main_page.urls'))

]
urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                     document_root=settings.STATIC_ROOT)
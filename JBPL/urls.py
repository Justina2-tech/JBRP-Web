from django.contrib import admin
from django.urls import path, include
from fullstack.views import HomeView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('user/', include('fullstack.urls.user_urls')),
]

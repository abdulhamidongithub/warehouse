from django.contrib import admin
from django.urls import path, include
from app1.views import HomeView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bolim/', include('app1.urls')),
    path('stats/', include('statistika.urls')),
    path('', HomeView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]


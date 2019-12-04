from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(template_name='registration/login.html'), name='logout'),
    path('', include('blog.urls')),
]

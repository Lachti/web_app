from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='library/login.html')),
    url(r'^library/', include('libraryapp.urls')),
    url(r'^admin/', admin.site.urls),
]

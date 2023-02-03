from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/', include([
        path('account/', include('accounts.urls')),
        path('forum/', include('web_forum.urls')),
        ])),
]

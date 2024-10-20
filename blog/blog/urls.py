from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blog_app.urls', namespace='blog_app')),
    path('admin/', admin.site.urls),
    path('blog_app/', include('blog_app.urls', namespace='blog_app'))
]
from django.urls import path
from . import views

urlpatterns = [
    # post views
    path('admin/', admin.site.urls),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='psot_detail')
]

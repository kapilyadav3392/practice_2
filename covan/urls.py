
from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name="index"),
    path('bg/',views.bg, name="bg")
]

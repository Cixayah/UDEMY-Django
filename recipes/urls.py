from django.urls import path
from recipes.views import home

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", home),
]

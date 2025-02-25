from django.urls import path
from recipes.views import home, contact, about

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home),
    path('contact/', contact),
    path('about/', about),
]

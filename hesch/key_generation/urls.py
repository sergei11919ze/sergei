from django.urls import path
from .views import hasch_gen


urlpatterns = [
    path('api/v1/<int:id>/', hasch_gen),
]
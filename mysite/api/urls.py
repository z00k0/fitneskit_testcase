from .views import get_employees_view
from django.urls import path

urlpatterns = [
    path("get_employees/", get_employees_view),
]

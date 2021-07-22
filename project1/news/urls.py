from django.urls import path
from .views import index,testing_page



urlpatterns = [
    path('', index),
    path('test/',  testing_page)

]
from django.urls import path
from .  import views



urlpatterns = [
    path ('',views.create),
    path ('read/',views.read),
    path ('update/<int:pk>',views.update),
    path ('delete/<int:id>',views.delete),
]

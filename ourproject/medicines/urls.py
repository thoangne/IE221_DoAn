from django.urls import path
from .views import (
  show_medicine,
  show_detail,
  add_medicine,
  update_medicine,
  delete_medicine,
)
app_name = 'medicines'

urlpatterns = [
  path('', show_medicine, name='show-medicine'),
  path('add/', add_medicine, name='add-medicine'),
  path('<int:id>/', show_detail, name='show-detail'),
  path('<int:id>/update/', update_medicine, name='update-medicine'),
  path('<int:id>/delete/', delete_medicine, name='delete-medicine'),
]
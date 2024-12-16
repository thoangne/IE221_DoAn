from django.contrib import admin
from django.http import HttpRequest
from .models import *
# Register your models here.
# class MedicineAdmin(admin.ModelAdmin):
#   list_display = ('medicine_id','name','catelogy_id','dosage_form','strength','quantity_in_stock','price','expiry_date')
#   list_filter = ('expiry_date')
#   search_fields = ('medicine_id','name')
#   ordering = ('price')
#   def has_add_permission(self, request):
#       return request.user.is_superuser  # Chỉ cho phép admin thêm

#   def has_change_permission(self, request, obj=None):
#     return request.user.is_superuser  # Chỉ cho phép admin sửa

#   def has_delete_permission(self, request, obj=None):
#     return request.user.is_superuser  # Chỉ cho phép admin xóa
# admin.site.register(Medicine,MedicineAdmin)

admin.site.register(Medicine)
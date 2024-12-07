from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
  class Meta:
    model = Medicine
    fields = ['medicine_id','name','catelogy_id','dosage_form','strength','quantity_in_stock','price','expiry_date']
    widgets = {
      'medicine_id': forms.TextInput(attrs={"placeholder": "Nhập mã thuốc"}),
      'name': forms.TextInput(attrs={"placeholder": "Nhập tên thuốc"}),
      'catelogy_id': forms.TextInput(attrs={"placeholder": "Nhập mã nhà cung cấp"}),
      'dosage_form': forms.TextInput(attrs={"placeholder": "Nhập dạng thuốc"}),
      'strength': forms.TextInput(attrs={"placeholder": "Nhập khối lượng thuốc"}),
      'quantity_in_stock': forms.NumberInput(attrs={"placeholder": "Nhập lượng hàng tồn"}),
      'price': forms.NumberInput(attrs={"placeholder": "Nhập giá"}),
      'expiry_date': forms.DateInput(attrs={"placeholder": "Nhập ngày hết hạn"}),
    }
    labels = {
      'medicine_id': 'Mã thuốc',
      'name': 'Tên thuốc',
      'catelogy_id': 'Mã NCC',
      'dosage_form': 'Dạng thuốc',
      'strength': 'Trọng lượng',
      'quantity_in_stock': 'Hàng tồn',
      'price': 'Giá',
      'expiry_date': 'Ngày hết hạn',
    }
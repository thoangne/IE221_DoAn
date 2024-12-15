from django import forms
from .models import *

class MedicineForm(forms.ModelForm):
  class Meta:
    model = Medicine
    fields = ['medicine_id','name','category_id','dosage_form','strength','quantity_in_stock','price','expiry_date', 'supplier_id']
    input_formats = {
      'expiry_date': ['%d/%m/%Y']
    }
    widgets = {
      'medicine_id': forms.TextInput(attrs={"placeholder": "Nhập mã thuốc"}),
      'name': forms.TextInput(attrs={"placeholder": "Nhập tên thuốc"}),
      'category_id': forms.TextInput(attrs={"placeholder": "Nhập mã chức năng thuốc"}),
      'dosage_form': forms.TextInput(attrs={"placeholder": "Nhập dạng thuốc"}),
      'strength': forms.TextInput(attrs={"placeholder": "Nhập khối lượng thuốc"}),
      'quantity_in_stock': forms.NumberInput(attrs={"placeholder": "Nhập lượng hàng tồn"}),
      'price': forms.NumberInput(attrs={"placeholder": "Nhập giá"}),
      'expiry_date': forms.DateInput(format='%d/%m/%Y',attrs={'type': 'date','placeholder': 'Nhập ngày hết hạn (DD/MM/YYYY)'}),
      'supplier_id': forms.TextInput(attrs={"placeholder": "Nhập mã nhà cung cấp"}),
    }
    labels = {
      'medicine_id': 'Mã thuốc',
      'name': 'Tên thuốc',
      'category_id': 'Mã chức năng thuốc',
      'dosage_form': 'Dạng thuốc',
      'strength': 'Trọng lượng',
      'quantity_in_stock': 'Hàng tồn',
      'price': 'Giá',
      'expiry_date': 'Ngày hết hạn',
      'supplier_id': 'Mã nhà cung cấp'
    }

class CategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = ['category_id','name','description']
    # input_formats = 
    widgets = {
      'category_id':forms.TextInput(attrs={"placeholder": "Nhập mã phân loại thuốc"}),
      'name': forms.TextInput(attrs={"placeholder": "Nhập tên phân loại thuốc"}),
      'deccription': forms.Textarea( attrs={"placeholder": "Nhập mô tả"})
    }
    labels = {
      'categoty_id': 'Mã phân loại thuốc',
      'name': 'Tên phân loại thuốc',
      'description': 'Mô tả'
    }

class SupplierForm(forms.ModelForm):
  class Meta:
    model = Supplier
    fields = ['supplier_id','name','contact_info','address']
    # input_formats = 
    widgets = {
      'supplier_id':forms.TextInput(attrs={"placeholder": "Nhập mã nhà cung cấp thuốc"}),
      'name': forms.TextInput(attrs={"placeholder": "Nhập tên nhà cung cấp thuốc"}),
      'contact_info': forms.TextInput( attrs={"placeholder": "Nhập số điện thoại liên hệ"}),
      'address': forms.TextInput(attrs={"placeholder": "Nhập địa chỉ nhà cung cấp"})
    }
    labels = {
      'supplier_id': 'Mã nhà cung cấp thuốc',
      'name': 'Tên nhà cung cấp thuốc',
      'contact_info': 'Số điện thoại liên hệ',
      'address':'Địa chỉ nhà cung cấp'
    }

class CustomerForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ['customer_id', 'name', 'contact_number','address','date_of_birth']
    input_formats = {
      'date_of_birth': ['%d/%m/%Y']
    }
    widgets = {
      'customer_id':forms.TextInput(attrs={"placeholder": "Nhập mã khách hàng"}),
      'name': forms.TextInput(attrs={"placeholder": "Nhập tên khách hàng"}),
      'contact_number': forms.TextInput( attrs={"placeholder": "Nhập số điện thoại liên hệ"}),
      'date_of_birth': forms.DateInput(format='%d/%m/%Y',attrs={'type': 'date','placeholder': 'Nhập ngày sinh khách hàng (DD/MM/YYYY)'})
    }
    labels = {
      'customer_id': 'Mã khách hàng',
      'name': 'Tên khách hàng','contact_number': 'Số điện thoại liên hệ',
      'address': 'Địa chỉ khách hàng',
      'date_of_birth': 'Ngày sinh khách hàng'
    }
#
class EmployeeForm(forms.ModelForm):
  class Meta:
    model = Employee
    fields = ['employee_id', 'name', 'position', 'contact_number', 'hire_date', 'salary', 'date_of_birth']
    input_formats = {
      'hire_date':  ['%d/%m/%Y'],
      'date_of_birth': ['%d/%m/%Y']
    } 
    widgets = {
      'employee_id':forms.TextInput(attrs={"placeholder": "Nhập mã nhân viên"}),
      'name': forms.TextInput(attrs={"placeholder": "Nhập tên nhân viên"}),
      'position': forms.TextInput( attrs={"placeholder": "Nhập vị trí"}),
      'contact_number': forms.TextInput(attrs={"placeholder": "Nhập số điện thoại liên hệ"}),
      'hire_date': forms.DateInput(format='%d/%m/%Y',attrs={'type': 'date','placeholder': 'Nhập ngày vào làm (DD/MM/YYYY)'}),
      'salary': forms.NumberInput(attrs={"placeholder": "Nhập lương theo tháng"}),
      'date_of_birth': forms.DateInput(format='%d/%m/%Y',attrs={'type': 'date','placeholder': 'Nhập ngày sinh nhân viên (DD/MM/YYYY)'})
    }
    labels = {
      'employee_id': 'Mã nhân viên',
      'name': 'Tên nhân viên','position': 'Mô tả',
      'contact_number': 'Số điện thoại liên hệ',
      'hire_date': 'Ngày vào làm',
      'salary': 'Lương theo tháng',
      'date_of_birth': 'Ngày sinh nhân viên'
    }

class SaleForm(forms.ModelForm):
  # total = forms.IntegerField(disabled=True)
  class Meta:
    model = Sale
    fields = ['sale_id', 'medicine_id', 'customer_id','quantity_sold', 'sale_date','total']
    input_formats = {
      'sale_date': ['%d/%m/%Y']
    } 
    widgets = {
      'sale_id':forms.TextInput(attrs={"placeholder": "Nhập mã hóa đơn"}),
      'medicine_id': forms.TextInput(attrs={"placeholder": "Nhập mã thuốc"}),
      'customer_id': forms.TextInput( attrs={"placeholder": "Nhập mã khách hàng"}),
      'quantity_sold': forms.NumberInput(attrs={"placeholder": "Nhập số lượng mua"}),
      'sale_date': forms.DateInput(format='%d/%m/%Y',attrs={'type': 'date','placeholder': 'Nhập ngày mua thuốc (DD/MM/YYYY)'}),
      'total': forms.NumberInput(attrs={'readonly': 'readonly'}),
    }
    labels = {
      'sale_id': 'Mã hóa đơn',
      'medicine_id': 'Mã thuốc',
      'customer_id': 'Mã khách hàng',
      'quantity_sold': 'Số lượng mua',
      'sale_date': 'Ngày mua thuốc',
      'total': 'Tổng tiền'
    }
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['total'].required = False
  # def clean(self):
  #   cleaned_data = super().clean()
  #   medicine = cleaned_data.get('medicine_id')  # Lấy đối tượng Medicine
  #   quantity = cleaned_data.get('quantity_sold')  # Lấy số lượng

  #   if medicine and quantity:
  #       # Tính toán total_price
  #       cleaned_data['total'] = medicine.price * quantity

  #   return cleaned_data
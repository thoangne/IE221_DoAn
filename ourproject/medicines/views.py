from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.forms import DateField
from django.urls import reverse

# Create your views here.
class LoginView:
# Create your views here.
  def register_view(response):
    if response.method =="POST":
      form =  RegisterForm(response.POST)
      if form.is_valid():
        form.save()
        return redirect("/login")

    else:
      form =  RegisterForm()
    print(form)
    return render(response, "register.html", {"form":form})

  def login_view(request):
    if request.method == 'POST':
      form = LoginForm(request.POST)
      if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
          login(request, user)
          return redirect('home')
    else:
      form = LoginForm()
    return render(request, 'login.html', {'form': form})

  def logout_view(response):
    logout(response)
    return redirect("login")
class MedicineView:
  def show_medicine(request):
    return render(request, 'show_medicine.html',{'object_list':Medicine.objects.all()})
  def show_detail(request,key_id):
    row = get_object_or_404(Medicine, pk=key_id)
    form = MedicineForm(instance=row)
    for field in form:
      field.is_date = isinstance(field.field, DateField)
    url_update = reverse("medicines:update-medicine", kwargs={'key_id': key_id})
    url_delete = reverse("medicines:delete-medicine", kwargs={'key_id': key_id})
    return render(request,'show_detail.html',{'form':form,'url_update': url_update,'url_delete':url_delete})
  def add_medicine(request):
    if request.method == 'POST':
      form = MedicineForm(request.POST)
      if form.is_valid():
        form.save()
        form = MedicineForm()
    else:
        form = MedicineForm()
    return render(request, 'add_medicine.html', {'form': form})
  def update_medicine(request, key_id):
    if request.method == 'POST':
      row = get_object_or_404(Medicine, pk=key_id)
      form = MedicineForm(request.POST,instance=row)
      if form.is_valid():
        form.save()
      return redirect('../')
    else:
      row = get_object_or_404(Medicine, pk=key_id)
      form = MedicineForm(instance=row)
    return render(request,'update_medicine.html',{'form':form})
  def delete_medicine(request,key_id):
    row = get_object_or_404(Medicine, pk=key_id)
    if request.method == 'POST':
      row.delete()
      return redirect('../../')
      # return redirect('/medicine/')
    return render(request, 'delete_medicine.html',{'object':row})
class CategoryView:
  def show_medicine(request):
    return render(request, 'show_medicine.html',{'object_list':Category.objects.all()})
  def show_detail(request,key_id):
    row = get_object_or_404(Category, pk=key_id)
    form = CategoryForm(instance=row)
    for field in form:
      field.is_date = isinstance(field.field, DateField)
    url_update = reverse("medicines:update-category", kwargs={'key_id': key_id})
    url_delete = reverse("medicines:delete-category", kwargs={'key_id': key_id})
    return render(request,'show_detail.html',{'form':form,'url_update': url_update,'url_delete':url_delete})
  def add_medicine(request):
    if request.method == 'POST':
      form = CategoryForm(request.POST)
      if form.is_valid():
        form.save()
        form = CategoryForm()
    else:
        form = CategoryForm()
    return render(request, 'add_medicine.html', {'form': form})
  def update_medicine(request, key_id):
    if request.method == 'POST':
      row = get_object_or_404(Category, pk=key_id)
      form = CategoryForm(request.POST,instance=row)
      if form.is_valid():
        form.save()
      return redirect('../')
    else:
      row = get_object_or_404(Category, pk=key_id)
      form = CategoryForm(instance=row)
    return render(request,'update_medicine.html',{'form':form})
  def delete_medicine(request,key_id):
    row = get_object_or_404(Category, pk=key_id)
    if request.method == 'POST':
      row.delete()
      return redirect('../../')
      # return redirect('/medicine/')
    return render(request, 'delete_medicine.html',{'object':row})
class SupplierView:
  def show_medicine(request):
    return render(request, 'show_medicine.html',{'object_list':Supplier.objects.all()})
  def show_detail(request,key_id):
    row = get_object_or_404(Supplier, pk=key_id)
    form = SupplierForm(instance=row)
    for field in form:
      field.is_date = isinstance(field.field, DateField)
    url_update = reverse("medicines:update-supplier", kwargs={'key_id': key_id})
    url_delete = reverse("medicines:delete-supplier", kwargs={'key_id': key_id})
    return render(request,'show_detail.html',{'form':form,'url_update': url_update,'url_delete':url_delete})
  def add_medicine(request):
    if request.method == 'POST':
      form = SupplierForm(request.POST)
      if form.is_valid():
        form.save()
        form = SupplierForm()
    else:
        form = SupplierForm()
    return render(request, 'add_medicine.html', {'form': form})
  def update_medicine(request, key_id):
    if request.method == 'POST':
      row = get_object_or_404(Supplier, pk=key_id)
      form = SupplierForm(request.POST,instance=row)
      if form.is_valid():
        form.save()
      return redirect('../')
    else:
      row = get_object_or_404(Supplier, pk=key_id)
      form = SupplierForm(instance=row)
    return render(request,'update_medicine.html',{'form':form})
  def delete_medicine(request,key_id):
    row = get_object_or_404(Supplier, pk=key_id)
    if request.method == 'POST':
      row.delete()
      return redirect('../../')
      # return redirect('/medicine/')
    return render(request, 'delete_medicine.html',{'object':row})
class CustomerView:
  def show_medicine(request):
    return render(request, 'show_medicine.html',{'object_list':Customer.objects.all()})
  def show_detail(request,key_id):
    row = get_object_or_404(Customer, pk=key_id)
    form = CustomerForm(instance=row)
    for field in form:
      field.is_date = isinstance(field.field, DateField)
    url_update = reverse("medicines:update-customer", kwargs={'key_id': key_id})
    url_delete = reverse("medicines:delete-customer", kwargs={'key_id': key_id})
    return render(request,'show_detail.html',{'form':form,'url_update': url_update,'url_delete':url_delete})
  def add_medicine(request):
    if request.method == 'POST':
      form = CustomerForm(request.POST)
      if form.is_valid():
        form.save()
        form = CustomerForm()
    else:
        form = CustomerForm()
    return render(request, 'add_medicine.html', {'form': form})
  def update_medicine(request, key_id):
    if request.method == 'POST':
      row = get_object_or_404(Customer, pk=key_id)
      form = CustomerForm(request.POST,instance=row)
      if form.is_valid():
        form.save()
      return redirect('../')
    else:
      row = get_object_or_404(Customer, pk=key_id)
      form = CustomerForm(instance=row)
    return render(request,'update_medicine.html',{'form':form})
  def delete_medicine(request,key_id):
    row = get_object_or_404(Customer, pk=key_id)
    if request.method == 'POST':
      row.delete()
      return redirect('../../')
      # return redirect('/medicine/')
    return render(request, 'delete_medicine.html',{'object':row})
class EmployeeView:
  def show_medicine(request):
    return render(request, 'show_medicine.html',{'object_list':Employee.objects.all()})
  def show_detail(request,key_id):
    row = get_object_or_404(Employee, pk=key_id)
    form = EmployeeForm(instance=row)
    for field in form:
      field.is_date = isinstance(field.field, DateField)
    url_update = reverse("medicines:update-employee", kwargs={'key_id': key_id})
    url_delete = reverse("medicines:delete-employee", kwargs={'key_id': key_id})
    return render(request,'show_detail.html',{'form':form,'url_update': url_update,'url_delete':url_delete})
  def add_medicine(request):
    if request.method == 'POST':
      form = EmployeeForm(request.POST)
      if form.is_valid():
        form.save()
        form = EmployeeForm()
    else:
        form = EmployeeForm()
    return render(request, 'add_medicine.html', {'form': form})
  def update_medicine(request, key_id):
    if request.method == 'POST':
      row = get_object_or_404(Employee, pk=key_id)
      form = EmployeeForm(request.POST,instance=row)
      if form.is_valid():
        form.save()
      return redirect('../')
    else:
      row = get_object_or_404(Employee, pk=key_id)
      form = EmployeeForm(instance=row)
    return render(request,'update_medicine.html',{'form':form})
  def delete_medicine(request,key_id):
    row = get_object_or_404(Employee, pk=key_id)
    if request.method == 'POST':
      row.delete()
      return redirect('../../')
      # return redirect('/medicine/')
    return render(request, 'delete_medicine.html',{'object':row})
class SaleView:
  def show_medicine(request):
    return render(request, 'show_medicine.html',{'object_list':Sale.objects.all()})
  def show_detail(request,key_id):
    row = get_object_or_404(Sale, pk=key_id)
    form = SaleForm(instance=row)
    for field in form:
      field.is_date = isinstance(field.field, DateField)
    url_update = reverse("medicines:update-sale", kwargs={'key_id': key_id})
    url_delete = reverse("medicines:delete-sale", kwargs={'key_id': key_id})
    return render(request,'show_detail.html',{'form':form,'url_update': url_update,'url_delete':url_delete})
  def add_medicine(request):
    # if request.method == 'POST':
    #   form = SaleForm(request.POST)
    #   if form.is_valid():
    #     form.save()
    #     form = SaleForm()
    # else:
    #   form = SaleForm()
    # return render(request, 'add_medicine.html', {'form': form})
    if request.method == 'POST':
      # Kiểm tra nếu đang ở bước "Calculate"
      if 'calculate' in request.POST:
        form = SaleForm(request.POST)
        if form.is_valid():
          # sale = form.cleaned_data['sale_id']
          medicine = form.cleaned_data['medicine_id']
          # customer = form.cleaned_data['customer_id']
          quantity = form.cleaned_data['quantity_sold']
          # date = form.cleaned_data['sale_date']
          
          # Tính toán total_price
          total = medicine.price * quantity

          # Gắn giá trị total_price vào form (chưa lưu vào database)
          form.initial['total'] = total
          form.data = form.data.copy()  # Tạo bản sao POST data để sửa dữ liệu
          form.data['total'] = total

          return render(request, 'add_sale.html', {'form': form, 'step': 'calculate'})

      # Nếu đang ở bước "Save"
      elif 'save' in request.POST:
        form = SaleForm(request.POST)
        if form.is_valid():
          medicine = form.cleaned_data['medicine_id']
          quantity = form.cleaned_data['quantity_sold']
          try:
            medicine.reduce_stock(quantity)
          except ValueError as e:
            return render(request, 'add_sale.html', {
                'form': form,
                'step': 'initial',
                'error': str(e)
            })
          form.save()  # Lưu vào cơ sở dữ liệu

          # Tạo form mới sau khi lưu
          form = SaleForm()
          return render(request, 'add_sale.html', {'form': form, 'step': 'initial', 'message': 'Saved successfully!'})

    else:
      # Hiển thị form ban đầu
      form = SaleForm()

    return render(request, 'add_sale.html', {'form': form, 'step': 'initial'})
  def update_medicine(request, key_id):
    if request.method == 'POST':
      row = get_object_or_404(Sale, pk=key_id)
      form = SaleForm(request.POST,instance=row)
      if form.is_valid():
        form.save()
      return redirect('../')
    else:
      row = get_object_or_404(Sale, pk=key_id)
      form = SaleForm(instance=row)
    return render(request,'update_medicine.html',{'form':form})
  def delete_medicine(request,key_id):
    row = get_object_or_404(Sale, pk=key_id)
    if request.method == 'POST':
      row.delete()
      return redirect('../../')
      # return redirect('/medicine/')
    return render(request, 'delete_medicine.html',{'object':row})

# class MedicineView:
#   def show_medicine(request):
#     return render(request, 'show_medicine.html',{'object_list':Medicine.objects.all()})
#   def show_detail(request,medicine_id):
#     # row = get_object_or_404(Medicine, medicine_id=medicine_id)
#     # # return render(request, 'show_detail.html',{'object':Medicine.objects.get(pk=id)})
#     # return render(request, 'show_detail.html',{'object':row})
    
#     # <!-- <td>
#     #     {% if field.field.__class__.__name__ == "DateField" %}
#     #         {{ field.value|date:"d/m/Y" }}
#     #     {% else %}
#     #         {{ field.value }}
#     #     {% endif %}
#     #   </td> -->

#     # <!-- <button onclick="location.href='{% url 'medicines:update-medicine' object.medicine_id %}';">Update</button>
#     # <button onclick="location.href='{% url 'medicines:delete-medicine' object.medicine_id %}';">Delete</button> -->

#     row = get_object_or_404(Medicine, pk=medicine_id)
#     form = MedicineForm(instance=row)
#     for field in form:
#         field.is_date = isinstance(field.field, DateField)
#     return render(request,'show_detail.html',{'form':form})

#   # def is_admin(user):
#   #   return user.is_superuser
#   # @user_passes_test(is_admin)
  # def add_medicine(request):
  #   if request.method == 'POST':
  #     form = MedicineForm(request.POST)
  #     if form.is_valid():
  #       # m_id = form.cleaned_data['medicine_id']
  #       # nm = form.cleaned_data['name']
  #       # c_id = form.cleaned_data['category_id']
  #       # df = form.cleaned_data['dosage_form']
  #       # sth = form.cleaned_data['strength']
  #       # qis = form.cleaned_data['quantity_in_stock']
  #       # pr = form.cleaned_data['price']
  #       # ed = form.cleaned_data['expiry_date']
  #       # s_id = form.cleaned_data['supplier_id']
  #       # # Category.objects.get(categoty_id=c_id)
  #       # # Supplier.objects.get(supplier_id=s_id)
  #       # reg = Medicine(medicine_id=m_id,name=nm,category_id=c_id,dosage_form=df,strength=sth,quantity_in_stock=qis,price=pr,expiry_date=ed,supplier_id=s_id)
  #       # reg.save()
  #       form.save()
  #       form = MedicineForm()
  #   else:
  #     form = MedicineForm()
  #   return render(request, 'add_medicine.html', {'form': form})
#   # @user_passes_test(is_admin)
#   def update_medicine(request, medicine_id):
#     # update: form ra id cua cac class khac chu khong hien ra ..._id cua class
#     if request.method == 'POST':
#       row = get_object_or_404(Medicine, medicine_id=medicine_id)
#       form = MedicineForm(request.POST,instance=row)
#       if form.is_valid():
#         form.save()
#       return redirect('../')
#     else:
#       row = get_object_or_404(Medicine, medicine_id=medicine_id)
#       form = MedicineForm(instance=row)
#     return render(request,'update_medicine.html',{'form':form})
#   # @user_passes_test(is_admin)
#   def delete_medicine(request,medicine_id):
#     row = get_object_or_404(Medicine, medicine_id=medicine_id)
#     if request.method == 'POST':
#       row.delete()
#       return redirect('../../')
#       # return redirect('/medicine/')
#     return render(request, 'delete_medicine.html',{'object':row})

# class CategoryView:
#   def show_category(request):
#     return render(request, 'show_medicine.html',{'object_list':Category.objects.all()})
#   def show_detail(request, category_id):
#     row = get_object_or_404(Category, category_id=category_id)
#     return render(request, 'show_detail_category.html', {'object': row})
#   def add_category(request):
#     if request.method =='POST':
#       form = CategoryForm(request.POST)
#       if form.is_valid():
#         form.save()
#         form = CategoryForm()
#     else:
#       form = CategoryForm()
#     return render(request, 'add_medicine.html', {'form': form})
#   def update_category(request, category_id):
#     if request.method == 'POST':
#       row = get_object_or_404(Category, category_id=category_id)
#       form = CategoryForm(request.POST, instance=row)
#       if form.is_valid():
#         form.save()
#       return redirect('../')
#     else:
#       row = get_object_or_404(Category, category_id=category_id)
#       form = CategoryForm(instance=row)
#     return render(request, 'update_medicine.html', {'form':form})
#   def delete_category(request, category_id):
#     row = get_object_or_404(Category, category_id=category_id)
#     if request.method == 'POST':
#       row.delete()
#       return redirect('../../')
#     return render(request, 'delete_medicine.html', {'object':row})
# class SupplierView:
#   def show_supplier(request):
#     return render(request, 'show_medicine.html', {'object_list':Supplier.objects.all()})
  
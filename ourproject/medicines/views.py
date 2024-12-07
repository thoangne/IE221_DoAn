from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .forms import MedicineForm
from .models import Medicine

# Create your views here.
def show_medicine(request):
  return render(request, 'show_medicine.html',{'object_list':Medicine.objects.all()})
def show_detail(request,id):
  return render(request, 'show_detail.html',{'object':Medicine.objects.get(pk=id)})
# def is_admin(user):
#   return user.is_superuser
# @user_passes_test(is_admin)
def add_medicine(request):
  if request.method == 'POST':
    form = MedicineForm(request.POST)
    if form.is_valid():
      m_id = form.cleaned_data['medicine_id']
      nm = form.cleaned_data['name']
      c_id = form.cleaned_data['catelogy_id']
      df = form.cleaned_data['dosage_form']
      sth = form.cleaned_data['strength']
      qis = form.cleaned_data['quantity_in_stock']
      pr = form.cleaned_data['price']
      ed = form.cleaned_data['expiry_date']
      reg = Medicine(medicine_id=m_id,name=nm,catelogy_id=c_id,dosage_form=df,strength=sth,quantity_in_stock=qis,price=pr,expiry_date=ed)
      reg.save()
      # form.save()
      form = MedicineForm()
  else:
    form = MedicineForm()
  return render(request, 'add_medicine.html', {'form': form})
# @user_passes_test(is_admin)
def update_medicine(request, id):
  if request.method == 'POST':
    row = Medicine.objects.get(pk=id)
    form = MedicineForm(request.POST,instance=row)
    if form.is_valid():
      form.save()
  else:
    row = Medicine.objects.get(pk=id)
    form = MedicineForm(instance=row)
  return render(request,'update_medicine.html',{'form':form})
# @user_passes_test(is_admin)
def delete_medicine(request,id):
  row = Medicine.objects.get(pk=id)
  if request.method == 'POST':
    row.delete()
    return redirect('/medicine/')
  return render(request, 'delete_medicine.html',{'object':row})
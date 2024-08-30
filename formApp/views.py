from django.shortcuts import render, redirect, get_object_or_404
from .form import StudentForm
from .models import StudentReg
import uuid
# Create your views here.

# This handles listing student data
def student_list(request):
    context = {
        'students': StudentReg.objects.all()
    }
    return render(request, 'formApp/templates/loctechstudents/std_table.html', context)

# This is the view function for the student registration form
# def student_reg(request, student_id=None):
#     if request.method == 'GET':
#         if student_id == None:
#             form = StudentForm()
#         else:
#             student = StudentReg.objects.get(pk=student_id)
#             form = StudentForm(instance=student) 
#         return render(request, 'formApp/templates/loctechstudents/reg_form.html', {'form': form})
#     else:   
#         if student_id == 0:
#             form = StudentForm(request.POST, request.FILES)
#         else:
#             student = StudentReg.objects.get(pk=student_id)
#             form = StudentForm(request.POST, request.FILES, instance=student)
#         if form.is_valid():
#             form.save()
#         return redirect('list/')

def student_reg(request, student_id=0):
    if request.method == 'GET':
        if student_id == 0:
            form = StudentForm()
        else:
            if StudentReg.objects.filter(pk=student_id).exists():
                student = StudentReg.objects.get(pk=student_id)
                form = StudentForm(instance=student)
            else:
                # Handle the case where the student does not exist
                # You can redirect, show an error message, etc.
                form = StudentForm()  # or some other action
        return render(request, 'formApp/templates/loctechstudents/reg_form.html', {'form': form})
    else:
        if student_id == 0:
            form = StudentForm(request.POST)
        else:
            if StudentReg.objects.filter(pk=student_id).exists():
                student = StudentReg.objects.get(pk=student_id)
                form = StudentForm(request.POST, instance=student)
            else:
                # Handle the case where the student does not exist
                # You can redirect, show an error message, etc.
                form = StudentForm(request.POST)  # or some other action
        if form.is_valid():
            form.save()
            return redirect(student_list)
        else:
            return render(request, 'formApp/templates/loctechstudents/reg_form.html', {'form': form})


# This view function handles deleting student data
def student_delete(request, student_id):
    student = StudentReg.objects.get(pk=student_id)
    student.delete()
    return redirect('student_list')
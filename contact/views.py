from django.shortcuts import render
from contact import models
from django.contrib import messages

# Create your views here.

def contact(request):
    if request.method == 'POST':
      first_name = request.POST['first_name']
      last_name = request.POST['first_name']
      email = request.POST['email']
      subject = request.POST['subject']
      message= request.POST['message']
      print(email)
      ins = models.Contact(first_name =first_name , last_name =last_name, email =email, message =message, subject =subject)
      ins.save()
      messages.success (request, f"message sent")
    return render(request,'contact.html')
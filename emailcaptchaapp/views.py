from django.shortcuts import render, redirect
from .models import Contact
from .forms import MyForm
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    return render(request, "home.html")
# Create your views here.
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        contact=Contact(name=name, email=email, phone=phone, content=content)

        form = MyForm(request.POST)
        if form.is_valid():
            print("Form Submitted")
            contact.save()
        else:
            print("Form not submitted")
        
        # Email Sending Code Starts
        subject = "Website Inquiry" 
        try:
            send_mail(subject, content, email, ['himseo17jan@gmail.com']) 
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect ('contact')
        # Email Sending Code Ends
        
    form = MyForm()
    return render(request, "contact.html",{'form':form})

# def contact(request):
#     if request.method == "POST":
#         form = MyForm(request.POST)
#         if form.is_valid():
#             print("Form Submitted")
#         else:
#             print("Form not submitted")
#     form = MyForm()
#     return render(request, 'contact.html', {'form':form})

def captest(request):
    form = MyForm()
    return render(request, 'contact.html',{'form':form})
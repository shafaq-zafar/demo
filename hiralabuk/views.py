from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.core.mail import send_mail
from service.models import Contact

    
def Contactus (request):
    return render(request, "Contactus.html")

def saveforms(request):
    if request.method == "POST":

        # Email to the admin
        send_mail(
            'New Form Submission',
            f'Name: {request.POST.get("name")}\nEmail: {request.POST.get("email")}\nSubject: {request.POST.get("subject")}\nMessage: {request.POST.get("message")}',
            'hiralabuk@gmail.com',
            ['hiralabuk@gmail.com'],  # Admin's email address
            fail_silently=False,
        )

        # Save form data to the database
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        en = Contact(name=name, email=email, subject=subject, message=message)
        en.save()

    return redirect("Contactus")
    
def home (request):
    return render(request, "index.html")
def Digital(request):
    return render(request, "Digital.html")
def Download(request):
    return render(request, "Download.html")
def Accreditations(request):
    return render(request, "Accreditations.html")
def Specialize(request):
    return render(request, "Specialize.html")
def aboutus(request):
    return render(request, "aboutus.html")
def how1(request):
    print("Debug: how1 view called")
    return render(request, "how1.html")
def how2(request):
    print("Debug: how2 view called")
    return render(request, "how2.html")
def how3(request):
    print("Debug: how3 view called")
    return render(request, "how3.html")
def how4(request):
    print("Debug: how4 view called")
    return render(request, "how4.html")
def how5(request):
    print("Debug: how5 view called")
    return render(request, "how5.html")
def how6(request):
    print("Debug: how6 view called")
    return render(request, "how6.html")
def clear(request):
    print("Debug: clear view called")
    return render(request, "clear.html")
def crown(request):
    print("Debug: crown view called")
    return render(request, "crown.html")
def dental(request):
    print("Debug: dental view called")
    return render(request, "dental.html")
def fully(request):
    print("Debug: fully view called")
    return render(request, "fully.html")
def pressure(request):
    print("Debug: pressure view called")
    return render(request, "pressure.html")

def gallery (request):
    return render(request, "gallery.html")


def Scanbody (request):
    return render(request, "Scanbody.html")

def Scan (request):
    return render(request, "Scan.html")

def test (request):
    return render(request, "test.html")





    
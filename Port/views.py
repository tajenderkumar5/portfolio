from ast import NameConstant

from django.conf import settings
from Portfolio.settings import EMAIL_HOST_USER
from django.forms.forms import Form
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .forms import contactForm
from django.core.mail import send_mail
from .models import Contact
from django.contrib import messages


def homepage(request):
    form = contactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        name = form.cleaned_data['name']
        userEmail = form.cleaned_data['userEmail']
        sub = form.cleaned_data['sub']
        message = form.cleaned_data['message']
        data_list = '\nName :    ' + name + '\nSubject  :   ' + \
            sub + '\nMessage   :    ' + message + '\nEmail  :    ' + userEmail
        resend_Data = 'Hey ,' + \
            name+' Thanks for connecting 🥰 Your message means alot to me.If you have any queries,suggestions and anything ,feel free to  Contact me.You can contact me on my E-mail :- ' + \
            EMAIL_HOST_USER + ' as well as on contact number :- 8130636098\nRegards :\nTajender Kumar \n '
    # context = {
    #     "title": "contact us",
    #     "form": form
    # }
    # send_mail(subject,data,frommail,tomail)
        send_mail("Contact Details", data_list,
                  userEmail, [EMAIL_HOST_USER], fail_silently=False)
        send_mail("Thank You For Connecting.", resend_Data,
                  EMAIL_HOST_USER, [userEmail], fail_silently=False)
        print("mail sent successfully")
    # messages.success(request, 'Welcome to contact')
    # if request.method == 'POST':
    #     print("We are using post request")
    #     Name = request.POST['name']
    #     Email = request.POST['userEmail']
    #     Subject = request.POST['sub']
    #     Message = request.POST['message']
    # Name=request.POST['']

    # if len(Name) < 2 or len(Email) < 3 or len(Subject) < 10 or len(Message) < 4:
    #     messages.error(request, "Please fill the form correctly")
    # else:
    #     contact = Contact(Username=Name, UserEmail=Email,
    #                       Subject=Subject, Message=Message)
    #     contact.save()
    #     messages.success(
    #         request, "Your message has been successfully sent")
    # print(Name, Email, Subject, Message)

    return render(request, "index.html", {'form': form})
    # return render(request, "index.html")
    # return HttpResponse(request, "sms sent successfully")

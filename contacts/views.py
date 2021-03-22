from django.shortcuts import render,redirect
from  django.contrib import messages
from .models import Contact,Contactpage
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'you have already inquired about this car')
                return redirect('/cars/'+car_id)

        contact = Contact(car_id=car_id,car_title = car_title,user_id=user_id,first_name=first_name,last_name=last_name,customer_need=customer_need,phone=phone,city=city,state=state,email=email,message=message)
        admin_info = User.objects.get(is_superuser = True)
        admin_email = admin_info.email
        send_mail(
            'New Car enquiry: ' + car_title,
            'You have a new enquiry for the car ' + car_title + '. Login for more details',
            'saishashidhar66@gmail.com',
            [admin_email],
            fail_silently=False,
        )

        contact.save()
        messages.success(request,"your request has been submitted,we will get ask to you shortly")
        return redirect('/cars/'+car_id)
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        contact = Contactpage(name =  name, email = email, message = message)
        contact.save()
        send_mail(
            f"Message from {name}",
            "message",
            "saishashidhar66@gmail.com",
            ['saishashidhar66@gmail.com'],
            fail_silently=False )
        send_mail(
            f"Hlooo {name}",
            f"Thank You For Reaching Us about {message}\n Please Wait until Our Executive contact You \n Thank You for your Patiance   -Team 1234",
            "saishashidhar66@gmail.com",
            [email],
            fail_silently=False )
    return render(request, 'pages/contact.html')


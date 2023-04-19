from django.shortcuts import render, redirect
from django.contrib import messages
# from django.core.mail import send_mail
from .models import Contact
from django.core.mail import send_mail, EmailMessage
# from btre.settings import EMAIL_HOST_USER

# Create your views here.

def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        user_id = request.POST['user_id']
        if user_id == "":
            user_id = None
        if request.user.is_authenticated:
            user_id = request.user.id  
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.success(request, "Your Inquiry is already registered. A realtor will Contact you Soon.") 
                return redirect('/listings/' + listing_id);

        realtor_email = request.POST['realtor_email']

        # email feature currently not working. needs some revision.
        # Send Email
        
        # send_mail(
        #     'Property Listing Inquiry ',
        #     f'there has been an inquiry for { listing } Sign into the admin panel for more info.',
        #     EMAIL_HOST_USER,
        #     ['noorulislamv2@gmail.com','noorulislam770@gmail.com'],
        #     fail_silently=False
            
        # )

        # msg = EmailMessage("BTRE","Content of the message ",to=["noorulislamv2@gmail.com",])
        # msg.send()
        
        contact = Contact(listing = listing,listing_id = listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id) 
        contact.save()

        messages.success(request, "Your request has been submitted, a realtor will get back to you soon.") 
        return redirect('/listings/' + listing_id);
from django.shortcuts import render

from apps.contacts.models import Contact
# Create your views here.
def contact(request):
    contact = Contact.objects.all()
    context = {
        "contact" : contact
    }
    return render(request,'contact.html',context)
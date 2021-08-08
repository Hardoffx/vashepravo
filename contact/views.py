from django.shortcuts import render, get_object_or_404

from home.models import HaveQuestions, FooterNumber, Email
from .models import WebSite

from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ContactForm


def contact(request):
    website = WebSite.objects

    havequestions = HaveQuestions.objects
    footernumber = FooterNumber.objects
    email = Email.objects

    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            f.save()
            messages.info(request, 'Сообщение успешно отправлено!')
            return HttpResponseRedirect('/contact/')
    else:
        f = ContactForm()
    return render(request, 'contact.html', {
                                            'havequestions': havequestions,
                                            'footernumber': footernumber,
                                            'email': email,
                                            'website': website,

                                            'form': f,
                                            })

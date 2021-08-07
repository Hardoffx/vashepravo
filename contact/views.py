from django.shortcuts import render, get_object_or_404
from .models import Contactnumber

from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ContactForm


def contact(request):
    contact = Contactnumber.objects

    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            f.save()
            messages.info(request, 'Сообщение успешно отправлено!')
            return HttpResponseRedirect('/contact/')
    else:
        f = ContactForm()
    return render(request, 'contact.html', {'form': f,
                                            'contact': contact,

                                            })

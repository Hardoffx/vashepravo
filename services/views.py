from django.shortcuts import render, get_object_or_404

from .models import ServicesDescription

from contact.forms import ContactForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def services(request):
    service = ServicesDescription.objects

    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            f.save()
            messages.info(request, 'Сообщение успешно отправлено!')
            return HttpResponseRedirect('/services/')
    else:
        f = ContactForm()

    return render(request, 'services.html', {'service': service,
                                             'form': f,

                                             })


def services_details(request, servicesdescription_id):
    servicesdescription = get_object_or_404(ServicesDescription, pk=servicesdescription_id)
    print('Дискрипшин id: ' + str(servicesdescription_id))

    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            f.save()
            messages.info(request, 'Сообщение успешно отправлено!')
            return HttpResponseRedirect('/services/')
    else:
        f = ContactForm()

    return render(request, 'services_details.html', {'servicesdescription': servicesdescription,
                                                     'form': f
                                                     })

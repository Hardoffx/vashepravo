from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Infobox, AchievementBlock, UploadVideo, PracticeAreas, LawyerCard, VashePravoImg, Reviews,\
    Gallery, FooterNumber, Email, VkLink, WorkHours, HaveQuestions, BackgroundHome


from contact.forms import ContactForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def home(request):
    bases = Infobox.objects
    achievementblock = AchievementBlock.objects
    uploadvideo = UploadVideo.objects
    practicereas = PracticeAreas.objects
    lawyercard = LawyerCard.objects
    vashepravoimg = VashePravoImg.objects
    reviews = Reviews.objects
    gallery = Gallery.objects
    footernumber = FooterNumber.objects
    email = Email.objects
    vklink = VkLink.objects
    workhours = WorkHours.objects
    havequestions = HaveQuestions.objects
    backgroundhome = BackgroundHome.objects

    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            f.save()
            messages.info(request, 'Сообщение успешно отправлено!')
            return HttpResponseRedirect('/')
    else:
        f = ContactForm()

    return render(request, 'home.html', {'bases': bases,
                                         'achievementblock': achievementblock,
                                         'uploadvideo': uploadvideo,
                                         'practicereas': practicereas,
                                         'lawyercard': lawyercard,
                                         'vashepravoimg': vashepravoimg,
                                         'reviews': reviews,
                                         'gallery': gallery,
                                         'footernumber': footernumber,
                                         'email': email,
                                         'vklink': vklink,
                                         'workhours': workhours,
                                         'havequestions': havequestions,
                                         'backgroundhome': backgroundhome,

                                         'form': f,
                                         })

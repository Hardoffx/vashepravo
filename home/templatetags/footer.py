from django import template
from home.models import PracticeAreas, FooterNumber, Email, VkLink, WorkHours, HaveQuestions

register = template.Library()


@register.inclusion_tag('footer.html')
def get_footer():
    practicereas = PracticeAreas.objects
    footernumber = FooterNumber.objects
    email = Email.objects
    vklink = VkLink.objects
    workhours = WorkHours.objects
    havequestions = HaveQuestions.objects
    return {'practicereas': practicereas,
            'footernumber': footernumber,
            'email': email,
            'vklink': vklink,
            'workhours': workhours,
            'havequestions': havequestions,

            }
from django import template
from home.models import LawyerCard

register = template.Library()


@register.inclusion_tag('lawyer_card.html')
def get_lawyer_card():
    lawyercard = LawyerCard.objects
    return {'lawyercard': lawyercard}

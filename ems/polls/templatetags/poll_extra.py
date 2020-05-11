from django import template
from polls.models import Question

register = template.Library()


def upper(value, n):
    """"Converts a string into all uppercase"""
    return value.upper()[0:n]


register.filter('upper', upper)


@register.simple_tag
def recent_polls(n=5):
    """"returns recent polls"""
    question = Question.objects.all().order_by('-created_at')
    return question[0:n]

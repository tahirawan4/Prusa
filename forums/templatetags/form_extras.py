from django import template

register = template.Library()


@register.simple_tag
def get_something(answer, user_id):
    return answer.can_vote(user_id)

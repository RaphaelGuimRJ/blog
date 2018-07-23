from django import template

register = template.Library()




@register.filter(name='nome_post')
def nome_post(value):
   return str(value).replace(' ','-').lower()

from django import template

register = template.Library()




@register.filter(name='nome_post')
def nome_post(value):

      if value is not None:
         if' ' in str(value):
            return str(value).replace(' ', '-').lower()

         else:
            return str(value)

      else:
         return value

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
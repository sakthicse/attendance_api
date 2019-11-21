from django import template
register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})

@register.filter(name='addplaceholder')
def addph(field, text):
   return field.as_widget(attrs={"placeholder":text})

@register.simple_tag(name='addstr')
def addstr(arg1, arg2,arg3):
    """concatenate arg1 & arg2"""
    return str(arg1)+'_'+ str(arg2)+'_'+str(arg3)

@register.simple_tag(name='addstrmapp')
def addstrmapp(dictionary,arg1, arg2,arg3):
    """concatenate arg1 & arg2"""
    value = dictionary.get(str(arg1)+'_'+ str(arg2)+'_'+str(arg3))
    if not value:
    	value = "-"
    return value

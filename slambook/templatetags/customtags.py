from django import template
from slambook.models import Contributor
from slambook.models import Notifications,Type_Of_Notification

register = template.Library()
mess=""
@register.filter
def responded_gifts(value):
    return Contributor.objects.filter(giftchart=value,response=True).count()


@register.filter
def isread_contrib(value):
    return Contributor.objects.filter(giftchart=value,isreadcontrib=True).count()

@register.filter
def isread_receiver(value):
    return Contributor.objects.filter(giftchart=value,isreadreceiver=True).count()


@register.filter
def format_message(var, args):
    if args is None:
        n=Notifications.objects.filter(pk=var)
        return n.typeofNotification.notif_main_message 
#    arg_list = [arg.strip() for arg in args.split(',')]
    #n.typeofNotification.notif_main_message.format()
    print("Hello")
    print(args)
    return "working"


@register.filter
def concat_string(value_1, value_2):
    return str(value_1) + str(value_2)



@register.filter
def format_mess(var):
    n=Notifications.objects.get(pk=var)
    tn=Type_Of_Notification.objects.get(pk=n.typeofNotification.pk)   
    arg=n.arguments    
    arg=arg.split(',')
    m=tn.notif_main_message
    foutput=m.format(*arg)
    #n.typeofNotification.notif_main_message.format()
    return foutput


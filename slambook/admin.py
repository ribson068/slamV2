from django.contrib import admin
from .models import (CharacterTemplate,CQuestion,
                     RCTemplateCQuestions,Slams,Slam,SlamChart,Gift,
                     Answer,UserExtension,Gifts,GiftChart,Contributor,Slam_Group,Group_User_Add)

# Register your models here.

class CharacterTemplateAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(CharacterTemplate)
admin.site.register(CQuestion)
admin.site.register(RCTemplateCQuestions)
admin.site.register(Slams)
admin.site.register(Slam)
admin.site.register(SlamChart)
admin.site.register(Answer)
admin.site.register(Gifts)
admin.site.register(UserExtension)
admin.site.register(GiftChart)
admin.site.register(Gift)
admin.site.register(Contributor)
admin.site.register(Slam_Group)
admin.site.register(Group_User_Add)

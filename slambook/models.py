from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime


# Create your models here.

class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(default=datetime(1900,1,1))
    pro_pic = models.ImageField(null=True,blank=True)
    def __str__(self):
        return str(self.dob)
    
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserExtension.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userextension.save()

class CharacterTemplate(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    cq_template=models.CharField(max_length=32)
    date_time=models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return '{} - {}'.format(self.pk, self.cq_template)
    
    
class CQuestion(models.Model):
        user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
        cquestion=models.TextField()
        date_time=models.DateTimeField(auto_now_add=True, blank=True)
        
        def __str__(self):
            return self.cquestion
        
        
class RCTemplateCQuestions(models.Model):
        user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
        ctemplate=models.ForeignKey(CharacterTemplate,on_delete=models.CASCADE)
        cquestion=models.ForeignKey(CQuestion,on_delete=models.CASCADE)
        date_time=models.DateTimeField(auto_now_add=True, blank=True)
        
        def __str__(self):
            return self.cquestion
        

class Slams(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    slam_name=models.CharField(max_length=32)
    date_time=models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.slam_name
    
class Slam(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    cquestion=models.ForeignKey(CQuestion,on_delete=models.CASCADE)
    slam=models.ForeignKey(Slams,on_delete=models.CASCADE)
    typ=models.IntegerField()
    date_time=models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.cquestion.cquestion

    
class SlamChart(models.Model):
    fr=models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='fr')
    to=models.ForeignKey(User,on_delete=models.CASCADE,related_name='to')
    slam=models.ForeignKey(Slams,on_delete=models.CASCADE)
    date_time=models.DateTimeField(auto_now_add=True, blank=True)
    mess=models.TextField(blank=True)
    rmess=models.TextField(blank=True)
    is_fr=models.BooleanField(default=True)
    is_to=models.BooleanField(default=True)
    response=models.BooleanField(default=False)
    isreadslam=models.BooleanField(default=False)
    
    
class Answer(models.Model):
    slamchart=models.ForeignKey(SlamChart,on_delete=models.CASCADE)
    cquestion=models.ForeignKey(CQuestion,on_delete=models.CASCADE)
    ans=models.BigIntegerField(blank=True)
    date_time=models.DateTimeField(auto_now_add=True, blank=True)


# class Gifts(models.Model):
#     giftname=models.CharField(max_length=32)
    
#     def __str__(self):
#         return self.giftname
    
class Gifts(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    gift_name=models.CharField(max_length=32)
    date_time=models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.gift_name
    
    
class Gift(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    cquestion=models.ForeignKey(CQuestion,on_delete=models.CASCADE)
    gift=models.ForeignKey(Gifts,on_delete=models.CASCADE)
    typ=models.IntegerField()
    date_time=models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return str(self.pk)+str(self.gift.pk)
    
    
class GiftChart(models.Model):
    fr=models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='gfr')
    #to=models.ForeignKey(User,on_delete=models.CASCADE,related_name='gto')
    re=models.ForeignKey(User,on_delete=models.CASCADE,related_name='gre')
    gift=models.ForeignKey(Gifts,on_delete=models.CASCADE)
    date_time=models.DateTimeField(auto_now_add=True, blank=True)
    mess=models.TextField(blank=True)
    #rmess=models.TextField(blank=True)
    giftmess=models.TextField(blank=True)
    is_fr=models.BooleanField(default=True)
    #is_to=models.BooleanField(default=True)
    is_re=models.BooleanField(default=True)
    #response=models.BooleanField(default=False)
    #isreadslam=models.BooleanField(default=False)
    def __str__(self):
        return self.gift.gift_name

class Contributor(models.Model):
    contrib=models.ForeignKey(User,on_delete=models.CASCADE,related_name='gto')
    giftchart=models.ForeignKey(GiftChart,on_delete=models.CASCADE,related_name="gc")
    date_time=models.DateTimeField(auto_now_add=True, blank=True)
    rmess=models.TextField(blank=True)
    is_to=models.BooleanField(default=True)
    response=models.BooleanField(default=False)
    isreadgift=models.BooleanField(default=False)

class GiftAnswer(models.Model):
    contrib=models.ForeignKey(Contributor,on_delete=models.CASCADE)
    cquestion=models.ForeignKey(CQuestion,on_delete=models.CASCADE)
    ans=models.BigIntegerField(blank=True)
    date_time=models.DateTimeField(auto_now_add=True, blank=True)
    
    
    
    
class Slam_Group(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    group_name=models.CharField(max_length=32)
    date_time=models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.group_name
    
class Group_User_Add(models.Model):
        user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
        group=models.ForeignKey(Slam_Group,on_delete=models.CASCADE)
        date_time=models.DateTimeField(auto_now_add=True, null=True,  blank=True)
        def __str__(self):
            return str(self.group) +" - "+ str(self.user)
        


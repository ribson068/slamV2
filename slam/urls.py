"""slam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from slambook.views import (test_ajax,Questions,base_t,index_t,character_tlist,delete_char_t,EditTemplateName,CreateTemplate,main_t,cquestion_tlist,delete_cquestion_t,EditCQuestion,CreateCQuestion,delete_RCQT_t,RCQT_tlist,add_RCQT_t,slams_list,CreateSlams,EditSlamsName,delete_slams,list_slam,delete_slam,add_slam,generate_slam,list_user,send_slam,Inbox,Sent,Response,delete_inbox,delete_sent,view_slam,edit_slam,response_slam,view_response,profile_view,Gift_view,generate_gift,search_user,GiftReceiver_view,delete_gifts,Add_User_to_Group,add_gift,Gift_Creator,Gift_Creator_Content,Group_view,Delete_Group,EditSlamGroup,list_gift,delete_gift,gift_contributor,list_user_gift,send_gift,CreateSlamGroup,Group_Users_list,add_user_group,delete_user,Receiver,Receiverbox,change_password,edit_gift)
from usermanagement import urls
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views


from slambook.views import (response_gift)



urlpatterns = [
     url(r'^test/', test_ajax,name='test'),
    url(r'^usermanagement/', include(urls)),
    url(r'^addquestion/', Questions),
    url(r'^admin/', admin.site.urls),
    url(r'^base/', base_t),
    url(r'^createslam/',index_t,name="createslam"),
    url(r'^$',main_t,name="index_t"),
    url(r'^(?P<pk>\d+)/profile$',profile_view,name="profile_name"),
    #Character Template
    url(r'^delete_char_t/', delete_char_t,name="delete_char_t"),
    url(r'^list/',login_required(character_tlist.as_view()),name="charactertlist"),
    url(r'^(?P<pk>\d+)/edittemplate$', login_required(EditTemplateName.as_view()),name="edittemplate"),
    url(r'^createtemplate/', login_required(CreateTemplate.as_view()),name="createtemplate"),
    #Character Questions
    url(r'^delete_cquestion/', delete_cquestion_t,name="delete_cquestion"),
    url(r'^cqlist/',login_required(cquestion_tlist.as_view()),name="listcquestion"),
    url(r'^(?P<pk>\d+)/cqlist$',login_required(cquestion_tlist.as_view()),name="listcquestiont"),
    url(r'^(?P<pk>\d+)/(?P<slam>\d+)/cqlist$',login_required(cquestion_tlist.as_view()),name="listcquestion"),
    url(r'^(?P<pk>\d+)/editcquestion$', login_required(EditCQuestion.as_view()),name="editcquestion"),
    url(r'^createcquestion/', login_required(CreateCQuestion.as_view()),name="createcquestion"),
    url(r'^(?P<pk>\d+)/(?P<slam>\d+)/createcquestion$',login_required(CreateCQuestion.as_view()),name="scquestion"),
    url(r'^(?P<pk>\d+)/createcquestion$',login_required(CreateCQuestion.as_view()),name="rcquestion"),
    #RCQT
    url(r'^delete_RCQT_t/', delete_RCQT_t,name="delete_rcqt_t"),
    url(r'^(?P<pk>\d+)/rcqt$',login_required(RCQT_tlist.as_view()),name="rcqt"),
    url(r'^add_RCQT_t/',add_RCQT_t,name="add_rcqt_t"),
    #SLAMS
    url(r'^delete_slams/', delete_slams,name="deleteslams"),
    url(r'^slamslist/',login_required(slams_list.as_view()),name="listslams"),
    url(r'^(?P<pk>\d+)/editslams$', login_required(EditSlamsName.as_view()),name="editslams"),
    url(r'^createslams/', login_required(CreateSlams.as_view()),name="createslams"),
    url(r'^generateslam/', generate_slam,name="generateslam"),
    #SLAM
    url(r'^deleteslam/', delete_slam,name="deleteslam"),
    url(r'^(?P<pk>\d+)/listslam$',login_required(list_slam.as_view()),name="listslam"),
    url(r'^addslam/',add_slam,name="addslam"),
    #USER
    url(r'^(?P<pk>\d+)/listuser$',login_required(list_user.as_view()),name="listuser"),
    url(r'^sendslam/',send_slam,name="sendslam"),

    #INBOX RESPONSE and SENT
    url(r'^inbox/',login_required(Inbox.as_view()),name="inbox"),
    url(r'^sent/',login_required(Sent.as_view()),name="sent"),
    url(r'^response/',login_required(Response.as_view()),name="response"),
    url(r'^deleteinbox/', delete_inbox,name="deleteinbox"),
    url(r'^deletesent/', delete_sent,name="deletesent"),
    url(r'^(?P<pk>\d+)/viewslam$',login_required(view_slam.as_view()),name="viewslam"),
    url(r'^(?P<pk>\d+)/editslam$',login_required(edit_slam.as_view()),name="editslam"),
    url(r'^responseslam/',response_slam,name="responseslam"),
    url(r'^(?P<pk>\d+)/viewresponse$',login_required(view_response.as_view()),name="viewresponse"),
    #Gifts
    url(r'^gifts/',login_required(Gift_view.as_view()),name="gifts"),
    url(r'^generategift/',generate_gift,name="generategift"),
    url(r'^(?P<pk>\d+)/generategift/',generate_gift,name="generategift"),
    url(r'^searchuser/',login_required(search_user.as_view()),name="searchuser"),
    url(r'^filteruser/',login_required(search_user.as_view()),name="filteruser"),
    url(r'^(?P<pk>\d+)/listgift$',login_required(list_gift.as_view()),name="listgift"),
    url(r'^deletegifts/', delete_gifts,name="deletegifts"),
    url(r'^deletegift/', delete_gift,name="deletegift"),
    url(r'^(?P<pk>\d+)/listusergift$',login_required(list_user_gift.as_view()),name="listusergift"),
    url(r'^sendgift/',send_gift,name="sendgift"),
    url(r'^addgift/',add_gift,name="addgift"),
    url(r'^giftcreator/',login_required(Gift_Creator.as_view()),name="giftcreator"),
    url(r'^(?P<pk>\d+)/giftcreatorcontent$',login_required(Gift_Creator_Content.as_view()),name="giftcreatorcontent"),

    #Gift Receiver
    url(r'^giftreceiver/',login_required(GiftReceiver_view.as_view()),name="receiver"),

    #Gift Contributor
    url(r'^giftcontributor/',login_required(gift_contributor.as_view()),name="contributor"),


    #Groups URLs
    url(r'^slamgroup/',login_required(Group_view.as_view()),name="slamgroup"),
    url(r'^(?P<pk>\d+)/slamgroupedit$',login_required(EditSlamGroup.as_view()),name="slamedit"),
    url(r'^slamgroupdelete',Delete_Group,name="slamgroupdelete"),
    url(r'^creategroup/', login_required(CreateSlamGroup.as_view()),name="creategroup"),


    url(r'^listgroupusers/',login_required(Group_Users_list.as_view()),name="listgroupusers"),
    url(r'^(?P<pk>\d+)/listgroupusers/',login_required(Group_Users_list.as_view()),name="listgroupusers"),
    url(r'^AddUserToGroup/',login_required(Add_User_to_Group.as_view()),name="AddUserToGroup"),
    url(r'^(?P<pk>\d+)/AddUserToGroup/',login_required(Add_User_to_Group.as_view()),name="AddUserToGroup"),
    
    url(r'^AddGroupUser/',add_user_group,name="addgroupuser"),
    url(r'^delete_user/',delete_user,name="delete_user"),
    #url(r'^(?P<pk>\d+)/(?P<user>\d+)/addusertogroup$',login_required(add_user_group.as_view()),name="addgroupusers"),
    
    url(r'^receiver/',login_required(Receiver.as_view()),name="receiver"),
    url(r'^(?P<pk>\d+)/receiverbox/',login_required(Receiverbox.as_view()),name="receiverbox"),
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    url(r'^password/',change_password,name="change_password"),
    













































    url(r'^(?P<pk>\d+)/edit_gift/',login_required(edit_gift.as_view()),name="edit_gift"),
    url(r'^responsegift/',response_gift,name="responsegift"),
    
















































]

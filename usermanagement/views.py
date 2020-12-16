from django.shortcuts import render,redirect

from usermanagement.forms import SignUpForm
from django.contrib.auth import login,authenticate
from slambook.models import CharacterTemplate,CQuestion,RCTemplateCQuestions
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            c1=CharacterTemplate(cq_template='default1',user=user)
            c2=CharacterTemplate(cq_template='default2',user=user)
            c1.save()
            c2.save()
            r=CQuestion.objects.filter(user=User(pk=1))
            count=0
            for i in r:
                if count<5:
                    rc=RCTemplateCQuestions(user=user,ctemplate=c1,cquestion=i)
                    count=count+1
                else:
                    rc=RCTemplateCQuestions(user=user,ctemplate=c2,cquestion=i)
                rc.save()
            
            return redirect('index_t')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


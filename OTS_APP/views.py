from django.shortcuts import render
from django.template import loader
from OTS_APP.models import *
from django.http import HttpResponse,HttpResponseRedirect
import random

def welcome(requset):
    temp=loader.get_template('welcome.html')
    return HttpResponse(temp.render())
def CandidateRegistrationForm(request):
    return render(request,"registration_form.html")
def CandidateRegistration(request):
    if request.method=="POST":
        username=request.POST["username"]
        if (len(Candidate.objects.filter(Username=username))):
            userstatus=1
        else:
            candidate=Candidate()
            candidate.Username=username
            candidate.Password=request.POST["password"]
            candidate.Name=request.POST["name"]
            candidate.save()
            userstatus=2
    else:
        userstatus=3
    return render(request,"RegistrationStatus.html",{'userstatus':userstatus})
def Loginview(request):
   if request.method=="POST":
       username=request.POST['username']
       password=request.POST['password']
      
       candidate=Candidate.objects.filter(Username=username,Password=password)
    
       if(len(candidate)==0):
           logerror="invalid username or password"
           res=render(request,"login.html",{'loginerror':logerror})
       else:
           request.session['username']=candidate[0].Username
           request.session['name']=candidate[0].Name
           res=HttpResponseRedirect("home")
   else:
       res=render(request,"login.html") 
   return res
def CandidateHome(request):
   if 'name' not in request.session.keys():
       return HttpResponseRedirect("login")
   else:
       return render(request,"home.html")
def TestPaper(request):
   if 'name' not in request.session.keys():
       return HttpResponseRedirect('login')

   n=int(request.GET['n'])
   question_pool=list(Question.objects.all())
   random.shuffle(question_pool)
   question_list=question_pool[:n]
   return render(request,'TestPaper.html',{'questions':question_list})
   
def CalculateTestResult(request):
     if 'name' not in request.session.keys():
       return HttpResponseRedirect('login')
     total_attempt=0  
     total_right=0
     total_wrong=0
     qid_list=[]
     for k in request.POST:
         if k.startswith('q'):
                  try:
                    qid_list.append(int(request.POST[k]))
                  except:
                      pass
          
     for n in qid_list:
         question=Question.objects.get(Queid=n)
         try:
             if question.Ans==request.POST['q'+str(n)]:
                 total_right+=1
             else:
                 total_wrong+=1
             total_attempt+=1
         except:
            pass
     points=(total_right-total_wrong)*2
     result=Result()
     result.Username=Candidate.objects.get(Username=request.session['username'])
     result.attempt=total_attempt
     result.Right=total_right
     result.Wrong=total_wrong
     result.points=points
     result.save()
     #update candidate
     candidate=Candidate.objects.get(Username=request.session['username'])
     candidate. Test_attempt+=1
     candidate.Points=(candidate.Points*(candidate.Test_attempt-1)+points)
     candidate.save()
     return HttpResponseRedirect('TestResult')
     
 
             

def ShowTestResult(request):
    if 'name' not in request.session.keys():
        return HttpResponseRedirect('login')
    result=Result.objects.filter(Resultid=Result.objects.latest('Resultid').Resultid)
    return render(request,'show_result.html',{'context':result})
   
def TestResultHistory(request):
     if 'name' not in request.session.keys():
        return HttpResponseRedirect('login')
     candidate=Candidate.objects.filter(Username=request.session['username']) 
     results=Result.objects.filter(Username=candidate[0].Username)
     context2={'candidate':candidate[0],'result':results}
     return render(request,"candidate_history.html",context2)
  
def Logout(request):
  if 'name'  in request.session.keys():
      del request.session['username']
      del request.session['name']
      return HttpResponseRedirect('login')
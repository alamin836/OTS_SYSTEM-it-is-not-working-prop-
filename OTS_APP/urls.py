from django.urls import path
from OTS_APP.views import *
app_name='OTS_APP'
urlpatterns=[
  path("",welcome),
  path("new-candidate",CandidateRegistrationForm,name="RegistrationForm"),
  path("store-candidate",CandidateRegistration,name="Registration"),
  path("login",Loginview,name="login"),
  path("home",CandidateHome,name="home"),
  path("test-paper",TestPaper,name="TestPaper"),
  path("calculate-result",CalculateTestResult,name="CalculateResult"),
  path("TestResult",ShowTestResult,name="TestResult"),
  path("result-history",TestResultHistory,name='TestHistory'),
  path("logout",Logout,name="logout"),
]
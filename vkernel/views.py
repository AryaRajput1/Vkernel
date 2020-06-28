from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages 
from vkernel.models import VideoTopic,Userdata,Membership,VideoContent
from django.views.decorators.csrf import csrf_exempt
from .paytm.paytm import generate_checksum,verify_checksum


# Create your views here.


MERCHANT_KEY = '21xR!3GBNEf55lvy'

def home(request):
    return render(request,'intro.html')
    
def mainpage(request):
    if(request.user.is_authenticated):
        videot=VideoTopic.objects.all()
        return render(request,'home.html',{"videot":videot})
    else:
        return redirect('/vkernel/')
def cvideo(request):
    return render(request,'videocontent.html')

def videostopic(request,id):
    user=Userdata.objects.filter(user=request.user)
    members=Membership.objects.all()
    if user[0].Member==members[0]:
         vt=VideoTopic.objects.filter(inMembership=user[0].Member)
    elif( user[0].Member==members[1]):
         vt=VideoTopic.objects.exclude(inMembership=members[2])
    else:
        vt=VideoTopic.objects.all()
    if user[0].Member is not None:
       topic=VideoTopic.objects.filter(vt_id=id)
       content=VideoContent.objects.filter( video_topic=topic[0])

       ab=[]
       for t in vt:
              ab.append(t.vt_id)
       if(id in ab):
         print("succes")
         print(content)
         return render(request,'vlistpage.html',{"vlst":content})
       else:
         print("error")
         return redirect('/vkernel/subscribe/')
    else:
       return redirect('/vkernel/subscribe/')

def videocontent(request,id):
    content=VideoContent.objects.filter(vc_id=id)
    return render(request,'videocontent.html',{"video":content[0]})
def loginpage(request):
    if(request.method=='POST'):
        name=request.POST.get('name')
        password=request.POST.get('password')
        user=authenticate(request,username=name,password=password)
        if user is not None:
            print('user exists')
            login(request,user)
            return redirect('/vkernel/mainpage/')
        else:
           return redirect('/vkernel/signup/')
    else:
        return render(request,'login.html')
def logoutpage(request):
    if(request.user.is_authenticated):
       logout(request)
       return render(request,'logout.html')
    else:
        return redirect('/vkernel/login/')
        
   
def signuppage(request):
  if(request.user.is_authenticated==False):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        user1=authenticate(request,username=name,password=password)
        if user1 is None:
            print('user not exists')
            usersample = User.objects.create_user(username=name,password=password,email=email)
            usersample.save()
            user1 = Userdata(user=usersample, u_phone=phone,Member=None)
            user1.save()
            return redirect('/vkernel/login/')
        else:
            print('worked')
            return redirect('/vkernel/login/')
           
    else:
        return render(request,'signup.html')
  else:
        return redirect('/vkernel/')
def account(request):
    if(request.user.is_authenticated):
        m=request.user
        userdata= Userdata.objects.filter(user=m)
        
        return render(request,'account.html',{"user":m,"userdata":userdata[0]})
    else:
        return redirect('/vkernel/login/')
def Buypage(request):
    if(request.user.is_authenticated):
        user=Userdata.objects.filter(user=request.user)
        member=Membership.objects.all()
        if(user[0].Member==None):
           
           messages.success(request, 'buy membership')
           
        else:
            messages.warning(request, 'upgrade  membership')
        return render(request,'subscribepage.html',{"Basic":member[0],"Premium":member[1],"Emperor":member[2]})
    else:
        return redirect('/vkernel/')
def Payment(request,id):
    payment=Membership.objects.filter(m_id=id)
    print(payment[0].price_month)
    print(payment[0].price_year)
    
    param={  'MID':'VcjDxQ77619025652125',
    
            'ORDER_ID':str(payment[0].m_id),
            'TXN_AMOUNT':str(payment[0].price_month),
            'CUST_ID':str(request.user.email),
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
            
	    'CALLBACK_URL':'http:127.0.0.1:8000/vkernel/handlerequest/',


    }
    param['CHECKSUMHASH']=generate_checksum(param,MERCHANT_KEY)
    return render(request,'paytm.html',{"paramdata":param})
@csrf_exempt
def handlerequest(request):
    m=''
    form = request.POST
   
    
    respons_dict = {}
    for i in form.keys():
        respons_dict[i]=form[i]
        if i=='CHECKSUMHASH':
            checksum = form[i]
    
    verify = verify_checksum(respons_dict, MERCHANT_KEY, checksum)
    if verify:
        if(respons_dict['RESPCODE']=='01'):
           m="succesful your payment"
           
        else:
            m="unsucceful your payment"
           
    return render(request,"succes.html",{"msg":m})


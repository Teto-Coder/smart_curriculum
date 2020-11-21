from django.shortcuts import render, redirect
from curriculum.models import UserData
from curriculum.models import UserData
# Create your views here.

# UserData.objects.create(userId='08360903',userName='林龍成',courses='1,2,3,4,5')
data = UserData.objects.all()

def curriculum(request):
    return render(request, 'index.html')

All_user = UserData.objects.all()


def Register(request):
    if request.method == 'POST':
        userName = request.POST.get('register-username')
        userEmail = request.POST.get('register-email')
        userPassword1 = request.POST.get('register-password')
        userPassword2 = request.POST.get('register-repeat-password')
        userSchool = request.POST.get('register-school')
        userMajor = request.POST.get('register-major')
        isTeacher = request.POST.get('register-teacher-code')
        
        if(userPassword1 == userPassword2):
            if not UserData.objects.filter(userName=userName):
                if(isTeacher == 8888):
                    UserData.objects.create(userName=userName,userEmail=userEmail,userPassword=userPassword1,userSchool=userSchool,userMajor=userMajor,isTeacher=True)
                else:
                    UserData.objects.create(userName=userName,userEmail=userEmail,userPassword=userPassword1,userSchool=userSchool,userMajor=userMajor)
            else:
                return render(request, 'index.html', {'islogin': 0,'alert':"帳號名稱已被使用"})
        else:
            return render(request, 'index.html', {'islogin': 0,'alert':"密碼輸入不一樣",})  
    return render(request, 'index.html', {'islogin': 1,'alert':"註冊成功",'u':userName})  

def login(request):
    if request.method == 'POST':
        u = request.POST.get('uu')
        p = request.POST.get('pp')
        if UserData.objects.filter(userName=u):
            if p == UserData.objects.filter(userName=u)[0].userPassword:   
                # 生成隨機字串儲存在cookie中 sessionid : xxxxx
                # 儲存在session中（資料庫）
                # 在服務端,每個隨機字串對應一個字典,儲存資訊
                request.session['user111'] = u
                request.session['is_login'] = True
                return render(request, 'index.html', {'islogin': 1,'alert':"登入成功",'u':u})

    return render(request, 'index.html', {'islogin': 0,'alert':"登入失敗"})

def index(request):
    u = request.session.get('user111')
    if request.session.get('is_login', None):
        return render(request, 'index.html', {'islogin': 1,'u':u,'alert':''})
    else:
        return render(request, 'index.html', {'islogin': 0,'u':u,'alert':''})


def logout(request):
    request.session.clear()
    return redirect('/index/')
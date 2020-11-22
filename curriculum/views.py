from django.shortcuts import render, redirect
from curriculum.models import UserData
from curriculum.models import UserData
import numpy as np
# Create your views here.

# UserData.objects.create(userId='08360903',userName='林龍成',courses='1,2,3,4,5')

# All_user = UserData.objects.all()

# for i in All_user:
#     i.delete()

def get_allcourse(name):
    all_course = UserData.objects.get(userName=name).courses
    all_course = all_course.split(',')
    print(type(all_course))
    return np.reshape(all_course,(14,7))

def Edit(request):
    u = request.session.get('user111')
    return render(request, 'index.html', {'islogin': 1,'u':u,'edit':True,'courses_data':get_allcourse(u)})  

def Finish(request):
    u = request.session.get('user111')
    return render(request, 'index.html', {'islogin': 1,'u':u,'edit':False,'courses_data':get_allcourse(u)})  

def change_course(request):
     return render(request, 'index.html', {'islogin': 1,'alert':"註冊成功",'u':userName,'courses_data':get_allcourse(userName)})  

def courses_info(request):
     return render(request, 'CourseInfo.html')

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
    return render(request, 'index.html', {'islogin': 1,'alert':"註冊成功",'u':userName,'courses_data':get_allcourse(userName)})  

def login(request):
    
    get_allcourse('andy010629')
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
                return render(request, 'index.html', {'islogin': 1,'alert':"登入成功",'u':u,'courses_data':get_allcourse(u)})

  #  result =  Computer.objects.order_by('?')[:1]
    return render(request, 'index.html', {'islogin': 0,'alert':"登入失敗"})

def index(request,alert=None):
    u = request.session.get('user111')
    if request.session.get('is_login', None):
        return render(request, 'index.html', {'islogin': 1,'u':u,'alert':'','courses_data':get_allcourse(u)})
    else:
        return render(request, 'index.html', {'islogin': 0,'u':u,'alert':alert})


def logout(request):
    request.session.clear()
    return redirect('/index/',alert="123")


def courses(request):
    request.session.clear()
    return redirect('/index/',alert="123")

from ast import LtE
from products.models import Addtocart
from food.models import FoodCategory
import string
import random
from datetime import timedelta
# from multiprocessing import context
# from tkinter.messagebox import NO
import uuid
from django.views.generic import ListView

import smtplib

import jwt
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import socket
from django.core.paginator import Paginator
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import views

from rest_framework_simplejwt.tokens import RefreshToken

from All_In_One import settings
from music.models import Album, AlbumHero, Hero
from products.models import Cloths, Category
import user
from user.models import UserData
from django.core.mail import send_mail
from All_In_One.settings import EMAIL_HOST_USER
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.urls import reverse

from .helper import send_forgot_password_mail

sender_address = 'spnnandu@gmail.com'
sender_pass = 'wrjgqfdixotpyabo'
socket.getaddrinfo('localhost', 8080)


if __name__ == '__main__':
    pass


def get_it_yours(request):
    return render(request, 'home/get_it_yours.html')


def about_us(request):
    return render(request, 'home/about_us.html')


def random_string(length=8, uppercase=True,
                  lowecase=True, numbers=True):
    charecter_set = '-'
    if uppercase:
        charecter_set += string.ascii_uppercase
    if lowecase:
        charecter_set += string.ascii_lowercase
    if numbers:
        charecter_set += string.digits
    return ''.join(random.choice(charecter_set) for i in range(length))


my_random = random_string(8)


def signup(request):
    try:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            error = False
            if request.method == 'POST':
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password']
                mobile = request.POST['mobile']
                image = request.FILES['image']
                mb = len(mobile)
                is_active = '0'
                unique_user_id = '#1'+my_random
                print('unique_user_id=', unique_user_id)
                if mb != 10:
                    message = 'mobile numbers must be contain 10 numbers'
                    return render(request, 'home/signup.html', {'message': message})
                else:
                    usr = User.objects.filter(email=email)
                if not usr:
                    user = User.objects.create_user(
                        username=username, password=password, email=email, is_active=is_active)
                    UserData.objects.create(
                        user=user, image=image, unique_user_id=unique_user_id, mobile=mobile)
                    user = User.objects.get(email=email)
                    token = RefreshToken.for_user(user).access_token
                    token.set_exp(lifetime=timedelta(days=36500))
                    current_site = get_current_site(request).domain
                    relativeLink = reverse('email-verify')
                    absurl = 'http://' + current_site + relativeLink +'?token=' + str(token)
                    reciver_mail = user.email
                    message = MIMEMultipart()
                    message['From'] = sender_address
                    message['To'] = reciver_mail
                    message['Subject'] = 'Registration confirmation! '
                    mail_content = 'hello' + ' ' + user.username + ' please click this below  link to verify your account ' \
                        '\n ' + absurl
                    message.attach(MIMEText(mail_content, 'plain'))
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    s.starttls()
                    s.login(sender_address, sender_pass)
                    text = message.as_string()
                    s.sendmail(sender_address, reciver_mail, text)
                    return redirect('login_signup')
                else:
                    error = True
    except IntegrityError:
        return render(request, 'home/signup.html', {'mesg': '...'})

    return render(request, 'home/signup.html', {'error': error})


class VerifyEmail(views.APIView):

    def get(self, request):
        token = request.GET.get('token')
        print('token=', token)
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=["HS256"])
            print('-----------')
            print(payload)

            user = User.objects.get(id=payload['user_id'])
            if not user.is_active:
                user.is_active = True
                user.save()

            return render(request, 'home/email-verify.html')
        except jwt.ExpiredSignatureError as identifier:
            return render(request, 'home/email-verify.html')


def login_signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        error = False

        if request.method == 'POST':
            dic = request.POST
            usr = dic['username']
            pwd = dic['password']
            print(usr)
            data = User.objects.filter(username=usr).first()
            print(data)

            user = authenticate(username=usr, password=pwd)
            print(user)

            if not data:
                print('-----')
                message = 'incorrect username'
                print(message)
                return render(request, 'home/login_signin.html', {'user_mesg': message})
            else:

                if not data.is_active:
                    message = 'account not verified, Please Check your mail to Activate the account'
                    return render(request, 'home/login_signin.html', {'message': message})

                else:

                    if user:
                        login(request, user)
                        return redirect('home')
                    else:
                        error = True

    return render(request, 'home/login_signin.html', {'error': error})


def logoutt(request):
    logout(request)
    return redirect('home')


def cloths(request):
    return render(request, 'home/cloths.html', {'cloths': Category.objects.all()})


def food(request):

    return render(request, 'home/food.html', {'res': FoodCategory.objects.all()})


# def (request):
#     album=Album.objects.all().order_by('album')
#     paginator = Paginator(album, 15)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'home/music.html',{'album': album,'hero':Hero.objects.all(),'page_obj': page_obj})


class Music(ListView):
    template_name = 'home/music.html'
    model = Album
    fields = "__all__"
    success_url = '/music/'
    paginate_by = 10

    def get_queryset(self):
        qs = Album.objects.all().order_by('album')
        return qs

    # album=Album.objects.all().order_by('album')
    # paginator = Paginator(album, 15)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # return render(request, 'home/music.html',{'album': album})


def hero(request):
    hero = Hero.objects.all()
    return render(request, 'home/music.html', {'hero': hero})


def filims(request):
    return render(request, 'home/films.html')


def wines(request):
    return render(request, 'home/wines.html')


def transport(request):
    return render(request, 'home/transport.html')


def tourism(request):
    return render(request, 'home/tourism.html')


def books(request):
    return render(request, 'home/books.html')


def electronics(request):
    return render(request, 'home/medicle.html')


def interiors(request):
    return render(request, 'home/interiors.html')


@login_required(login_url='login_signup')
def home(request):
    return render(request, 'home/index.html', {'res': Addtocart.objects.filter(user=request.user)})


def forgot_password(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')

            if not User.objects.filter(username=username).first():

                message = 'sorry , we are not found record with this username'
                return render(request, 'home/forgot_password.html', {'message': message})
            else:

                user_obj = User.objects.get(username=username)

                token = str(uuid.uuid4())
                profile_obj = UserData.objects.get(user=user_obj)
                profile_obj.forgot_password_token = token

                profile_obj.save()

                print('token=', token)
                send_forgot_password_mail(user_obj.email, token, request)

                print('email sent')
                message = 'email sent'
                return render(request, 'home/forgot_password.html', {'message': message})
    except Exception as e:
        print(e)

    return render(request, 'home/forgot_password.html')


def change_password(request, token):
    print('token=', token)
    print('request arrived')
    context = {}
    try:
        profile_obj = UserData.objects.filter(
            forgot_password_token=token).first()
        print('profile=', profile_obj)
        print('profile_obj=', profile_obj.user.id)
        context = {'user_id': profile_obj.user.id, 'token': token}
        if request.method == "POST":
            new_password = request.POST['password']
            c_password = request.POST['confirm_pasword']
            user_id = request.POST['user_id']
            user_obj = User.objects.get(id=user_id)
            user_obj.set_password(new_password)

            if user_id is None:
                return redirect(f'/change_password/{token}/')
            elif new_password != c_password:
                print('password not matched')
                return render(request, 'home/change_password.html', {'message': 'both passwords should match', 'token': token})
            else:

                print('password saved begins')
                user_obj.save()
                print('password saved')
                return redirect('/login_signup/')

    except Exception as e:
        print(e)

    return render(request, 'home/change_password.html', context)

def editemployee(request,pk):
    print('request arrived')
    print('pk for edit user=',pk)
    userdra=User.objects.filter(id=pk)
    print(userdra)
    usr=UserData.objects.filter(user_id=pk)
    print('usr=',usr)
    if request.method=="POST" or request.FILES:
        dic=request.POST
        username=dic['username']
        mobile=dic['mobile']
        print('username=',username)
        print('username=',mobile)
        image=dic['image']
        print('image=',image)
        userdra.update(username=username)
        usr.update(mobile=mobile,image=image)
        

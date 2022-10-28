from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from dashboard.forms import FeedBackForm
from dashboard.models import Dashboard
from user.models import UserData
from products.models import Addtocart
from django.contrib.auth.models import User
from dashboard.models import FeedBack
from food.models import RestaurentModel,FoodCategory
from food.forms import FoodForm




from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.urls import reverse
from django.db.models import Avg
from food.forms import RestaurentForm

from django.contrib.auth.models import User



# Create your views h


def dashboard_types(request):
    res=Dashboard.objects.all()
    return render(request,'dashboard/dashboard_types.html',{'res':res})


def dashboard(request):
    return render(request,'dashboard/dashboard.html')


def view_dashboard(request,pk):
    res=Dashboard.objects.filter(id=pk).first()
    print(res)
    
    if res.dashboard_type=='User':
        if request.user.is_authenticated:
            # puserdata=User.objects.get(username=request.user)
            userres=UserData.objects.filter(user=request.user)
            userdata=UserData.objects.all()
            # print(puserdata)
            return render(request,'dashboard/Userdashboard.html',{'userdata':userdata,'userres':userres})
        else:
            return render(request,'home/login_signin.html')
    elif res.dashboard_type=='SuperAdmin':
         return render(request,'dashboard/SuperAdmin.html')

    elif res.dashboard_type=='Food':
        res=FoodCategory.objects.all()
        print('category=',res)
        # print('form=',FoodForm())

        return render(request,'dashboard/Food.html',{'data':res})


def user_profile(request):
    res=UserData.objects.filter(user=request.user)
    c=Addtocart.objects.filter(user=request.user).count()
    print(res)

    return render(request,'dashboard/userprofile.html',{'res':res,'count':c})

def persional_profile(request):
    res=UserData.objects.filter(user=request.user)
    feedback=FeedBack.objects.filter(user=request.user)
    print(feedback)
    return render(request,'dashboard/persional_profile.html',{'res':res,'feedback':feedback})

def review_ratings(request):
    return render(request,'dashboard/reviews.html')



def rate(request):

    return render(request,'dashboard/reviews.html')


def submit_review(request):

    if request.method == 'POST':
        form = FeedBackForm(request.POST)

        if form.is_valid():

            rate = form.save(commit=False)

            rate.user = request.user
            #rate.movie = movie
            rate.save()
            return render(request,'dashboard/reviews.html')


def display_feedback(request):
    feedback=FeedBack.objects.filter(user=request.user)
    print(feedback)
    return render(request,'dashboard/display_feedback.html',{'feedback':feedback})





# def rate(request):
# 	#movie = Review.objects.get(imdbID=imdb_id)
# 	user = request.user

# 	if request.method == 'POST':
# 		form = RateForm(request.POST)
# 		if form.is_valid():
# 			rate = form.save(commit=False)
# 			rate.user = user
# 			#rate.movie = movie
# 			rate.save()
# 			return HttpResponseRedirect(reverse('movie-details', args=[id]))
# 	else:
# 		form = RateForm()

# 	template = loader.get_template('dashboard/reviews.html')

# 	context = {
# 		'form': form,
# 		#'movie': movie,
# 	}

# 	return HttpResponse(template.render(context, request))



def super_login(request):
    if request.method=='POST':
        dict=request.POST

        email=dict['email']
        password=dict['password']

        if email == 'SuperAdmin@gmail.com' and password =='SuperAdmin':
            tot=RestaurentModel.objects.all().count()
            rest_res=RestaurentModel.objects.filter(rest_status='Approved')
            rest_res_count=RestaurentModel.objects.filter(rest_status='Approved').count()
            prest_res=RestaurentModel.objects.filter(rest_status='Pending')
            prest_res_count=RestaurentModel.objects.filter(rest_status='Pending').count()
            rrest_res=RestaurentModel.objects.filter(rest_status='Rejected')
            rrest_res_count=RestaurentModel.objects.filter(rest_status='Rejected').count()
            users=UserData.objects.all().count()
            allusers=UserData.objects.all()
            return render(request,'dashboard/superadmindashboard.html',{'users':users,'allusers':allusers,'apppres':rest_res,'pres':prest_res,
                                                                        'rres':rrest_res,'rest_res_count':rest_res_count,
                                                                        'prest_res_count':prest_res_count,
                                                                        'rrest_res_count':rrest_res_count,'tcount':tot})
        else:
           return render(request,'dashboard/SuperAdmin.html',{'error':'sorry, either email or password is incorrect'})


def index2(request):
    return render(request,'SuperAdmin/index-2.html')

def index3(request):
    return render(request,'SuperAdmin/index-3.html')


def event_management(request):
    return render(request,'SuperAdmin/event-management.html')

def all_professors(request):
    return render(request,'SuperAdmin/all-professors.html')



def add_professor(request):
    return render(request,'SuperAdmin/add-professor.html')


def edit_professor(request):
    return render(request,'SuperAdmin/edit-professor.html')

def professor_profile(request):
    return render(request,'SuperAdmin/professor-profile.html')
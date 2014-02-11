from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib.auth.models import User
from golfapp.forms import UserForm, SignupForm, LoginForm, UserInfoForm, FeedForm, Course_ScoreForm, CoursesForm
from golfapp.models import UserInfo, Feed, Course, Game
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from golfapp.models import *


# ____________________________________________________________Home

def home_view(request):
        return render_to_response('home.html')

# ____________________________________________________________Signup

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password"],
            )
        return HttpResponseRedirect("/thanks/")
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/thanks/')
        else:
            # Show an error page
            data =  {
                "UserForm" : UserForm(),
                "SignupForm" : SignupForm()
            }
            return render(request, 'signup-page.html', data)

# ____________________________________________________________Login

@csrf_protect
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/dashboard/')
        else:
            return HttpResponseRedirect('/incorrect/')
    else:
        form = LoginForm()
        return render(request, 'login-page.html', {"LoginForm":form})


def incorrect_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect ('/dashboard/')
        else:
            return HttpResponseRedirect('/incorrect/')
    else:
        form = LoginForm()
        return render(request, 'incorrect-page.html', {"LoginForm":form})

# ____________________________________________________________Thanks

def show_thanks(request):
    return render_to_response('thanks.html')

# ____________________________________________________________Logout

@login_required
def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

# ____________________________________________________________Dashboard

def show_dashboard(request):
    users = User.objects.all() # Display all users
    user_count = User.objects.count() # Display total users
    dashboard_user = request.user # Display the loggedin user
    print dashboard_user # See name of loggedin user in terminal

    return render(request, 'dashboard.html', {'users':users, 'dashboard_user':dashboard_user, 'user_count':user_count})

# ____________________________________________________________Dashboard - Profile

@login_required
def create_profile(request):
    if request.method == 'GET':
        form = UserInfoForm()
    else:
        # A POST request: Handle Form Upload
        form = UserInfoForm(request.POST) # Bind data from request.POST into a PostForm

        # If data is valid, proceeds to create new profile post and redirect the user
        if form.is_valid():

            info = UserInfo()

            info.user_id = request.user.id
            info.name = form.cleaned_data['name']
            info.location= form.cleaned_data['location']
            info.birth_date = form.cleaned_data['birth_date']
            info.skill_level = form.cleaned_data['skill_level']
            info.website = form.cleaned_data['website']
            info.email = form.cleaned_data['email']
            info.gender = form.cleaned_data['gender']
            info.industry = form.cleaned_data['industry']
            info.occupation = form.cleaned_data['occupation']
            info.education = form.cleaned_data['education']
            info.degree = form.cleaned_data['degree']
            info.from_date_ed = form.cleaned_data['from_date_ed']
            info.to_date_ed = form.cleaned_data['to_date_ed']
            info.organization = form.cleaned_data['organization']
            info.org_location = form.cleaned_data['org_location']
            info.about_me = form.cleaned_data['about_me']
            info.from_date_org = form.cleaned_data['from_date_org']
            info.to_date_org = form.cleaned_data['to_date_org']

            info.save()
            return HttpResponseRedirect('dashboard/profile/profile_view/')

    return render(request, 'profile.html', {'form': form})


def view_profile(request):
    return render(request, 'profile_view.html', {})


# ____________________________________________________________ Filter users

def user_list(request):
    filter = UserInfoFilter(request.GET, queryset=UserInfo.objects.all())
    return render(request, 'dashboard.html', {'filter': filter})


# ____________________________________________________________ Search

def search(request):
    q = request.GET.get("q")
    print q
    if q:
       # use `__istartswith' for optimal search
       results = User.objects.filter(username__icontains=q)
    else:
       # you may want to return Customer.objects.none() instead
       results = User.objects.all()     

    context = dict(results=results, q=q)
    return render(request, "dashboard_search.html", context)


# ____________________________________________________________Tracker - Course

def view_tracker(request):
    if request.method == 'GET':
        form = CoursesForm()
    else:
        # A POST request: Handle Form Upload
        form = CoursesForm(request.POST) # Bind data from request.POST into a PostForm

        # If data is valid, proceeds to create new profile post and redirect the user
        if form.is_valid():

            info = CoursesForm()

            info.course = course.id
            info.course_name = form.cleaned_data['course_name']
            info.address = form.cleaned_data['address']
            info.city = form.cleaned_data['city']
            info.state = form.cleaned_data['state']
            info.zip = form.cleaned_data['zip']
            
       
            info.save()
            return HttpResponseRedirect('/dashboard/tracker/')

    return render(request, 'tracker.html', {'form': form})


# ____________________________________________________________Tracker - Scorecard

def view_tracker(request):
    if request.method == 'GET':
        form = Course_ScoreForm()
    else:
        # A POST request: Handle Form Upload
        form = Course_ScoreForm(request.POST) # Bind data from request.POST into a PostForm

        # If data is valid, proceeds to create new profile post and redirect the user
        if form.is_valid():


            info = Course_ScoreForm()

            info.golfcourse_id = Course.id
            info.hole_01 = form.cleaned_data['hole_01']
            info.hole_02 = form.cleaned_data['hole_02']
            info.hole_03 = form.cleaned_data['hole_03']
            info.hole_04 = form.cleaned_data['hole_04']
            info.hole_05 = form.cleaned_data['hole_05']
            info.hole_06 = form.cleaned_data['hole_06']
            info.hole_07 = form.cleaned_data['hole_07']
            info.hole_08 = form.cleaned_data['hole_08']
            info.hole_09 = form.cleaned_data['hole_09']
            info.hole_10 = form.cleaned_data['hole_10']
            info.hole_11 = form.cleaned_data['hole_11']
            info.hole_12 = form.cleaned_data['hole_12']
            info.hole_13 = form.cleaned_data['hole_13']
            info.hole_14 = form.cleaned_data['hole_14']
            info.hole_15 = form.cleaned_data['hole_15']
            info.hole_16 = form.cleaned_data['hole_16']
            info.hole_17 = form.cleaned_data['hole_17']
            info.hole_18 = form.cleaned_data['hole_18']
            
       
            info.save()
            return HttpResponseRedirect('/dashboard/tracker/')

    return render(request, 'tracker.html', {'form': form})

# ____________________________________________________________Map

def show_map(request):
    return render(request, 'main-maps.html', {})

# ____________________________________________________________Calendar

def show_cal(request):
    return render(request, 'calendar.html', {})

# ____________________________________________________________Buddy List

def friends_page(request, username):
    user = get_object_or_404(User, username=username)
    friends = [friendship.to_friend
    for friendship in user.friend_set.all()]
    friend_bookmarks = Bookmark.objects.filter(
    user__in=friends
    ).order_by('-id')
    variables = RequestContext(request, {
            'username': username,
            'friends': friends,
            'bookmarks': friend_bookmarks[:10],
            'show_tags': True,
            'show_user': True
        })
    return render_to_response('friends_page.html', variables)

# ____________________________________________________________Create Event

# @login_required
# def show_event(request, event_id)
#     event = get_object_or_404(Event, id=event_id)
#     if request.method == 'POST':
#         try:
#             id = request.POST.get('dashboard_id')
#             attendee = Profile.objects.get(id=id)
#             relationship = Event.objects.create(attendees__user=attendee, .... ) # set other variable you want
#             is_attending = True
#     else:
#         # check in your event either your profile user is already attending or not? and set is_attending variable according to it
#     data = { 
#             'is_attending': is_attending,
#              ....
#             }
#    return render_to_response('event.html',
#                           data,
#                           context_instance=RequestContext(request))

from django import forms
from django.contrib.auth.models import User
from golfapp.models import UserInfo, Feed, Game, Course_Score, Game_Holes, Course
from django.core.validators import MaxLengthValidator
from django.forms.extras.widgets import SelectDateWidget


# ____________________________________________________________Signup

class UserForm(forms.ModelForm):
    class Meta(object):
        model = User
        fields = ["username", "email", "password"]
        widgets = {
            "username":forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            "email":forms.EmailInput(attrs={'placeholder': 'E-mail', 'class': 'form-control'}),
            "password":forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
        }


class SignupForm(UserForm):
    confirm_password=forms.CharField(required=True,
        widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'})
    )


# ____________________________________________________________Login

class LoginForm(UserForm):
    class Meta(object):
        model = User
        fields = ["username", "password"]
        widgets = {
            "username":forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            "password":forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
        }


# ____________________________________________________________Dashboard - Profile

SKILL_CHOICES = (
    ('Beginner - 30+ handicap', 'Beginner - 30+ handicap'),
    ('Intermediate - 20-29 handicap', 'Intermediate - 20-29 handicap'),
    ('Advanced - 10-19 handicap', 'Advanced - 10-19 handicap'),
    ('Professional - Scrtch - 9 handicap', 'Professional - Scrtch - 9 handicap'),
)

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class UserInfoForm(forms.ModelForm):
    class Meta(object):
        model = UserInfo
        fields = ['name', 'location', 'birth_date', 'skill_level', 'website', 'email', 'gender', 'industry', 'occupation', 'company', 'education', 'degree', 'from_date_ed', 'to_date_ed', 'organization', 'org_location', 'about_me', 'from_date_org', 'to_date_org']
        widgets = {
            "name":forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
            "location":forms.TextInput(attrs={'placeholder': 'City, State', 'class': 'form-control'}),
            "birth_date":forms.DateInput(attrs={'placeholder': 'Birthday', 'class': 'form-control', 'type':"date", 'id':"dateForm"}),
            "skill_level":forms.Select(choices=SKILL_CHOICES),
            "website":forms.TextInput(attrs={'placeholder': 'Website URL', 'class': 'form-control'}),
            "email":forms.EmailInput(attrs={'placeholder': 'E-mail', 'class': 'form-control'}),
            "gender":forms.Select(choices=GENDER_CHOICES),
            "industry":forms.Textarea(attrs={'placeholder': 'Industry', 'class': 'form-control'}),
            "occupation":forms.TextInput(attrs={'placeholder': 'Occupation', 'class': 'form-control'}),
            "education":forms.TextInput(attrs={'placeholder': 'Education', 'class': 'form-control'}),
            "degree":forms.TextInput(attrs={'placeholder': 'Degree', 'class': 'form-control'}),
            "from_date_ed":forms.DateTimeInput(attrs={'placeholder': 'Birthday', 'class': 'form-control', 'id': 'date'}),
            "to_date_ed":forms.DateTimeInput(attrs={'placeholder': 'Birthday', 'class': 'form-control', 'id': 'date'}),
            "organization":forms.TextInput(attrs={'placeholder': 'Website', 'class': 'form-control'}),
            "org_location":forms.TextInput(attrs={'placeholder': 'Website', 'class': 'form-control'}),
            "about_me":forms.TextInput(attrs={'placeholder': 'Website', 'class': 'form-control'}),
            "from_date_org":forms.DateTimeInput(attrs={'placeholder': 'Birthday', 'class': 'form-control', 'id': 'date'}),
            "to_date_org":forms.DateTimeInput(attrs={'placeholder': 'Birthday', 'class': 'form-control', 'id': 'date'}),
        }
        
 
# ____________________________________________________________Dashboard - Activity Wall

class FeedForm(forms.ModelForm):
    class Meta(object):
        model = Feed
        feed = forms.CharField(widget=forms.Textarea, required=True, validators=[MaxLengthValidator(500)])

# ____________________________________________________________Dashboard - Events - Create Event

class GameForm(forms.ModelForm):
    class Meta(object):
        model = Game
        fields = ["date", "time", "user_id1", "user_id2", "user_id3", "user_id4"]

# ____________________________________________________________Dashboard - Events - Course

class CoursesForm(forms.ModelForm):
    class Meta(object):
        model = Course
        fields = ["course_name", "address", "city", "state", "zip"]
        widgets = {
            "course_name":forms.TextInput(attrs={'placeholder': 'Course', 'class': 'form-control'}),
            "address":forms.EmailInput(attrs={'placeholder': 'Course Address', 'class': 'form-control'}),
            "city":forms.PasswordInput(attrs={'placeholder': 'Course City', 'class': 'form-control'}),
            "state":forms.PasswordInput(attrs={'placeholder': 'Course State', 'class': 'form-control'}),
            "zip":forms.PasswordInput(attrs={'placeholder': 'Course Zip', 'class': 'form-control'})
        }


# ____________________________________________________________Dashboard - Tracker - Scorecard

class Course_ScoreForm(CoursesForm):
    class Meta(object):
        model = Course_Score
        fields = ['hole_01', 'hole_02', 'hole_03', 'hole_04', 'hole_05', 'hole_06', 'hole_07', 'hole_08', 'hole_09', 'hole_10', 'hole_11', 'hole_12', 'hole_13', 'hole_14', 'hole_15', 'hole_16', 'hole_17', 'hole_18']
        widgets = {
            "hole_01":forms.NumberInput(attrs={'placeholder': '1'}),
            "hole_02":forms.NumberInput(attrs={'placeholder': '2'}),
            "hole_03":forms.NumberInput(attrs={'placeholder': '3'}),
            "hole_04":forms.NumberInput(attrs={'placeholder': '4'}),
            "hole_05":forms.NumberInput(attrs={'placeholder': '5'}),
            "hole_06":forms.NumberInput(attrs={'placeholder': '6'}),
            "hole_07":forms.NumberInput(attrs={'placeholder': '7'}),
            "hole_08":forms.NumberInput(attrs={'placeholder': '8'}),
            "hole_09":forms.NumberInput(attrs={'placeholder': '9'}),
            "hole_10":forms.NumberInput(attrs={'placeholder': '10'}),
            "hole_11":forms.NumberInput(attrs={'placeholder': '11'}),
            "hole_12":forms.NumberInput(attrs={'placeholder': '12'}),
            "hole_13":forms.NumberInput(attrs={'placeholder': '13'}),
            "hole_14":forms.NumberInput(attrs={'placeholder': '14'}),
            "hole_15":forms.NumberInput(attrs={'placeholder': '15'}),
            "hole_16":forms.NumberInput(attrs={'placeholder': '16'}),
            "hole_17":forms.NumberInput(attrs={'placeholder': '17'}),
            "hole_18":forms.NumberInput(attrs={'placeholder': '18'}),
        }


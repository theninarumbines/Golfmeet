from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin



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

class UserInfo(models.Model):
    user = models.OneToOneField(User)
    buddies = models.ManyToManyField("self", blank=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    skill_level = models.CharField(max_length=50, choices=SKILL_CHOICES)
    website = models.URLField("Website", blank=True)
    email = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    industry = models.CharField(max_length=30, blank=True)
    occupation = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=30, blank=True)
    education = models.CharField(max_length=30, blank=True)
    degree = models.CharField(max_length=30, blank=True)
    from_date_ed = models.DateTimeField(blank=True, null=True)
    to_date_ed = models.DateTimeField(blank=True, null=True)
    organization = models.CharField(max_length=30, blank=True)
    org_location = models.CharField(max_length=30, blank=True)
    about_me = models.CharField(max_length=200, blank=True)
    from_date_org = models.DateTimeField(blank=True, null=True)
    to_date_org = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.name

# ____________________________________________________________Dashboard - Filter users


# ____________________________________________________________Dashboard - Tracker/Create Event

class Course(models.Model):
    course_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.IntegerField(max_length=5)

    def __unicode__(self):
        return self.course_name


class Course_Score(models.Model):
    golfcourse_id = models.ForeignKey(Course)
    courses = models.ManyToManyField("self", blank=True)
    description = models.CharField(max_length=255)
    hole_01 = models.IntegerField(max_length=2)
    hole_02 = models.IntegerField(max_length=2)
    hole_03 = models.IntegerField(max_length=2)
    hole_04 = models.IntegerField(max_length=2)
    hole_05 = models.IntegerField(max_length=2)
    hole_06 = models.IntegerField(max_length=2)
    hole_07 = models.IntegerField(max_length=2)
    hole_08 = models.IntegerField(max_length=2)
    hole_09 = models.IntegerField(max_length=2)
    hole_10 = models.IntegerField(max_length=2)
    hole_11 = models.IntegerField(max_length=2)
    hole_12 = models.IntegerField(max_length=2)
    hole_13 = models.IntegerField(max_length=2)
    hole_14 = models.IntegerField(max_length=2)
    hole_15 = models.IntegerField(max_length=2)
    hole_16 = models.IntegerField(max_length=2)
    hole_17 = models.IntegerField(max_length=2)
    hole_18 = models.IntegerField(max_length=2)


class Game(models.Model):
    date = models.DateTimeField()
    time = models.DateTimeField()
    golfcourse_id = models.ForeignKey(Course)
    user_id1 = models.ManyToManyField(User, related_name="player1")
    user_id2 = models.ManyToManyField(User, related_name="player2")
    user_id3 = models.ManyToManyField(User, related_name="player3")
    user_id4 = models.ManyToManyField(User, related_name="player4")

    def __unicode__(self):
        return self.name


class Event(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    about = models.TextField(null=True, blank=True)
    attendees = models.ManyToManyField(UserInfo, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Game_Holes(models.Model):
    user_id1 = models.ManyToManyField(Game, related_name="player1")
    user_id2 = models.ManyToManyField(Game, related_name="player2")
    user_id3 = models.ManyToManyField(Game, related_name="player3")
    user_id4 = models.ManyToManyField(Game, related_name="player4")

    def __unicode__(self):
        return self.name




# ____________________________________________________________Dashboard - Invites

class Friendship(models.Model):
    from_friend = models.ForeignKey(User, related_name='friend_set')
    to_friend = models.ForeignKey(User, related_name='to_friend_set')

    def __unicode__(self):
        return u'%s, %s' % (self.from_friend.username, self.to_friend.username)

    class Meta:
        unique_together = (('to_friend', 'from_friend'), )
        permissions = (('can_list_friend_bookmarks', 'Can list friend bookmarks'),)

# ____________________________________________________________Dashboard - Activity Wall

class Feed(models.Model):
    feed = models.CharField(max_length=500)
    creator = models.ForeignKey(User, blank=True, null=True)


    def __unicode__(self):
        return self.feed


# ____________________________________________________________Dashboard - Calendar


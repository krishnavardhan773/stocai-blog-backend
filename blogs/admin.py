from django.contrib import admin
from .models import BlogPost

admin.site.register(BlogPost)

from .models import StorySubmission

admin.site.register(StorySubmission)

from .models import Feedback

admin.site.register(Feedback)

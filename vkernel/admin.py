from django.contrib import admin
from vkernel.models import Userdata,VideoContent,VideoTopic,Membership
# Register your models here.
admin.site.register(Membership)
admin.site.register(VideoTopic)
admin.site.register(VideoContent)
admin.site.register(Userdata)
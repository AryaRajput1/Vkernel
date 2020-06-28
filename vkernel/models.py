from django.db import models

# Create your models here.
from django.contrib.auth.models import User



class Membership(models.Model):
    m_id=models.AutoField(primary_key=True)
    catagory=models.CharField(max_length=100,default='')
    price_month=models.IntegerField(default=0)
    price_year=models.IntegerField(default=0)

    def __str__(self):
        return self.catagory

class Userdata(models.Model):
    u_id=models.AutoField(primary_key=True)
    u_phone=models.CharField(max_length=10,default='')
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Member=models.ForeignKey(Membership,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.user)

class VideoTopic(models.Model):
    vt_id=models.AutoField(primary_key=True)
    vt_img=models.ImageField(upload_to="images/")
    vt_desc=models.CharField(max_length=200,default='')
    inMembership=models.ForeignKey(Membership,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.vt_desc

class VideoContent(models.Model):
    vc_id=models.AutoField(primary_key=True)
    vc_desc=models.CharField(max_length=200,default='')
    vc_video=models.CharField(default='',max_length=500,null=False)
    video_topic=models.ForeignKey(VideoTopic,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.vc_desc


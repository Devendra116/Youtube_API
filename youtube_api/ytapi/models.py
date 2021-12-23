from django.db import models

# Create your models here.
# {'kind': 'youtube#searchResult', 'etag': 'BaDF2Pnmpg88QqIaP99cPBVvHMU', 'id': {'kind': 'youtube#video', 'videoId': 'gfDE2a7MKjA'}, 'snippet': {'publishedAt': '2020-09-24T11:34:17Z', 'channelId': 'UCeVMnSShP_Iviwkknt83cww', 'title': 'Python Tutorial For Beginners In Hindi (With Notes) 
# 🔥', 'description': 'Learn Python One Video in Hindi: This Python Programming in Hindi tutorial is a complete python course in Hindi comprising of ...', 'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/gfDE2a7MKjA/default.jpg', 'width': 120, 'height': 90}, 'medium': {'url': 'https://i.ytimg.com/vi/gfDE2a7MKjA/mqdefault.jpg', 'width': 320, 'height': 180}, 'high': {'url': 'https://i.ytimg.com/vi/gfDE2a7MKjA/hqdefault.jpg', 'width': 480, 'height': 360}}, 'channelTitle': 'CodeWithHarry', 'liveBroadcastContent': 'none', 'publishTime': '2020-09-24T11:34:17Z'}}

class video(models.Model):
    kind = models.CharField(max_length=20)
    videoId = models.CharField(max_length=20)
    publishedAt = models.DateTimeField()
    channelId = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    channelTitle = models.CharField(max_length=20)
    thumbnails=models.CharField(max_length=25)
    description=models.TextField()
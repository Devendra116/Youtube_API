from django.shortcuts import render
from django.http import HttpResponse
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from ytapi.models import video
import datetime

#To get the first day of the current month in RFC 3339 formatted date-time value
first_day_of_the_month = datetime.date.today().replace(day=1)
firstdate=str(first_day_of_the_month)+'T00:00:00Z'


# this func help in avoiding the duplcate values in database
def checker(data):
    video_id=video.objects.values('videoId')
    video_id_list=[]
    for i in video_id:
        video_id_list.append(i['videoId'])
    if not (data.videoId in video_id_list):
        data.save()


# this function fires a get request for video with mentioned parameters 
def search_yt_video():
    try:
        search_url='https://www.googleapis.com/youtube/v3/search'
        # don't keep api open for production
        api_key='AIzaSyCbDM7NvdtXpiT8YCiB0JjuD6fG4maMsO4'
        params={
            'part':'snippet',
            'key':api_key,
            'q':'python',
            'maxResults':5,
            'type':'video',
            'order':'date',
            'publishedAfter':firstdate
        }
        r=requests.get(search_url,params=params)
        items=r.json()['items']
        for item in items:
            kind=item['id']['kind']
            videoId=item['id']['videoId']
            publishedAt=item['snippet']['publishedAt']
            channelId=item['snippet']['channelId']
            title=item['snippet']['title']
            channelTitle=item['snippet']['channelTitle']
            thumbnails=item['snippet']['thumbnails']['high']['url']
            description=item['snippet']['description']
            ins=video(kind=kind,videoId=videoId,channelTitle=channelTitle,publishedAt=publishedAt,channelId=channelId,title=title,thumbnails=thumbnails,description=description)
            checker(ins)
    except Exception as err:
        print('An Exception has occured :',err)

# This func display the data from database 
def display_video(request):
    content=video.objects.all().order_by('-publishedAt')
    search_yt_video()
    return render(request,'index.html',{'content':content})

# scheduler will call the search_yt_video after 10 sec 
scheduler = BackgroundScheduler()
scheduler.add_job(search_yt_video, 'interval', seconds=10)
scheduler.start()

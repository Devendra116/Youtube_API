# Youtube_API (Backend Assignment -Extern)

## Project Goal
#### *To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.*

## Project Implementation:
- Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of vid eos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- It should be scalable and optimised.

## Tech Stack
- Python
- Django

## To Run Project :
#### clone repo
```
git clone https://github.com/Devendra116/Youtube_API.git
```
#### Install requirement
```
pip install -r requirements.txt
```
#### Enter into youtube_api
``` 
cd youtube_api
```
#### Run this commands
```
py manage.py makemigrations
py manage.py migrate
```
#### (Optional) Create super user to access admin
```
py manage.py createsuperuser
```
#### TO Run the Server
```
py manage.py runserver
```
#### The Project is Live on 
```
http://127.0.0.1:8000/
```




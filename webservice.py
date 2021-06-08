# can cai pyrebase va python-firebase truoc khi chay
# def postDataToFirebase(path_local):
import pyrebase
from firebase import firebase
from datetime import datetime
from pyfcm import FCMNotification
import json
push_service = FCMNotification(
    api_key="AAAASt_Swfw:APA91bEti8HM6YStJi2gFSJYKkXf7xWQiRUzYGswGgam95BYeeZzIY963nOWsfl1E6eREcyxWkX7DxvkKeOrQ40xhW1Fk371iBZSVaOVu7zTetYBKwHR7RjbZfGwoO42bri7g8tXSR99")
firebase_app = firebase.FirebaseApplication(
    "https://fall-detect-4one-default-rtdb.firebaseio.com/", None)

registration_id = "fOYYBsnelUAFuDo83hwUZd:APA91bEG9HrNcz-Opez8OkEANggTW0f8CM63wBrAgqat0i4-hM4GxhBrACjmXJBlD0RLiNGMfg8Q2lnI1Y4Dkdhp7AL9I7n3A5HTEGfZt3g4qmwVm7xtjjrte4iUVlellZcwkCZPBVMk"

# lay thoi gian hien tai
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

results = firebase_app.get('/InforFall', None)

if (results):
    id = len(results) + 1
else:
    id = 1  # id nay trong luc chay se tang dan theo moi hinh va lam ten cua hinh

# push hinh anh len storage
config = {
    "apiKey": "AIzaSyCnA6GDhhKUR5CigO8haI-JDdfyoxE0ap0",
    "authDomain": "fall-detect-4one.firebaseapp.com",
    "databaseURL": "https://fall-detect-4one-default-rtdb.firebaseio.com/",
    "projectId": "fall-detect-4one",
    "storageBucket": "fall-detect-4one.appspot.com",
    "messagingSenderId": "321582711292",
    "appId": "1:321582711292:web:9ae44ab12c23b55e793279",
    "measurementId": "G-21Y3FWF0K8"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
path_local = "./images/falling.png"
path_on_cloud = "images/"+str(id)+".png"
storage.child(path_on_cloud).put(path_local)

# du lieu push len realtime database
data = {
    'id': id,
    'time': dt_string
}

result = firebase_app.post("/InforFall", data)  # push len realtime db
print(result)

# Send notification to CloudMessaging
message_title = "Fall Alert"
message_body = "Alert! Someone just fallen!"
result = push_service.notify_single_device(
    registration_id=registration_id, message_title=message_title, message_body=message_body)





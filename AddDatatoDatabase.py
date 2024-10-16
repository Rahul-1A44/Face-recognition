import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
'databaseURL': "https://faceattendance-819f3-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "1231":
        {
            "name": "Rahul Kumar Gupta",
            "major": "Python Developer",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "A",
            "year": 6,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1232":
        {
            "name": "Pukar Chapagai",
            "major": "UX-UI Designer",
            "starting_year": 2022,
            "total_attendance": 12,
            "standing": "B",
            "year": 6,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1233":
        {
            "name": "Roshan Shrestha",
            "major": "Full Stack Developer",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 6,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)


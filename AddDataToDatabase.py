import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://faceattendancerealtime-19931-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')
data = {
    '59562':
        {
            'name': 'Mark Zuckerberg',
            'major': 'Web Dev',
            'starting year': 2006,
            'total_attendance': 6,
            'standing': 'G',
            'year': 6,
            'last attendance_time': '2023-12-11 00:54:34'
        },
    '59999':
        {
            'name': 'Elon Musk',
            'major': 'Physics',
            'starting year': 2006,
            'total_attendance': 6,
            'standing': 'H',
            'year': 6,
            'last attendance_time': '2023-12-11 00:54:34'
        },
    '59189':
        {
            'name': 'Bill Gates',
            'major': 'CSE',
            'starting year': 2006,
            'total_attendance': 0,
            'standing': 'H',
            'year': 1,
            'last attendance_time': '2023-12-11 00:54:34'
        },
    '56666':
        {
            'name': 'xyz',
            'major': 'it',
            'starting year': 2008,
            'total_attendance': 0,
            'standing': 'H',
            'year': 2,
            'last attendance_time': '2023-12-11 00:54:34'
        }
}
for key, value in data.items():
    ref.child(key).set(value)

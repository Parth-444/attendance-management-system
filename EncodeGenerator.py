import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
from firebase_admin import storage


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://faceattendancerealtime-19931-default-rtdb.firebaseio.com/',
    'storageBucket': 'faceattendancerealtime-19931.appspot.com'
})



# importing student images
folderPath = 'Images'
PathList = os.listdir(folderPath)
imgList = []
studentIds = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    print(os.path.splitext(path)[0])
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)


# print(len(imgList))


def find_encodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


print('Encoding started')
encodeListKnown = find_encodings(imgList)
print(encodeListKnown)
encodeListKnownWithIds = [encodeListKnown,studentIds]
print('Encoding Complete')

with open('EncodeFile.p', 'wb') as file:
    pickle.dump(encodeListKnownWithIds, file)

print('File saved')


#FACE DETECTION

# import cv2
# img=cv2.imread("baby.jpg",cv2.IMREAD_COLOR)
# face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# faces=face_cascade.detectMultiScale(grey_img,1.1,3)
# print(faces)
# for(x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
# cv2.imshow("Face Detector",img)
# cv2.waitKey(5000)
# cv2.destroyAllWindow()

#EYE DETECTION

# import cv2
# img=cv2.imread("eye.jpeg",cv2.IMREAD_COLOR)
# face_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")
# grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# faces=face_cascade.detectMultiScale(grey_img,1.1,5)
# print(faces)
# for(x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
# cv2.imshow("Eye Detector",img)
# cv2.waitKey(5000)
# cv2.destroyAllWindow()

#NOSE DETECTION

# import cv2
# img=cv2.imread("nose.jpeg",cv2.IMREAD_COLOR)
# face_cascade=cv2.CascadeClassifier("nose.xml")
# grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# faces=face_cascade.detectMultiScale(grey_img,1.1,5)
# print(faces)
# for(x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
# cv2.imshow("Nose Detector",img)
# cv2.waitKey(5000)
# cv2.destroyAllWindow()

#LEFT-EAR DETECTION

# import cv2
# img=cv2.imread("ear.webp",cv2.IMREAD_COLOR)
# face_cascade=cv2.CascadeClassifier("left_ear.xml")
# grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# faces=face_cascade.detectMultiScale(grey_img,1.1,5)
# print(faces)
# for(x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
# cv2.imshow("Ear Detector",img)
# cv2.waitKey(5000)
# cv2.destroyAllWindow()

#RIGHT-EAR DETECTION


# import cv2
# img=cv2.imread("right_ear.webp",cv2.IMREAD_COLOR)
# face_cascade=cv2.CascadeClassifier("right_ear.xml")
# grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# faces=face_cascade.detectMultiScale(grey_img,1.1,5)
# print(faces)
# for(x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
# cv2.imshow("Ear Detector",img)
# cv2.waitKey(5000)
# cv2.destroyAllWindow()

#MOUTH DETECTION

# import cv2
# img=cv2.imread("mouth.webp",cv2.IMREAD_COLOR)
# face_cascade=cv2.CascadeClassifier("mouth.xml")
# grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# faces=face_cascade.detectMultiScale(grey_img,1.1,32)
# print(faces)
# for(x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
# cv2.imshow("Ear Detector",img)
# cv2.waitKey(5000)
# cv2.destroyAllWindow()
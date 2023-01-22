from deepface import DeepFace
import cv2
from mtcnn import MTCNN
# define a video capture object
vid = cv2.VideoCapture("http://192.168.1.5:4747/video")
models = [
"VGG-Face", # 0
"Facenet",  # 1
"Facenet512", # 2
"OpenFace", # 3
"DeepFace", # 4
"DeepID", # 5
"ArcFace", # 6
"Dlib", # 7
#   "SFace", # 8
]
backends = [
'opencv', # 0
'ssd', # 1
'dlib', # 2
'mtcnn', # 3
'retinaface', # 4 
'mediapipe'# 5
]
my_list_of_persons=["/home/abdullah/Data_Base_Project last 1-15-2022/Data_Base_Project/image_to_find/A.png","/home/abdullah/Data_Base_Project last 1-15-2022/Data_Base_Project/image_to_find/K.png"]
n=1
mtcnn = MTCNN()

while(True):
    try:
        ret, frame = vid.read()
        cv2.imshow('frame', frame)
        
        # result = DeepFace.verify(img1_path = frame , 
        #         img2_path = my_list_of_persons[n], 
        #         model_name = models[7],
        #         detector_backend=backends[2],enforce_detection=False
        #         )
        # print(my_list_of_persons[n],result["verified"])

    except:
        # n=0
        pass
vid.release()
cv2.destroyAllWindows()
print(len(my_list_of_persons))
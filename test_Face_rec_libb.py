from deepface import DeepFace

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

data=DeepFace.stream("/home/abdullah/Pictures/Screenshots/For_Search/",model_name=models[6],detector_backend=backends[4],time_threshold=1,frame_threshold=1,enable_face_analysis = False,)




































# import cv2
# import mtcnn
# from facenet_pytorch import MTCNN, InceptionResnetV1
# import torch

# # initialize the face detector and the face recognition model
# detector = mtcnn.MTCNN()
# arcface = InceptionResnetV1(pretrained='vggface2').eval()

# # The database of known faces, each key is a name, and the value is the embedding of the face
# face_database = {'person_name':arcface(torch.randn(1, 3, 160, 160))}

# # open the video stream
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
    
#     # detect faces in the frame
#     faces = detector.detect_faces(frame)
#     for face in faces:
#         # extract the bounding box of the face
#         x, y, width, height = face['box']
#         x1, y1 = abs(x), abs(y)
#         x2, y2 = x1 + width, y1 + height
        
#         # extract the face from the frame and preprocess it for face recognition
#         face_img = frame[y1:y2, x1:x2]
#         face_img = cv2.resize(face_img, (160, 160))
#         face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
#         face_img = (face_img / 255.0).astype(np.float32)
#         face_img = torch.from_numpy(face_img).permute(2, 0, 1)
#         face_img = face_img.unsqueeze(0)
        
#         # recognize the face
#         face_embedding = arcface(face_img)
#         dist = torch.sum(face_embedding * face_embedding, dim=1)
#         name = 'unknown'
#         for known_name, known_embedding in face_database.items():
#             dist = torch.sum((known_embedding - face_embedding) ** 2, dim=1)
#             if dist < min_dist:
#                 min_dist = dist
#                 name = known_name
#         # draw the bounding box and the name of the recognized face on the frame
#         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
#         cv2.putText(frame, name, (x1, y1 - 20), cv2.FONT_HERSHEY_SIMPLEX,
#                 0.75, (0, 0, 255), 2)
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

















# import face_recognition

# # Load the first image
# image1 = face_recognition.load_image_file("/home/abdullah/Data_Base_Project last 1-15-2022/Data_Base_Project/image_to_find/A.png")

# # Load the second image
# image2 = face_recognition.load_image_file("/home/abdullah/Pictures/Screenshots/To Insert/Screenshot from 2023-01-16 13-33-09.png")

# # Get the face encodings for each image
# encoding1 = face_recognition.face_encodings(image1)[0]
# encoding2 = face_recognition.face_encodings(image2)[0]

# # Compare the faces
# similarity_score = face_recognition.face_distance([encoding1], encoding2)

# # Convert similarity score to percentage
# similarity_percentage = (1 - similarity_score[0]) * 100

# print("Similarity Percentage: ", similarity_percentage)

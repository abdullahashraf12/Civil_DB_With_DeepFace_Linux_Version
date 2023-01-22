import cv2
from mtcnn import MTCNN
from deepface import DeepFace

# Load MTCNN model for face detection
mtcnn = MTCNN()

# Load DeepFace model for facial recognition
deepface = DeepFace.build_model(model_name="Dlib")

# Load known faces as a list of photo paths
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
known_faces_paths=["/home/abdullah/Data_Base_Project last 1-15-2022/Data_Base_Project/image_to_find/A.png","/home/abdullah/Data_Base_Project last 1-15-2022/Data_Base_Project/image_to_find/K.png"]

known_faces = []
for path in known_faces_paths:
    img = cv2.imread(path)
    embedding = DeepFace.represent(img, enforce_detection = False,model_name = models[7],detector_backend=backends[2])
    known_faces.append(embedding)

# Open video capture
cap = cv2.VideoCapture("http://192.168.1.5:4747/video")
while True:
    # Read frame from video capture
    ret, frame = cap.read()

    # Detect faces in frame
    faces = mtcnn.detect_faces(frame)

    # Iterate over each face
    for face in faces:
        x, y, w, h = face['box']
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        # Crop face from frame
        face_img = frame[y:y+h, x:x+w]

        # Get face embedding
        face_embedding = DeepFace.represent(face_img,enforce_detection = False,model_name = models[7],
                detector_backend=backends[2])

        # Compare face embedding to known faces
        # and output the best match
        best_match = DeepFace.verify(img1_path=frame, img2_path="/home/abdullah/Data_Base_Project last 1-15-2022/Data_Base_Project/image_to_find/A.png",
        model_name = models[7],detector_backend=backends[2],
                enforce_detection=True
        )
        cv2.putText(frame, "Match", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Display frame
    cv2.imshow('frame', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture
cap.release()
cv2.destroyAllWindows()

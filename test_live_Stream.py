import face_recognition
import cv2

# Load known faces and their names
known_faces = [
    face_recognition.load_image_file("/home/abdullah/Data_Base_Project last 1-15-2022/Data_Base_Project/image_to_find/A.png"),
    face_recognition.load_image_file("/home/abdullah/Data_Base_Project last 1-15-2022/Data_Base_Project/image_to_find/K.png"),
]
known_names = ["Abdullah Ashraf", "Khaled Ashraf"]

# Extract facial embeddings for known faces
known_faces_encodings = [face_recognition.face_encodings(f)[0] for f in known_faces]

# Open video capture
cap = cv2.VideoCapture("http://192.168.1.5:4747/video")

while True:
    # Read frame from video capture
    ret, frame = cap.read()

    # Detect faces
    faces_locations = face_recognition.face_locations(frame)
    faces_encodings = face_recognition.face_encodings(frame, faces_locations)

    # Iterate over each face
    for (top, right, bottom, left), face_encoding in zip(faces_locations, faces_encodings):
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Compare face encoding to known faces
        matches = face_recognition.compare_faces(known_faces_encodings, face_encoding)

        # If a match is found, display the name
        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            similarity_score = face_recognition.face_distance([known_faces_encodings], face_encoding)
            similarity_percentage = (1 - similarity_score[0]) * 100
            print("Similarity Score: ", similarity_percentage)
    cv2.imshow('Video', frame)
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow('Video', frame)
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # Release handle to the webcam
cap.release()
cv2.destroyAllWindows()

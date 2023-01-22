from deepface import DeepFace
my_face=DeepFace.find(img_path="/home/abdullah/Downloads/1.jpg",db_path="/home/abdullah/Pictures/Screenshots/For_Search/",model_name="ArcFace",detector_backend="mtcnn")
print(my_face["identity"][2])
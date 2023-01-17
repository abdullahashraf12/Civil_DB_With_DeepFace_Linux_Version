from deepface import DeepFace

# Initialize the ArcFace model with the 'resnet100' face detection model
arcface = DeepFace.build_model("arcface", model_type="resnet100")

# Perform face recognition
result = arcface.verify("path/to/image1.jpg", "path/to/image2.jpg")

similarity = 1 - (result["distance"] / 2)
print("Similarity Score:", similarity)
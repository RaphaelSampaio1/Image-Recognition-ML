import cv2
import matplotlib.pyplot as plt

def detect_faces(image_path):
    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Read the input image
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Unable to load image. Check the file path.")
        return
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw yellow rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 0), 8)  #  color 
    
    # Convert the BGR image to RGB (for matplotlib)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Display the result using matplotlib
    plt.imshow(image_rgb)
    plt.axis('off')  # Hide the axis
    plt.show()

# Predefined image path
image_path = r"C:\Users\WIN11\Downloads\Foto perfil.jpg"  # Update this with the correct image path
image_path2 = r"C:\Users\WIN11\Downloads\Peoples.jpg"  # Update this with the correct image path

# Call the face detection function
detect_faces(image_path2)

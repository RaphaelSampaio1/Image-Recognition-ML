# Face Detection with OpenCV

This project demonstrates how to use **OpenCV** to detect faces in an image and highlight them with a **black square** and **thicker lines**.

## Project Overview

This script loads an image, detects faces using a pre-trained Haar Cascade Classifier, and draws a **black square** with **thicker lines** around each detected face. It uses the **OpenCV** library for computer vision tasks and **Matplotlib** for displaying the image.

### Features:
- Detect faces in an image.
- Draw a **black square** around each detected face.
- The square has **thicker black lines** for better visibility.
- Uses **Haar Cascade Classifier** for face detection.

## Requirements

To run this project, you'll need:

- Python 3.x
- OpenCV
- Matplotlib

You can install the required libraries using the following commands:

```bash
pip install opencv-python
pip install matplotlib
```

## Code Explanation

1. **Face Detection using Haar Cascade Classifier**:
   - We use OpenCV's pre-trained Haar Cascade Classifier (`haarcascade_frontalface_default.xml`) to detect faces in the image.
   - The `detectMultiScale()` function detects the faces by looking for patterns that correspond to faces.

2. **Drawing a Black Square**:
   - Once faces are detected, the script draws a **black square** around each face. The side of the square is determined by the largest dimension (either width or height) of the detected face, ensuring that the square fully encloses the face.
   - The square is drawn using the `cv2.rectangle()` function, with a **thicker line width (10)** to make the square more visible.

3. **Displaying the Image**:
   - After detecting faces and drawing squares, the image is displayed using **Matplotlib**. This is a cross-platform solution that doesn't rely on OpenCV's GUI functionality, making it more robust across different environments.

## Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/face-detection.git
cd face-detection
```

2. Update the `image_path` variable in `face_detection.py` to the path of the image you want to use for face detection.

3. Run the script:

```bash
python face_detection.py
```

The script will display the image with detected faces highlighted by black squares.

## Example

Here’s an example of the result:

- The script detects the faces in the image.
- For each detected face, it draws a **black square** around the face.
- The lines of the square are **thicker** for better visibility.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Additional Notes:
- Make sure your image path is correct in the script (`image_path = r"C:\path\to\image.jpg"`).
- The script should work for most frontal faces but may not perform as well on rotated or side-profile faces.

If you need any further modifications or explanations, feel free to reach out!

---

You can replace `your-username` in the clone command with your GitHub username and feel free to modify any sections to match your repository’s specifics.

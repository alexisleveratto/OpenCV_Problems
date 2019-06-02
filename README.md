# Computer Vision Problems

Practicing OpenCV, to avoid getting rusty, using the free-online course given by awsomeness Adrian, creator of the  [PyImageSearch](https://www.pyimagesearch.com) platform.

### No. 01 -  Face Recognition
Perform fast, accurate face detection with OpenCV using a pre-trained deep learning face detector model shipped with the library.
- Run it:
    - For video: `python detect_faces_video.py -p deploy.prototxt.txt -m res10_300x300_ssd_iter_140000.caffemodel`
    - For images: `python face_detection_w_OpenCV.py -i sample_0.jpg -p deploy.prototxt.txt -m res10_300x300_ssd_iter_140000.caffemodel`

### No. 02 -  OpenCV Guide
Learning OpenCV isn’t as hard as it used to be. And in fact, I’ll go as far as to say studying OpenCV has become significantly easier.

- Run it:
    - Basic Image Manipulation: `python opencv_01.py -i jp.png`
    - Basic Color Image Manipulation: `python opencv_02.py -i tetris_blocks.png`

### No. 03 -  Scan a Document
Building a document scanner with OpenCV can be accomplished in just three simple steps:
1. Detect edges.
2. Use the edges in the image to find the contour (outline) representing the piece of paper being scanned.
3. Apply a perspective transform to obtain the top-down view of the document.

- Run it: `python scanner.py -i final-bill.jpg`

### No. 04 -  Multiple Choice Exam Scanner
Build a bubble sheet scanner and test grader using Python and OpenCV.
1. Detect the exam in an image.
2. Apply a perspective transform to extract the top-down, birds-eye-view of the exam.
3. Extract the set of bubbles (i.e., the possible answer choices) from the perspective transformed exam.
4. Sort the questions/bubbles into rows.
5. Determine the marked (i.e., “bubbled in”) answer for each row.
6. Determine if the mark was done once in the same question.
7. Detemine if the answer was done.
8. Lookup the correct answer in our answer key to determine if the user was correct in their choice.
9. Repeat for all questions in the exam.

- Run it: `python test_grader.py -i omr_test_01.png`
[Change the correct answers in the exam on **Line 17**, to see how it works.]

### No. 05 -  Object Tracking by Segmentation
The goal here is:
1. Detect the presence of a colored ball using computer vision techniques.
2. Track the ball as it moves around in the video frames, drawing its previous positions as it moves.

- Run it: `python object_tracking.py`
[Change color range on **Lines 19 and 20**, to see how it works.]

### No. 06 - Measuring size of objects in an image with OpenCV
We need to determine our “pixels per metric” ratio, which describes the number of pixels that can “fit” into a given number of inches, millimeters, meters, etc.

To compute this ratio, we need a reference object with some properties:

**Property #1:** The reference object should have known dimensions (such as width or height) in terms of a measurable unit (inches, millimeters, etc.).

**Property #2:** The reference object should be easy to find, either in terms of location of the object or in its appearance.

**Property #3:** All of the objects to be measured be co-planar with the reference object. 

- Run it: `python .\object_size.py -i .\example_03.png -w 3.5`

### No. 07 - Parkinson Detection with OpenCV
Reducing the requirement of tracking pen speed and pressure:
1. Eliminates the need for additional hardware when performing the test.
2. Makes it far easier to automatically detect Parkinson’s.

- Run it: `python detect_parkinsons.py --dataset dataset/spiral`

### No. 08 - Find Facial Landmarks
Facial landmarks are used to localize and represent salient regions of the face, such as:
* Eyes
* Eyebrows
* Nose
* Mouth
* Jawline

More info [here](https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/)

- Run it: `python facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat --image  img_1.jpg`

### No. 09 - Eye Blink Detection

To build our blink detector, we’ll be computing a metric called the eye aspect ratio (EAR), introduced by Soukupová and Čech in their 2016 paper, [Real-Time Eye Blink Detection Using Facial Landmarks](http://vision.fe.uni-lj.si/cvww2016/proceedings/papers/05.pdf).

The eye aspect ratio is approximately constant while the eye is open, but will rapidly fall to zero when a blink is taking place.

We can avoid image processing techniques and simply rely on the ratio of eye landmark distances to determine if a person is blinking.

### No. 13 - Find Facial Landmarks

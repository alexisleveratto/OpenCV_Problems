# Computer Vision Problems

Practicing OpenCV, to avoid getting rusty, using the free-online course given by awsomeness Adrian, creator of the . [PyImageSearch](https://www.pyimagesearch.com).

### No. 1 -  Face Recognition
Perform fast, accurate face detection with OpenCV using a pre-trained deep learning face detector model shipped with the library.

- For video:

<code>python detect_faces_video.py -p deploy.prototxt.txt -m res10_300x300_ssd_iter_140000.caffemodel</code>

- For images:

<code>python face_detection_w_OpenCV.py -i sample_0.jpg -p deploy.prototxt.txt -m res10_300x300_ssd_iter_140000.caffemodel</code>

### No. 2 -  OpenCV Guide
Learning OpenCV isn’t as hard as it used to be. And in fact, I’ll go as far as to say studying OpenCV has become significantly easier.

- Basic Image Manipulation:

<code>python opencv_01.py -i jp.png</code>

- Basic Color Image Manipulation:

<code>python opencv_02.py -i tetris_blocks.png</code>


### No. 3 -  Scan a Document
Building a document scanner with OpenCV can be accomplished in just three simple steps:
1. Detect edges.
2. Use the edges in the image to find the contour (outline) representing the piece of paper being scanned.
3. Apply a perspective transform to obtain the top-down view of the document.

- Try it:

<code>python scanner.py -i final-bill.jpg</code>

### No. 4 -  Multiple Choice Exam Scanner
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

- Try it:
Change the correct answers in the exam on **Line 17**, to see how it works.

<code>python test_grader.py -i omr_test_01.png</code>

### No. 5 -  Object Tracking by Segmentation
The goal here is:
1. Detect the presence of a colored ball using computer vision techniques.
2. Track the ball as it moves around in the video frames, drawing its previous positions as it moves.

- Try it
Change color range on **Lines 19 and 20**, to see how it works.
<code>python object_tracking.py</code>
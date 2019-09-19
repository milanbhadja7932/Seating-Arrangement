# Seating-Arrangement
# YOLOv3-Object-Detection-with-OpenCV

Finding Available Seat In Library is Most Difficult task for Reader. SML System increasingly looked upon as the solution
to this problem and saved Time and Effort for Reader.
This project implements an image and video object detection classifier using pretrained yolov3 models. 
The yolov3 models are taken from the official yolov3 paper which was released in 2018. The yolov3 implementation is from [darknet](https://github.com/pjreddie/darknet). Also, this project implements an option to perform classification real-time using the webcam.

● SML System is Developed for the library to simplify the Seating With CCTV, Display Of Library You Show the Available
Seat Live time, SML used DL With IOU to Find Available Seat.
## How to use?

# Breaking Down The Problem
1) Clone the repository

When we have a complicated problem that we want to solve with machine learning, the first step is to break down the problem into a sequence for simple tasks. Then, using our breakdown as a guide, we can pull different tools from our machine learning toolbox to solve each of the smaller tasks. By chaining together several small solutions into a pipeline, we’ll have a system that can do something complicated.
```
git clone https://github.com/iArunava/YOLOv3-Object-Detection-with-OpenCV.git
```

2) Move to the directory
```
cd YOLOv3-Object-Detection-with-OpenCV
```

--> Input:Webcamera for Video  -->  Detect Chair or Table --> Detect Human --> Compute Iou--> Show Available Space
3) To infer on an image that is stored on your local machine
```
python3 yolo.py --image-path='/path/to/image/'
```
4) To infer on a video that is stored on your local machine
```
python3 yolo.py --video-path='/path/to/video/'
```
5) To infer real-time on webcam
```
python3 yolo.py
```

# Detect the table in restaurant
Note: This works considering you have the `weights` and `config` files at the yolov3-coco directory.
<br/>
If the files are located somewhere else then mention the path while calling the `yolov3.py`. For more details
```
yolo.py --help
```

 Detecting chairs in a frame of video is a textbook object detection problem. There are lots of machine learning approaches we could use to detect an object in an image. Here are some of the most common object detection algorithms, in order from “old school” to “new school”:
## Inference on images

<strong>1-->Hog(Histogram of Oriented Gradients)</br>   2--> CNN (Convolutional Neural Network)</br>  3--> YOLO</br> </strong> 

![yolo_img_infer_1](https://user-images.githubusercontent.com/26242097/48849319-15d21180-edcc-11e8-892f-7d894be8d1a6.png)
![yolo_img_infer_2](https://user-images.githubusercontent.com/26242097/48850723-41a2c680-edcf-11e8-8940-aec302cd8aa3.png)
![yolo_infer_3](https://user-images.githubusercontent.com/26242097/48850729-449db700-edcf-11e8-853d-9f3eca6233c9.png)
![yolo_img_infer_4](https://user-images.githubusercontent.com/26242097/48850735-47001100-edcf-11e8-80d6-b474e54fd7af.png)

<p align="center">
  <img src="https://github.com/milanbhadja7932/Seating-Arrangement/blob/master/Screenshot%20(17).png" width="350" alt="accessibility text">
</p>
## Inference on Video

# Detecting Empty Table Spaces
[![yolov3-video](https://user-images.githubusercontent.com/26242097/48851021-0785f480-edd0-11e8-8ce4-cdfb78e8a849.png)](https://www.youtube.com/watch?v=AzmCYs5fAn0)
<small> Click on the image to Play the video on YouTube </small>

We know the pixel location of each chair in our image. And by looking at multiple frames of video in succession, we can easily work out which chair haven’t moved and assume those areas are parking spaces. But how do we detect when a human leaves a chair?
## Inference in Real-time

The problem is that the bounding boxes of the chair in our image partially overlap:
[![yolov3-video](https://user-images.githubusercontent.com/26242097/48862668-0ca56c80-eded-11e8-9482-31d795105983.png)](https://youtu.be/QaxEtpRwmtI)
<small> Click on the image to Play the video on YouTube </small>

So if we assume that each of those bounding boxes represents a  Chair, it’s possible that the box can be partially occupied by a Human even when the space is empty. We need a way to measure how much two objects overlap so we can check for “mostly empty” boxes.
## References

The measure we will use is called Intersection Over Union or IoU. IoU calculated by finding the amount of pixels where two objects overlap and dividing it by the amount of pixels covered by both objects, like this:
<p align="center">
  <img src="https://github.com/milanbhadja7932/Seating-Arrangement/blob/master/iou.png" width="350" alt="accessibility text">
</p>

Green Boxes Indicate the chair is empty and red Boxes Indicate the chair is Not Available for Seating.
<p align="center">
  <img src="https://github.com/milanbhadja7932/Seating-Arrangement/blob/master/Screenshot%20(32).png" width="350" alt="accessibility text">
</p>

# OUTPUT

  ![Alt Text](https://github.com/milanbhadja7932/Seating-Arrangement/blob/master/gif%20for%20video.gif)

# CONCEPTS LIBRARY AND USER INTERFACE LIST USED IN PROJECT


<strong>CONCEPTS</br></strong>
   <strong>MACHINE LEARNING</br></strong>
        --> GENERATE CHARTS</br>
        --> USER GRAPH</br>
        --> ADMIN VIEW </br>
        --> ETC</br>
   <strong>DEEP LEARNING</br></strong>
        --> OBJECT DETECTION</br>
        --> INTERSECTION OVER UNION</br>
        --> SPACE DETECTION</br>
        --> ETC</br>
<strong>LIBRARY</br></strong>
    --> NUMPY</br>
    --> OPENCV</br>
    --> YOLO</br>
    --> FlASK</br>
    --> ADMIN LTE</br>
    --> FLASK_SOCKETIO</br>
    --> MATPLOTLIB</br>
    --> SEABORN</br>
    --> OS</br>

<strong>USER INTERFACE</br></strong>

  <strong>USER SIDE</br></strong>
    --> SIGNUP</br>
    --> LOGIN</br>
    --> HOME PAGE</br>
    --> MONITOR</br>
    --> ENQUIRY</br>
    --> FEED BACK</br>
    --> LOGOUT</br>
 <strong>ADMIN SIDE</br></strong>
    --> DASH BOARD</br>
    --> ENQUIRY-FORM</br>
    --> FEED BACK -FORM</br>
    --> USER CONTACT</br>
    --> CHARTS OF USER</br>
    --> LOGOUT</br>


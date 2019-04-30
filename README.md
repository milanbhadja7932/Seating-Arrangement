# Seating-Arrangement

Finding Available Seat In Library is Most Difficult task for Reader. SML System increasingly looked upon as the solution
to this problem and saved Time and Effort for Reader.

● SML System is Developed for the library to simplify the Seating With CCTV, Display Of Library You Show the Available
Seat Live time, SML used DL With IOU to Find Available Seat.

# Breaking Down The Problem

When we have a complicated problem that we want to solve with machine learning, the first step is to break down the problem into a sequence for simple tasks. Then, using our breakdown as a guide, we can pull different tools from our machine learning toolbox to solve each of the smaller tasks. By chaining together several small solutions into a pipeline, we’ll have a system that can do something complicated.


--> Input:Webcamera for Video  -->  Detect Chair or Table --> Detect Human --> Compute Iou--> Show Available Space

# Detect the table in restaurant

 Detecting chairs in a frame of video is a textbook object detection problem. There are lots of machine learning approaches we could use to detect an object in an image. Here are some of the most common object detection algorithms, in order from “old school” to “new school”:

<strong>1-->Hog(Histogram of Oriented Gradients)</br>   2--> CNN (Convolutional Neural Network)</br>  3--> YOLO</br> </strong> 


<p align="center">
  <img src="https://github.com/milanbhadja7932/Seating-Arrangement/blob/master/Screenshot%20(17).png" width="350" alt="accessibility text">
</p>

# Detecting Empty Table Spaces

We know the pixel location of each chair in our image. And by looking at multiple frames of video in succession, we can easily work out which chair haven’t moved and assume those areas are parking spaces. But how do we detect when a human leaves a chair?

The problem is that the bounding boxes of the chair in our image partially overlap:

So if we assume that each of those bounding boxes represents a  Chair, it’s possible that the box can be partially occupied by a Human even when the space is empty. We need a way to measure how much two objects overlap so we can check for “mostly empty” boxes.

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
   



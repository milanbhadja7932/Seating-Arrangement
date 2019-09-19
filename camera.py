import cv2
import yolo

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        #self.video = cv2.VideoCapture(0)

        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        #self.video = cv2.VideoCapture('./opo.mp4')
        self.video = cv2.VideoCapture("./hw.mp4")
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self,bb1):
        #success, frame = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        
        #count=0
        #bb1=None
        #while True:
            
        _, frame = self.video.read()
        fr,bb1=yolo.yolo(frame,bb1)
        print("count : ",bb1)
        #count=count+1
            #if (count%1==0):
            #    bb1=y
            #count=count+1

            #if cv2.waitKey(1) & 0xFF == ord('q'):
             #   break
        #if (count%5==0):
        #    y=yoloc.yolo(frame,count,bb1)
        
            
        

        
        ret, jpeg = cv2.imencode('.jpg', fr)
        return jpeg.tobytes(),bb1



class VideoCamera2(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        #self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        #self.video = cv2.VideoCapture('./opo.mp4')
        self.video = cv2.VideoCapture("./opo.mp4")
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self,bb1):
        #success, frame = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        
        #count=0
        #bb1=None
        #while True:
            
        _, frame = self.video.read()
        fr,bb1=yolo.yolo(frame,bb1)
        print("count : ",bb1)
        #count=count+1
            #if (count%1==0):
            #    bb1=y
            #count=count+1

            #if cv2.waitKey(1) & 0xFF == ord('q'):
             #   break
        #if (count%5==0):
        #    y=yoloc.yolo(frame,count,bb1)
        
            
        

        
        ret, jpeg = cv2.imencode('.jpg', fr)
        return jpeg.tobytes(),bb1

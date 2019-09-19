import numpy as np
import argparse
import cv2 as cv
import subprocess
import time
import os
from yolo_utils import infer_image, show_image

FLAGS = []

if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	parser.add_argument('-m', '--model-path',
		type=str,
		default='./yolov3-coco/',
		help='The directory where the model weights and \
			  configuration files are.')

	parser.add_argument('-w', '--weights',
		type=str,
		default='./yolov3-coco/yolov3.weights',
		help='Path to the file which contains the weights \
			 	for YOLOv3.')

	parser.add_argument('-cfg', '--config',
		type=str,
		default='./yolov3-coco/yolov3.cfg',
		help='Path to the configuration file for the YOLOv3 model.')

	parser.add_argument('-i', '--image-path',
		type=str,
		help='The path to the image file')

	parser.add_argument('-v', '--video-path',
		type=str,
		help='The path to the video file')


	parser.add_argument('-vo', '--video-output-path',
		type=str,
        default='./output.avi',
		help='The path of the output video file')

	parser.add_argument('-l', '--labels',
		type=str,
		default='./yolov3-coco/coco-labels',
		help='Path to the file having the \
					labels in a new-line seperated way.')

	parser.add_argument('-c', '--confidence',
		type=float,
		default=0.5,
		help='The model will reject boundaries which has a \
				probabiity less than the confidence value. \
				default: 0.5')

	parser.add_argument('-th', '--threshold',
		type=float,
		default=0.3,
		help='The threshold to use when applying the \
				Non-Max Suppresion')

	parser.add_argument('--download-model',
		type=bool,
		default=False,
		help='Set to True, if the model weights and configurations \
				are not present on your local machine.')

	parser.add_argument('-t', '--show-time',
		type=bool,
		default=False,
		help='Show the time taken to infer each image.')

	FLAGS, unparsed = parser.parse_known_args()

	# Download the YOLOv3 models if needed
	if FLAGS.download_model:
		subprocess.call(['./yolov3-coco/get_model.sh'])

	# Get the labels
	labels = open(FLAGS.labels).read().strip().split('\n')
	print("label",(labels))

	# Intializing colors to represent each label uniquely
	colors = np.random.randint(0, 255, size=(len(labels), 3), dtype='uint8')

	# Load the weights and configutation to form the pretrained YOLOv3 model
	net = cv.dnn.readNetFromDarknet(FLAGS.config, FLAGS.weights)
	#net= model.load_weights(weightsfile)

	# Get the output layer names of the model
	layer_names = net.getLayerNames()
	layer_names = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        
	# If both image and video files are given then raise error
	if FLAGS.image_path is None and FLAGS.video_path is None:
	    print ('Neither path to an image or path to video provided')
	    print ('Starting Inference on Webcam')

	# Do inference with given image
	if FLAGS.image_path:
		# Read the image
		try:
			img = cv.imread(FLAGS.image_path)
			height, width = img.shape[:2]
		except:
			raise 'Image cannot be loaded!\n\
                               Please check the path provided!'

		finally:
			img = infer_image(net, layer_names, height, width, img, colors, labels, FLAGS)
			show_image(img)

	elif FLAGS.video_path:
		# Read the video
		try:
			vid = cv.VideoCapture(FLAGS.video_path)
			height, width = None, None
			writer = None
		except:
			raise 'Video cannot be loaded!\n\
                               Please check the path provided!'

		finally:
			while True:
				grabbed, frame = vid.read()

			    # Checking if the complete video is read
				if not grabbed:
					break

				if width is None or height is None:
					height, width = frame.shape[:2]

				frame, _, _, _, _ = infer_image(net, layer_names, height, width, frame, colors, labels, FLAGS)



				def make_video(self, images, outimg=None, fps=2, size=None, is_color=True, format="XVID", outvid='image_video.avi'):
                                

				



                                        from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
                                        fourcc = VideoWriter_fourcc(*format)
                                        vid = None
                                        for image in images:
                                            if not os.path.exists(image):
                                                raise FileNotFoundError(image)
                                                img = imread(image)
                                            if vid is None:
                                                if size is None:
                                                    size = img.shape[1], img.shape[0]
                                                vid = VideoWriter(outvid, fourcc, float(fps), size, is_color)
                                            if size[0] != img.shape[1] and size[1] != img.shape[0]:
                                                img = resize(img, size)
                                            vid.write(img)
                                        vid.release()
                                        return vid
                        #mak=make_video(self,frame)
                        

                                

                        
                                
                                



                        







				

				#if writer is None:
					# Initialize the video writer
				#	fourcc = cv.VideoWriter_fourcc(*"XVID")
				#	writer = cv.VideoWriter(FLAGS.video_output_path, fourcc, 30, 
				#		            (frame.shape[1], frame.shape[0]), True)

                                #writer.write(frame)
			#writer.release()
			#vid.release()
				#mak=make_video(frame)
						            
				

				


                                
                                #print ("[INFO] Cleaning up...")
                                
                                
				
				

                                
                                
                                


	else:

                def compute_iou(box, boxes, box_area, boxes_area):
                    """Calculates IoU of the given box with the array of the given boxes.
                    box: 1D vector [y1, x1, y2, x2]
                    boxes: [boxes_count, (y1, x1, y2, x2)]
                    box_area: float. the area of 'box'
                    boxes_area: array of length boxes_count.

                    Note: the areas are passed in rather than calculated here for
                    efficiency. Calculate once in the caller to avoid duplicate work.
                    """
                    # Calculate intersection areas
                    y1 = np.maximum(box[0], boxes[:, 0])
                    y2 = np.minimum(box[2], boxes[:, 2])
                    x1 = np.maximum(box[1], boxes[:, 1])
                    x2 = np.minimum(box[3], boxes[:, 3])
                    intersection = np.maximum(abs(x2 - x1), 0) * np.maximum(abs(y2 - y1), 0)
                    union = box_area + boxes_area[:] - intersection[:]
                    iou = intersection / union
                    print("iou",iou)
                    return iou

                

                def compute_overlaps(boxes1, boxes2):
                    """Computes IoU overlaps between two sets of boxes.
                    boxes1, boxes2: [N, (y1, x1, y2, x2)].

                    For better performance, pass the largest set first and the smaller second.
                    """
                    # Areas of anchors and GT boxes
                    ara1=1
                    ara2=1
                    try:
                            area1 = (abs(boxes1)[:, 2] - abs(boxes1)[:, 0]) * abs((boxes1)[:, 3] - abs(boxes1)[:, 1])
                            ara1=area1
                    except:
                            area1=ara1

                    try:
                            
                            area2 = (abs(boxes2)[:, 2] - abs(boxes2)[:, 0]) * (abs(boxes2)[:, 3] - abs(boxes2)[:, 1])
                            ara2=area2
                    except:
                            area2=ara2

                    # Compute overlaps to generate matrix [boxes1 count, boxes2 count]
                    # Each cell contains the IoU value.
                    overlaps = np.zeros((boxes1.shape[0], boxes2.shape[0]))
                    for i in range(overlaps.shape[1]):
                        box2 = boxes2[i]
                        #overlaps=1
                        overlaps[:, i] = compute_iou(box2, boxes1, area2[i], area1)
                        return overlaps


                
                def get_car_boxes(boxes,classids):
                        car_boxes = []
                        for i,box in enumerate(boxes):
                                #if classids[i] in [56,57,58]:
                                        car_boxes.append(box)
                                        #print("car_boxes",car_boxes)
                                        
                                
                                

                        return np.array(car_boxes)
                def get_car_boxes1(boxes,classids):
                        car_boxes = []
                        for i,box in enumerate(boxes):
                                #if classids[i] in [0]:
                                        car_boxes.append(box)
                                        #print("car_boxes",car_boxes)
                                        
                                
                                

                        return np.array(car_boxes)
                #parked_box=None

                vid = cv.VideoCapture(r"./b.mp4")
                count = 0


                while True:
                        _, frame = vid.read()
                        height, width = frame.shape[:2]

                        rgb_image = frame[:, :, ::-1]

                        #results = model.detect([rgb_image], verbose=0)
                        print("count",count)
                        
                        if count == 0:
                               
                                                
                                                frame, boxes, confidences, classids, idxs = infer_image(net, layer_names, \
                                                        		height, width, frame, colors, labels, FLAGS)
                                        
                                
                                                bb1=get_car_boxes(boxes,classids)
                                                #print("arra",bb1)
                                                count += 1
                        else:

                                
                                                frame, boxes, confidences, classids, idxs = infer_image(net, layer_names, \
		    						height, width, frame, colors, labels, FLAGS)#, boxes, confidences, classids, idxs, infer=False)
                                                count = (count + 1)
                                                print("boxes",boxes)
                                                bb2=get_car_boxes1(boxes,classids)
                                                print("arra2",bb2)
                                                #print("arra",bb1)

                                                overlaps = compute_overlaps(bb1, bb2)
                                                #print("iou",iou) 
                                                #print("overlaps",overlaps)

                                                for parking_area, overlap_areas in zip(bb1, overlaps):
                                                        max_IoU_overlap = np.max(overlap_areas)
                                                        print("max",max_IoU_overlap)

                                                        x,y,w,h = parking_area
                                                        #print("xyyx",x,y,w,h)

                                                        if (max_IoU_overlap) < 0.30:
                                                                for c in confidences:
                                                                        if c>0.6:
                                                                                cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
                                                                        
                                                                

                                                        else:
                                                                for c in confidences:
                                                                        if c>0.6:
                                                                                cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)
                                                                                
                                                                
                                                        

                                                        


                                                
                        cv.imshow('webcam', frame)
                        if cv.waitKey(1) & 0xFF == ord('q'):
                                break
                vid.release()
                cv.destroyAllWindows()
                                
                                

		
		

		
                
		

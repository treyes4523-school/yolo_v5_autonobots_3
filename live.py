from threading import Thread
import cv2
import detect
import numpy as np
class WebcamVideoStream:
    def __init__(self, src=0):
	# initialize the video camera stream and read the first frame
	# from the stream
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False

    def start(self):
	# start the thread to read frames from the video stream
        Thread(target=self.update, args=()).start()
        return self
    def update(self):
	# keep looping infinitely until the thread is stopped
        while True:
		# if the thread indicator variable is set, stop the thread
            if self.stopped:
                return
		# otherwise, read the next frame from the stream
            (self.grabbed, self.temp) = self.stream.read()
            self.frame = cv2.resize(self.temp,(512,512))
    def read(self):
	# return the frame most recently read
        return self.frame
    def stop(self):
	# indicate that the thread should be stopped
        self.stopped = True	
vs = WebcamVideoStream().start()
stop = False
while stop is False:
    frame = vs.read()
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if cv2.waitKey(33) == ord('q'):
        stop = True
    
cv2.destroyAllWindows()

import cv2
import mediapipe as mp
import time
mpDraw=mp.solutions.drawing_utils
#used to connect the detected landmarks of a person present in the image
mpPose=mp.solutions.pose
pose=mpPose.Pose(static_image_mode=True,upper_body_only=False,smooth_landmarks=True,min_detection_confidence=0.5,min_tracking_confidence=0.5)
#if static_image_mode is set to True then If set to true, person detection runs every input image, ideal for processing a batch of
#static,possibly unrelated, images. Default to false. 

def plot_landmarks(frame,draw=False):
    """
    Function that returns a list of 33 landmarks detected on the person present in the frame.
    Arguments:
    frame: The image on which landmarks should be detected.
    draw: if set to True detected landmarks are joined using lines and if set to False only landmarks are plotted. False by default
    """
    landMarks=[]
    #array to store all the 33 landmarks of the detected person
    results=pose.process(frame)
    if results.pose_landmarks:
        if draw:
            mpDraw.draw_landmarks(frame,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
            #The above statement plots the landmarks as well as connects them using lines.
        else:
            mpDraw.draw_landmarks(frame,results.pose_landmarks)
            #The above statement just plots the landmarks
        for id,land_mark in enumerate(results.pose_landmarks.landmark):
        #numbering every landmark
            height,width,filters=frame.shape
            x,y=int(land_mark.x*width),int(land_mark.y*height)
            #Finding actual position of  landmark
            landMarks.append([id,x,y])
            #Appending all the landmarks to the list.
    return landMarks
    #returning the array that contains all the 33 landmarks

def track_landmarks(toBeTracked,landmarks,frame):
    """
    Function used to track particular landmark among the 33 landmarks.
    Arguments:
    toBeTracked: list of id's of landmarks to be tracked specificly.
    landmarks: list of all the 33 landmarks
    frame: The image on which the specific landmarks should be overlayed.
    """
    for i in landmarks:
        #comparing whether a particular landmark is to be tracked or not
        if i[0] in toBeTracked:
            cv2.circle(frame,(i[1],i[2]),10,(255,0,0),cv2.FILLED)
            #overlaying a bigger dot on the specific points to be tracked with blue color.
    return frame
    
                
prev_time=0
#if the argumnent of cv2.VidoeCaputer() is provided as 0 then your webcam turn on. If location of any video file is provided as argument
#then the video will be considered as input.
video=cv2.VideoCapture(r'C:\Users\Naga Sai\Downloads\temp.mp4')
width=int(video.get(3))
height=int(video.get(4))
processed_video = cv2.VideoWriter('processedVideo2.mp4', cv2.VideoWriter_fourcc('F','M','P','4'), 12.0, (width,height))
while True:
    ret,frame=video.read()
    if not(ret):
        break
    #The mediapipe model takes color image as input. Conveting the BGR image that was read by OpenCv into RGB image.
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    #Finding landmarks of a person in the frame.
    landmarks=plot_landmarks(frame,True)
    #Landmarks to be tracked should be passed in the form of list as the first argument to the track_landmarks() function.
    frame=track_landmarks([11,12],landmarks,frame)
    #calculating frames per second value
    curr_time=time.time()
    fps=int(1/(curr_time-prev_time))
    prev_time=curr_time
    #Displaying frames per second value on screen
    cv2.putText(frame,str(fps),(10,40),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)
    #Displaying the processed frame.
    cv2.imshow('PoseDetection',frame)
    processed_video.write(frame)
    if cv2.waitKey(1)==27:
        break
processed_video.release()
video.release()
cv2.destroyAllWindows()
    

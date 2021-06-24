# HumanPoseDetection
Tracking various parts of the body is the basic stepping stone for developing any kind of advanced computer vision Project. In this project I have developed a program using which one can track 33 different landmarks of a person. </br>
The id values of the landmarks that are being tracked are provided in the below image
![pose_tracking_full_body_landmarks](https://user-images.githubusercontent.com/40739974/123245964-f0b55a80-d502-11eb-89a6-a298515d987b.png) </br>
### **The code in the repository detects the landmarks either from the webcam or from a video and creates and processed video file in the same directory.** </br>
1. The code detects all the 33 landmarks and you can even specifically track only the required landmarks using their id values as shown in the above figure.
2. The only modification you need to change is the argument of the function cv2.videoCaputure() in the line number 56. If 0 is passed as an argument then the input of the program    is taken for the live cam and if the location of any video file is provided as input then the frames of the image will be taken as input.
3.The entire code consists of two functions, the task that is done by each function is clearly provided as a docstring for that function.
4. Play with the arguments of functions as you like.
5. The output of the above code for tracking left shoulder and right shoulder of the person will be as follows.
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/lzi49Y1RvQE/0.jpg)](http://www.youtube.com/watch?v=lzi49Y1RvQE)



##################################### Libraries Needed #####################################
import cv2
import os

##################################### Class generating frames #####################################
class FrameGenerator:

    def __init__(self, input_video, frame):
        self.input_video = input_video
        self.frame = frame

    ##################################### Function to save the required FRAME #####################################
    def get_frame(self):

        #________________ Load Video with OpenCV ________________#
        cap = cv2.VideoCapture(self.input_video)
        #________________ Counter Variable for counting Frame ________________#
        currentFrame = 1

        #________________ Loop to parse through Video Frames ________________#
        while(currentFrame <= self.frame):

            #________________ Read and store the Frame ________________#
            ret, frame = cap.read()

            #________________ Check if video ends or not ________________#
            if not ret:
                print('Framing complete!!!')
                break

            #________________ Increment the counter ________________#
            currentFrame += 1

        #________________ Save the Frame as image ________________#
        name = "Frame_{FRAME_NUMBER}.jpeg".format(FRAME_NUMBER=self.frame)
        cv2.imwrite(name, frame)


        #________________ Terminate or release capture when done ________________#
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':

    # input_video = input("Enter the video name: ")
    # frame = int(input("Enter the frame number: "))


    input_video = "./Video1.mp4"
    frame = 700

    Frame = FrameGenerator(input_video, frame)
    Frame.get_frame()
import cv2
import cvzone
def draw_x_y_plot(frame_name):

    ## drawing/writing x values
    for i in range(0, frame_name.shape[1], 100):
        cv2.circle(frame_name, (i, frame_name.shape[0] - 15), 10, (255, 0, 0), -1)
        cvzone.putTextRect(frame_name, f'{i}', (i, frame_name.shape[0] - 20), 1.4, 2, colorT=(0, 0, 0),
                           colorR=(255, 255, 255), offset=2)

    ## drawing/writing y values
    for i in range(0, frame_name.shape[0], 100):
        if i == 0 :
            cvzone.putTextRect(frame_name, f'{i}', (20, i+15), 1.4, 2, colorT=(0, 0, 0), colorR=(255, 255, 255), offset=2)
        cv2.circle(frame_name, (1, i), 10, (255, 0, 0), -1)
        cvzone.putTextRect(frame_name, f'{i}', (20, i), 1.4, 2, colorT=(0, 0, 0), colorR=(255, 255, 255), offset=2)

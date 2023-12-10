import cv2
import cvzone

from x_y_live_plot import draw_x_y_plot
cap = cv2.VideoCapture(0)

## optional to change frame size
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)

while True:
    sucess, img = cap.read()
    if not sucess:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    draw_x_y_plot(img)

    cv2.imshow('frame', img)

# Release the video capture object
cap.release()
cv2.destroyAllWindows()
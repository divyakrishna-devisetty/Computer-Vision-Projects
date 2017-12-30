import cv2

co_ordinates = []
status = False


# This function gets called whenever we click/release mouse left button
def crop(events, x, y, flags, params):
    # you declare as global when u want to modify module level params within function
    # and you want them to reflect for the entire program scope.
    global co_ordinates, status

    if events == cv2.EVENT_LBUTTONDOWN:  # that means you are selecting to crop
        status = True  # you started cropping procedure so status is set to true
        co_ordinates = [(x, y)]  # initial co-ordinates where we started cropping

    if events == cv2.EVENT_LBUTTONUP:
        status = False
        co_ordinates.append((x, y))  # appending the final co-ordinates

        # bound the region of interest with rectangle
        cv2.rectangle(image, co_ordinates[0], co_ordinates[1], (255, 0, 0), 3)
        cv2.imshow('crop', image)


image = cv2.imread('flower.jpg')
image_copy = image.copy()

# Name a window on which you want to perform call back events
cv2.namedWindow("crop")

# set call back function
cv2.setMouseCallback("crop", crop)

while True:
    cv2.imshow("crop", image)
    keypress = cv2.waitKey(1)

    if keypress == ord('r'):  # redoes selection presses r
        image = image_copy.copy()
    if keypress == ord('c'):  # confirms selection presses c
        break

# once you confirm selection co-ordinates will be initial n final

if len(co_ordinates) == 2:
    roi = image[co_ordinates[0][1]:co_ordinates[1][1], co_ordinates[0][0]:co_ordinates[1][0]]
    cv2.imshow('region_of_interest', roi)
    cv2.imwrite('cropped_image.jpg', roi)
    cv2.waitKey()

cv2.destroyAllWindows()




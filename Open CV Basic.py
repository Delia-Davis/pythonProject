import cv2
print(cv2.__version__)
# Read the input image
image = cv2.imread("friends.jpg")
# Access pixel values and modify them
x , y = image.shape[:2]
print("Height = {}, Width ={}".format(x,y))
pixel = image[100,100]
print(pixel)
# Resize Image


scale = 80
width = int(image.shape[1] * scale / 100)
height = int(image.shape[0] * scale / 100)
dim = (width, height)
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
print('Resized Dimensions : ', resized.shape)
cv2.imshow("Resized image", resized)
cv2.waitKey()
cv2.destroyAllWindows()

# read image as greyscale
image = cv2.imread("friends.jpg")
# get image height, width
(h, w) = image.shape[:2]
# calculate the center of the image
center = (w / 2, h / 2)

angle90 = 90
angle180 = 180
angle270 = 270

scale = 1.0

# Perform the counterclockwise rotation holding at the center
# 90 degrees
M = cv2.getRotationMatrix2D(center, angle90, scale)
rotated90 = cv2.warpAffine(image, M, (h, w))
cv2.imshow('Image rotated by 90 degrees', rotated90)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image

# Edge Detection
import cv2

image = cv2.imread("friends.jpg")
edges = cv2.Canny(image, 100, 200)

cv2.imshow("Edge Detected Image", edges)
cv2.imshow("Original Image", image)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()

#opencv image thresh hold

img  = cv2.imread(r'Gandhiji.jpg',1)
retval, threshold = cv2.threshold(img, 62, 255, cv2.THRESH_BINARY)
cv2.imshow("Original Image", img)
cv2.imshow("Threshold",threshold)
cv2.waitKey(0)
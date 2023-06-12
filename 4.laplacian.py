import cv2

img = cv2.imread('gambar/nicola.jpg', 0)

blur = cv2.GaussianBlur(img, (3, 3), 0)

laplacian = cv2.Laplacian(blur, cv2.CV_64F)
laplacian = laplacian / laplacian.max()

cv2.imshow('laplacian-gaussian', laplacian)
cv2.waitKey(0)


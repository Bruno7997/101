import cv2
import numpy as np

img = cv2.imread("./Imgss/solar-system.jpg")

cv2.putText(img, "SOL", (100,80),cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255))
cv2.putText(img, "MERCURIO", (120,240),cv2.FONT_HERSHEY_COMPLEX, 1/3, (255,255,255))
cv2.putText(img, "VENUS", (195,250),cv2.FONT_HERSHEY_COMPLEX, 1/3, (255,255,255))
cv2.putText(img, "TERRA", (295,260),cv2.FONT_HERSHEY_COMPLEX, 1/3, (255,255,255))
cv2.putText(img, "MARTE", (385,240),cv2.FONT_HERSHEY_COMPLEX, 1/3, (255,255,255))
cv2.putText(img, "JUPITER", (585,360),cv2.FONT_HERSHEY_COMPLEX, 1/3, (255,255,255))
cv2.putText(img, "SATURNO", (775,270),cv2.FONT_HERSHEY_COMPLEX, 1/3, (255,255,255))
cv2.putText(img, "URANO", (975,280),cv2.FONT_HERSHEY_COMPLEX, 1/3, (255,255,255))
cv2.putText(img, "NETUNO", (1125,275),cv2.FONT_HERSHEY_COMPLEX, 1/3, (255,255,255))

##cv2.imwrite("./Imgss/solar-system.jpg",img)
cv2.imshow("Imagem", img)
cv2.waitKey(0)
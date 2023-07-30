import cv2
import numpy as np
import os


path = "./Imgss/Img1/"
images=[]
for file in os.listdir(path):
 N, E = os.path.splitext(file)
 if E in [".gif", ".png", ".jpg", ".jfif"]:
  file_name=path+"/"+file
  print(file_name)
  images.append(file_name)
cont=len(images)
frame=cv2.imread(images[0])
height, width, channels = frame.shape
size=(width, height)
out = cv2.VideoWriter("project.avi",cv2.VideoWriter_fourcc(*"DIVX"), 0.8, size)
for i in range(0, cont-1):
  frame = cv2.imread(images[i])
  out.write(frame)
out.release()
print("concluido")
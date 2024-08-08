import os
import cv2

path = "/Users/ompatel/Documents/Python/PRO-C105-Project-Images-main/Images"
Images = []

for file in os.listdir(path):
    name, extension = os.path.splitext(file)
    if extension in ['.gif', '.png', '.jpg', '.jpeg', 'jfif']:
        file_name = path + '/' + file
        print(file_name)
        Images.append(file_name)
        count = len(Images)
        frame = cv2.imread(Images[0])
        height, width, layers = frame.shape
        size = (width, height)
        print(size)
        out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

        for i in range(0,count-1):
            img = cv2.imread(Images[i])
            out.write(img)
            cv2.imshow('video', img)
            print("Done")



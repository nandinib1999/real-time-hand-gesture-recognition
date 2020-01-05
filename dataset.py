# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 19:17:55 2019

@author: nandini
"""
import cv2
import os

def create_dir(opath):
    if not os.path.exists(opath):
        os.mkdir(opath)
    return opath


path = './dataset/'
create_dir(path)

cap = cv2.VideoCapture(0)
gesture_captured = {"up":0, "down":0}
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.rectangle(frame, (100,100), (300, 300), (0,0,255), 2)
    img = frame[100:300, 100:300]
    cv2.imshow("image", frame)
    key = cv2.waitKey(1)
    if key == ord('u'):
        op_path = create_dir(os.path.join(path, 'up'))
        if len(os.listdir(op_path)) != 0:
            last_file = max([int(x.split('_')[1].split('.')[0]) for x in os.listdir(op_path)])
            gesture_captured['up'] = last_file + 1
        else:
            gesture_captured['up'] = 1
            
        file_name = 'up_'+str(gesture_captured['up'])+'.jpg'
        cv2.imwrite(os.path.join(op_path, file_name), img)
        print(file_name+' saved successfully..')
    elif key == ord('d'):
        op_path = create_dir(os.path.join(path, 'down'))
        if len(os.listdir(op_path)) != 0:
            last_file = max([int(x.split('_')[1].split('.')[0]) for x in os.listdir(op_path)])
            gesture_captured['down'] = last_file + 1
        else:
            gesture_captured['down'] = 1
            
        file_name = 'down_'+str(gesture_captured['down'])+'.jpg'
        cv2.imwrite(os.path.join(op_path, file_name), img)
        print(file_name+' saved successfully..')
    elif key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
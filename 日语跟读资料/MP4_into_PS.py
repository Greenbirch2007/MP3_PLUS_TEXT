# 使用opencv2包实现,这里的视频帧计数间隔是真实时间…不是数字越大,越能截到时间较长的帧

import cv2
import os


l_path = os.getcwd()


# 使用opencv按一定间隔截取视频帧，并保存为图片

vc = cv2.VideoCapture('{0}/1.mp4'.format(l_path))  # 读取视频文件
c = 0
print("------------")
if vc.isOpened():  # 判断是否正常打开
    print("yes")
    rval, frame = vc.read()
else:
    rval = False
    print("false")
# 大约2秒钟截图一次
timeF = 40000000  # 视频帧计数间隔频率

while rval:  # 循环读取视频帧
    rval,frame = vc.read()
    print(c,timeF,c%timeF)
    if (c % timeF == 0):# 每隔timeF帧进行存储操作
        print("write...")
        cv2.imwrite('{0}/'.format(l_path) + str(c) +"--2"+ '.jpg', frame)  # 存储为图像
        print("success!")
    c = c + 100000
cv2.waitKey(1)
vc.release()
print("==================================")
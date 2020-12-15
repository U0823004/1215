import cv2
import numpy as np
import argparse

#顯示模組
def display(windowsName,img):
    cv2.namedWindow(windowsName, cv2.WINDOW_NORMAL) #使視窗可調整，並命名
    size = img.shape# 影像尺寸最佳化
    h = size[0]
    w = size[1]
    while(True):
        if w>800 or h>800:
            w = int(w/2)
            h = int(h/2)
        else:
            break
    cv2.resizeWindow(windowsName,w,h)
    cv2.imshow(windowsName,img)
    cv2.waitKey(0)

ap = argparse.ArgumentParser()
ap.add_argument('-i',required= True,help='Path to the image')
args = vars(ap.parse_args())
image = cv2.imread(args['i'],flags=0)
imagename = args['i']
display(imagename,image)
lap = cv2.Laplacian(image, cv2.CV_64F)#將函數轉為浮點格式CV_64F
lap = np.uint8(np.absolute(lap))#取得絕對值後轉為8bit資訊
lap = abs(255-lap)
display('LAP',lap)

cv2.imwrite('.\\edge_lenna.png',lap)

'''
使用Laplacian找出邊緣。注意使用此函數除了傳入灰階影像之外，亦須指定輸出的影像浮點格式CV_64F
為什麼是使用64bits而非灰階的8bits呢？因為Laplacian過程需進行black-to-white及white-to-black兩種轉換
在微分的梯度計算（gradient）中black-to-white屬於正向的運算而white-to-black則是負向
灰階的8bits格式僅能儲存0-255的正值，因此必須使用64bits。
注意在接下來須取其絕對值並轉為8bit的灰階資訊，這是一般在運行Laplacian運算時所建議的方法
網路上的說法是此方式可保留所有的邊緣資訊：先轉出為64bit，再取絕對值轉為8bit。
'''

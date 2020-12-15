# 1215上課內容

- 了解如何安裝`openCV`套件包與操作。
- 練習 `openCV`與影像處理運算。
- 抓取人臉位置與利用`opencv`。

## OpenCV 簡介
OpenCV的全稱是Open Source Computer Vision Library，是一個跨平台的電腦視覺庫。OpenCV是由英特爾公司發起並參與開發，以BSD授權條款授權發行，可以在商業和研究領域中免費使用。
<center> <img src="https://upload.wikimedia.org/wikipedia/commons/5/53/OpenCV_Logo_with_text.png"> 
</center>
<center>OpenCV的LOGO</center>
OpenCV的應用其實很廣，在許多的 #程式設計 上均有OpenCV的蹤跡，其中近年來以 #python 最為熱門因此本文也將使用python進行使用與探討。

在 #機器視覺 專案的開發中，OpenCV作為較大眾的開源庫，擁有了豐富的常用影象處理函式庫，採用C/C 語言編寫，可以執行在Linux/Windows/Mac等作業系統上，能夠快速的實現一些影象處理和識別的任務。此外，OpenCV還提供了Java、 [#python](%E4%BD%BF%E7%94%A8Python) 、 #cuda 等的使用介面、機器學習的基礎演算法呼叫，從而使得影象處理和影象分析變得更加易於上手，讓開發人員更多的精力花在演算法的設計上。
### 應用領域
- 人機互動
	- 人臉識別
	- 運動分析
- 影像處理
	- 邊緣偵測
	- 灰階處理
	- 濾波降噪
- 物體辨別
	- 動作識別
	- 汽車安全駕駛
	- 結構分析
實務上具有許多操作是混和使用，應用上也十分複雜。


##  安裝OpenCV
以下內容均利用`python`進行操作，主要可分為`pip`與[`conda`](conda用法)兩種，分別指令如下。
### pip 套件管理器
```shell
pip install opencv-python
```
這裡會自動下載[pypi](https://pypi.org/project/opencv-python/)的最新套件內容，這個函數是目前穩定的相關內容，已經驗證過的算式會放入這裡，如果想要使用最新的套件及開發中的套件包，可以安裝這下列版本。
```shell
pip install opencv-contrib-python
```
其詳細解說如[網站](https://pypi.org/project/opencv-contrib-python/)所述。

### conda 套件安裝管理
指令如下，會從[conda套件庫](https://anaconda.org/anaconda/opencv)下載目前的版本。
```shell
conda install opencv
```
其中，利用`pip`與`conda`下載的版本會略有落差，使用實際得特別注意版本差異。

## 匯入OpenCV
在python中，[匯入](python_import語句)OpenCV程式碼如下所示：
```py
import cv2 
```
由於python是物件導向的程式語言，因此操作上都是利用`cv2`這個做為開頭，進行OpenCV的一系列函數操作。

## 基本功能
### 讀取影像
```py
cv2.imread('path/image.png',flag)
```
其中`flag`可以用下列參數作為輸入
- cv2.IMREAD_COLOR(可用`1`代替)
	- 此為預設值，會載入影片的RGB數據，忽略透明度
- cv2.IMREAD_GRAYSCALE(可用`0`代替)
	- 直接將影像轉為灰階圖片
- cv2.IMREAD_UNCHANGED(可用`-1`代替)
	- 包含透明度在內的所有資訊均轉入數據

範例示範
```py
import cv2 
import numpy as np

A = np.array(cv2.imread('Lenna.jpg',cv2.IMREAD_COLOR))
B = np.array(cv2.imread('Lenna.jpg',cv2.IMREAD_GRAYSCALE))
C = np.array(cv2.imread('Lenna.jpg',cv2.IMREAD_UNCHANGED))

A_size = np.shape(A)
B_size = np.shape(B)
C_size = np.shape(C)

print(A_size)
print(B_size)
print(C_size)
```

得到結果如下
```shell
(316, 316, 3)
(316, 316)
(316, 316, 3)
```
這裡使用的圖片是大名鼎鼎的萊娜圖

<center> <img src="https://upload.wikimedia.org/wikipedia/zh/3/34/Lenna.jpg"> </center>

從上述的程式碼中可以發現，由於檔案的[副檔名](副檔名)是`jpg`的格式，因此本身就已經移除透明度的資料，也因此這裡用`cv2.IMREAD_COLOR`與`cv2.IMREAD_UNCHANGED`的結果，最終的陣列大小都是一樣**(316×316×3)** 的大小，而使用`cv2.IMREAD_GRAYSCALE`的陣列大小就僅有二維，這是因為取值僅取得明度的部分，也因此每一個像素僅只有一個強度值，故最後大小呈現二維的陣列。

值得一提的是利用OpenCV取得的陣列，一順序分別是`B` `G` `R`的資料，在陣列中分別表示`[:,:,0]` `[:,:,0]` `[:,:,2]` 的資料順序。

### 顯示影像
剛才利用OpenCV將影像匯入了程式內，轉換為陣列，現在顯示的功能將影像匯出
指令如下：
```py
cv2.imshow('Title',data)
```
其中`data`是放入陣列數據。
而這樣的程式碼，一般來說只會讓影像顯示一瞬間就結束程式，故要加入等待指令

```py
cv2.waitKey(0)
```
括號處可填入停留時間，以毫秒作為單位，若填入`0`則會等待使用者按下任意鍵後才進行關閉OpenCV的視窗。

將剛剛匯入的影像再利用`cv2.imshow`顯示後的範例：
```py
cv2.imshow('B',(A[:,:,0])) #取得影像藍色數據
cv2.imshow('G',(A[:,:,1])) #取得影像綠色數據
cv2.imshow('R',(A[:,:,2])) #取得影像紅色數據
cv2.imshow('all',(A[:,:,:])) #取得影像所有數據
cv2.imshow('gray',B) #取得影像數據
cv2.waitKey(0)
```

顯示結果如下：
![顯示結果](https://github.com/edwardhome/Notebook/blob/main/picture/imshow_test.jpg?raw=true)
#### 關閉視窗設定
當開啟多個視窗可利用下列指令來控制關閉的條件
```py
cv2.waitKey(0)
cv2.destroyAllWindows()
```
利用這組指令，當按下任意鍵後則會自動關閉所有視窗，若希望可以一時間按照順序關閉指定圖片可利用下列指令進行控制：
```py
cv2.waitKey(0)
cv2.destroyWindow('Title') #填入指定的視窗名稱
```

### 儲存影像
最後當我們對影像處理完成後，希望儲存一個新的影像檔案，可利用下列指令進行影像儲存的動作
```py
cv2.imwrite('path/name.jpg',var)
```
依序填入儲存位置，及陣列變數名稱，即可針對影像進行儲存
這裡利用將圖片改為負片後存儲下來：
```py
Anegative = np.array(abs(255-A))
cv2.imshow('negative',Anegative)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('negative.png',Anegative)
```
其結果如下：
<center><img src="https://github.com/edwardhome/Notebook/blob/main/opencv_test/negative.png?raw=true"></center>

## 

```
* Some pre-trained results are in the folder ./runs/train, Some of them are used for helmet testing, and 
some are used for helmet plus protective clothing testing.
* The version required for each package are already in the file requirements.txt
First, we have to create a virtual environment for python3.8, please execute the following operations on the command line:

```bash
conda create -n yolo5 python==3.8.5
conda activate yolo5
```

## pytorch installation (installation of gpu version and cpu version)



```cmd
conda install pytorch==1.8.0 torchvision torchaudio cudatoolkit=10.2

conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cpuonly 
```


![image-20210726172454406](https://vehicle4cm.oss-cn-beijing.aliyuncs.com/typoraimgs/image-20210726172454406.png)

### installation for pycocotools


```
pip install pycocotools-windows
```

### installation for other packages


```bash
pip install -r requirements.txt
pip install pyqt5
pip install labelme
```

### test


```bash
python detect.py --source data/images/bus.jpg --weights pretrained/yolov5s.pt
```


```bash
 python detect.py --source 0  # webcam
                            file.jpg  # image 
                            file.mp4  # video
                            path/  # directory
                            path/*.jpg  # glob
                            'https://youtu.be/NUsoVlDFqZg'  # YouTube video
                            'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```



## data processing

pip install labelimg  

### data labeling

### arrangement for files

```bash
YOLO_Mask
└─ score
       ├─ images
       │    ├─ test
       │    ├─ train
       │    └─ val
       └─ labels
              ├─ test
              ├─ train 
              ├─ val
```

### model training 

To create a model configuration file `mask_yolov5s.yaml` under models, and execute the following command:


```
python train.py --data mask_data.yaml --cfg mask_yolov5s.yaml --weights pretrained/yolov5s.pt --epoch 100 --batch-size 4 --device cpu
```

20 rounds of training has made the results accurate enough



## Evaluation of the model

Generally, we will come into contact with two indicators, namely recall rate and precision. The two indicators p and r are simply to judge the quality of the model from one angle, and they are both values between 0 and 1. Among them, close to 1 indicates that the performance of the model is better, and close to 0 indicates that the performance of the model is worse.

In order to comprehensively evaluate the performance of target detection, the mean average density map is generally used to further evaluate the quality of the model. By setting different confidence thresholds, we can get the p-value and r-value calculated by the model under different thresholds. In general, the p-value and r-value are negatively correlated, and they can be drawn as shown below. As shown in the curve, the area of the curve is called AP. Each target in the target detection model can calculate an AP value, and the mAP value of the model can be obtained by averaging all AP values. Taking this article as an example, we can calculate For the AP values of the two targets wearing a helmet and without a helmet, we average the AP values of the two groups to obtain the mAP value of the entire model. The closer the value is to 1, the better the performance of the model.




### Usage of the model


```bash
 # detection for the camera
 python detect.py  --weights runs/train/exp_yolov5s/weights/best.pt --source 0  # webcam
 # detection for the image
  python detect.py  --weights runs/train/exp_yolov5s/weights/best.pt --source file.jpg  # image 
 # detection for the video 
   python detect.py --weights runs/train/exp_yolov5s/weights/best.pt --source file.mp4  # video
                    
```
# Smoke and fire detection from CCTV video

This project was commissioned by a fire prevention and fighting service company in industrial environments. Considering that the detection of smoke and fire using gas sensors has a delay and the speed of fire growth is very high, it has become important to use CCTV images to detect and announce the fire before it spreads. The purpose of this project is to detect smoke and fire using CCTV cameras in the environment (which are also used for monitoring purposes) and to notify the alarm.
![Screenshot](https://github.com/MoeinHan/smoke-and-fire-detection/blob/main/1.png)

## Requirements

* python 3.10

## How to Install

```bash
git clone https://github.com/MoeinHan/smoke-and-fire-detection.git
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## How to Use

```bash
python runner.py 
```
### status plot and show detection you have to run runner.py in yolov5 folder
### show detection only please run detect.py in yolov5 folder

introduce options in detect.py:

* \--weights : model path or triton URL
* \--source : file/dir/URL/glob/screen/0(webcam)
* \--data : (optional) dataset.yaml path
* \--imgsz : inference size h,w
* \--conf-thres : confidence threshold
* \--iou-thres : NMS IoU threshold
* \--max-det : maximum detections per image
* \--device : cuda device, i.e. 0 or 0,1,2,3 or cpu
* \--view-img : show results
* \--save-txt : save results to *.txt
* \--save-csv : save results in CSV format
* \--save-conf : save confidences in --save-txt labels
* \--save-crop : save cropped prediction boxes
* \--nosave : do not save images/videos
* \--classes : filter by class: --classes 0, or --classes 0 2 3
* \--agnostic-nms : class-agnostic NMS
* \--augment : augmented inference
* \--visualize : visualize features
* \--update : update all models
* \--project : save results to project/name
* \--name : save results to project/name
* \--exist-ok : existing project/name ok, do not increment
* \--line-thickness : bounding box thickness (pixels)
* \--hide-labels : hide labels
* \--hide-conf : hide confidences
* \--half : use FP16 half-precision inference
* \--dnn : use OpenCV DNN for ONNX inference
* \--vid-stride : video frame-rate stride
* \--show-status-figure : line plot for showing status

## Support

Merge requests are welcome as a support for this project.
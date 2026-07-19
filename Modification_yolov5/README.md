
# <p align="center"> Interactive Image-Based Aphid Counting in Yellow Water Traps under Stirring Actions </p>



<p align="center">
  <img src="https://github.com/XuminGaoGithub/Interactive-Image-Based-Aphid-Counting-in-Yellow-Water-Traps-under-Stirring-Actions/blob/main/Modification_yolov5/Overview_overall_methodology.jpg" width="1000" height="1000"" />
</p>

<p align="center">
Overview of our proposed method
</p>
<br/>


## Overview
The current vision-based aphid counting methods in water traps suffer from undercounts caused by occlusions and low visibility arising from dense aggregation of insects and other objects. To address this problem, we propose a novel aphid counting method through interactive stirring actions. We use interactive stirring to alter the distribution of aphids in the yellow water trap and capture a sequence of images which are then used for aphid detection and counting through an optimized small object detection network based on Yolov5. We also propose a counting confidence evaluation system to evaluate the confidence of counting results. The final counting result is a weighted sum of the counting results from all sequence images based on the counting confidence. Experimental results show that our proposed aphid detection network significantly outperforms the original Yolov5, with improvements of 33.9% in AP@0.5 on the aphid test set. In addition, the aphid counting test results using our proposed counting confidence evaluation system show significant improvements over the static counting method, closely aligning with manual counting results. The datasets and project code are released at: https://github.com/XuminGaoGithub/Interactive-Image-Based-Aphid-Counting-in-Yellow-Water-Traps-under-Stirring-Actions.



## Prerequisites

This work is based on https://github.com/ultralytics/yolov5.

As space limitation and file size limitation, datasets are uplaoded to OneDrive. Please download datasets by the links which has already included in the relevent files named README.md.



## Installation and Run

**1. Install envs**   
Please refer https://github.com/XuminGaoGithub/Automatic_aphid_counting___2023/tree/main/Automatic_aphid_counting to set up Yolov5 envs      

**2. Training and test model**

 **2.1 Detection**

**Prepare dataset**    
Please refer https://github.com/XuminGaoGithub/Automatic_aphid_counting___2023/tree/main/Automatic_aphid_counting to prepare yolo format datasets (#./dataset/voc2054/, ./dataset/voc2055/).

**Train**

`python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2055.yaml --cfg models/yolov5s.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100` #Training Yolov5 model

`python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2054.yaml --cfg models/yolov5s-ODConv-CoT3.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100` #Training the improved Yolov5 model


**Test**

`python test.py --img 640 --data data/aphid_voc_2055.yaml --weights /home/xumin/Modification_yolov5/runs/train/voc2055_original_yolov5/weights/best.pt --device '0' --batch-size 1` #Test Yolov5 model

`python sahi_split_test_keep_src_256x256.py --data /home/xumin/yolov5/data/aphid_voc_2055.yaml --weights /home/newdrive/Phd/Modification_yolov5/runs/train/voc_2054_yolov5s_ODConv_CoT3/weights/best.pt --device '0' --batch-size 1 --sliced_width 640 --sliced_height 640 --overlapped_height_ratio 0.2 --overlapped_width_ratio 0.2` #Test the improved Yolov5 model


**2.2 Counting confidence assessment**

**Dataset**

9 sets of sequence images under interactive stirring actions, with each set containing 9 images. Seven of these sets were used to build the aphid counting confidence model, while the remaining 2 sets were used for testing.

Dataset link: 

https://universityoflincoln-my.sharepoint.com/:f:/g/personal/25766099_students_lincoln_ac_uk/IgAyMWwn2shvTYCxHb5qtFSoAXwMmIc1wTP4PhsFcFdIrXU?e=dniXgu


**Calculate CNGR for each of images in dataset**

python sahi_split_detect_keep_src_ConfusionMatrix_files_with_CountingConfidence.py --weights /home/newdrive/Phd/Modification_yolov5/runs/train/voc_2054_yolov5s_ODConv_CoT3/weights/best.pt --device 0 --save-txt --save-conf --sliced_height 640 --sliced_width 640 --overlapped_height_ratio 0.2 --overlapped_width_ratio 0.2 --xml /home/newdrive/Phd/Modification_yolov5/dataset/test_counting_model/labels/ --source /home/newdrive/Phd/Modification_yolov5/dataset/test_counting_model/src/ #get cnbr.txt (which is calculated and recorded the detection confidence of aphid bounding boxes, the predicted number of aphids, the image clarity,and ground truth of counting confidence for each of images)


**Multiple linear regression analysis**

cd /home/newdrive/Modification_yolov5/dataset/test_counting_model/CNBR

python sort_cnbr.py #get sort_cnbr.txt and split into sorted_CNBR_training.txt and sorted_CNBR_test.txt

python multiple_linear_analysis_training.py

python multiple_linear_analysis_test.py

python plot4.py # get the data from above and copy it into code, plot "Variations of the average values of C, N, G, and R over time T.



**The final counting result**

The final counting result is computed as a weighted sum of counting results from a complete counting sequence, where the counting result for each image N_i is weighted by a softmax probability derived from its corresponding counting confidence R_i.

cd R_probability

python cal_probability.py
   
## Citation
X. Gao, M. Stevens, G. Cielniak. Interactive Image-Based Aphid Counting in Yellow Water Traps under Stirring Actions. The 27th International Conference on Pattern Recognition VAIB Workshop (ICPR2024), Kolkata, India, 2024.

## Contact
If you have any issue, please contact us.



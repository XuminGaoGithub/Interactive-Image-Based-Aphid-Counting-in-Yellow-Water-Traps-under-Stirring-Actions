
# <p align="center"> Interactive Image-Based Aphid Counting in Yellow Water Traps under Stirring Actions </p>



<p align="center">
  <img src="https://github.com/XuminGaoGithub/Interactive-Image-Based-Aphid-Counting-in-Yellow-Water-Traps-under-Stirring-Actions/blob/main/Modification_yolov5/Overview_overall_methodology.jpg" width="1000" height="1000"" />
</p>

<p align="center">
Overview of our proposed method
</p>
<br/>


## Overview
The current vision-based aphid counting methods in water traps suffer from undercounts caused by occlusions and low visibility arising from dense aggregation of insects and other objects. To address this problem, we propose a novel aphid counting method through interactive stirring actions. We use interactive stirring to alter the distribution of aphids in the yellow water trap and capture a sequence of images which are then used for aphid detection and counting through an optimized small object detection network based on Yolov5. We also propose a counting confidence evaluation system to evaluate the confidence of count-ing results. The final counting result is a weighted sum of the counting results from all sequence images based on the counting confidence. Experimental results show that our proposed aphid detection network significantly outperforms the original Yolov5, with improvements of 33.9% in AP@0.5 on the aphid test set. In addition, the aphid counting test results using our proposed counting confidence evaluation system show significant improvements over the static counting method, closely aligning with manual counting results. The datasets and project code are released at: https://github.com/XuminGaoGithub/Interactive-Image-Based-Aphid-Counting-in-Yellow-Water-Traps-under-Stirring-Actions.



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


cd CSRNet-pytorch-master/

`python -m visdom.server` # Open visdom to watch the training curves

`python train.py train.json val.json 0 0` # Training

**Notice**

Please note that we have two datasets (aphid_dataset_1,aphid_dataset_2), before training, you need to configure some training files，for example:

if you train aphid_dataset_1,

(1) mofify 'CSRNet-pytorch-master/Shanghai/part_A_final_aphid_dataset_1' to 'CSRNet-pytorch-master/Shanghai/part_A_final'

(2) copy three json file from 'CSRNet-pytorch-master/aphid_dataset_1_json' to 'CSRNet-pytorch-master/'


if you train aphid_dataset_2,

(1) mofify 'CSRNet-pytorch-master/Shanghai/part_A_final_aphid_dataset_2' to 'CSRNet-pytorch-master/Shanghai/part_A_final'

(2) copy three json file from 'CSRNet-pytorch-master/aphid_dataset_2_json' to 'CSRNet-pytorch-master/'


**Test**

Please refer to '*4. Hybrid_network test*', you can use 'hybird_network_image.py' and 'hybird_network_test.py' to do test by setting the condition for the detection network to 'False' in the codes, in this case, only density map estimation network works. Also, please you need to modify the loaded model name in the codes which you want use as we have two density map estimation network model (for aphid_dataset_1, aphid_dataset_2 respectively).


**4. Hybrid_network test**
* The hybrid_network integrates the detection network and the density map estimation network. When the distribution density of aphids is low, it utilizes the improved Yolov5 to count aphids. Conversely, when the distribution density of aphids is high, it switches to CSRNet to count aphids.

`python hybird_network_image.py --weights ./runs/train/yolov5s-2-DCN2-low/weights/best.pt --source ./dataset/voc2013/JPEGImages/IMG_40_1.jpg --device 0` # For single image test

`python hybird_network_image.py --weights ./runs/train/yolov5s-2-DCN2-low/weights/best.pt --source ./images --device 0` # For image_file test

`python hybird_network_test.py --data data/aphid_voc.yaml --weights ./runs/train/yolov5s-2-DCN2-low/weights/best.pt --device '0' --batch-size 1` # Test on the test set

`python hybird_network_test_Thresholds_Figure.py --data data/aphid_voc.yaml --weights ./runs/train/yolov5s-2-DCN2-low/weights/best.pt --device '0' --batch-size 1` # vary T from 0 to 200 with an interval of 5 and carry out counting test to get the optimal T
   
## Citation
Gao, X., Xue, W., Lennox, C., Stevens, M. and Gao, J., 2024. Developing a hybrid convolutional neural network for automatic aphid counting in sugar beet fields. Computers and Electronics in Agriculture, 220, p.108910.

## Contact
If you have any issue, please contact us.



#python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2022.yaml --cfg models/yolov5s-2-DCN2.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100
#python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2023.yaml --cfg models/yolov5s-2-DCN2.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100
#python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2025.yaml --cfg models/yolov5s-2-DCN2.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100
#python multiple_split_train.py --img 640 --batch 4 --epoch 1 --data data/aphid_voc_2026.yaml --cfg models/yolov5s-2-DCN2.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100
#python train.py --img 1472 --batch 4 --epoch 300 --data data/aphid_voc_2043.yaml --cfg models/yolov5s-2-DCN2.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100
#python train.py --img 1472 --batch 4 --epoch 600 --data data/aphid_voc_2044.yaml --cfg models/yolov5s-2-DCN2.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100
#python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2045.yaml --cfg models/yolov5s-2-DCN2.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100
#python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2046.yaml --cfg models/yolov5s-2-DCN2.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100
#python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2048.yaml --cfg models/yolov5s.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100 #Original_yolov5
#python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2048.yaml --cfg models/yolov5s-2-DCN2.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100 #First_improved_yolov5
#python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2045.yaml --cfg models/yolov5s-final.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100

#python train.py --img 640 --batch 4 --epoch 600 --data /home/xumin/yolov5/data/aphid_voc_2045.yaml --cfg models/yolov5s-final.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100
#python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2051.yaml --cfg models/yolov5s-final.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100
#python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2053.yaml --cfg models/yolov5s-final.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100


#python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2054.yaml --cfg models/yolov5s.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100
#python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2054.yaml --cfg models/yolov5s-ODConv.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100
#python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2054.yaml --cfg models/yolov5s_cotnet2.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100
#python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2054.yaml --cfg models/yolov5s-CA.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100
#python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2054.yaml --cfg models/yolov5s-final.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100

python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2054.yaml --cfg models/yolov5s-ODConv-CoT3.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100
python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2054.yaml --cfg models/yolov5s-ODConv-CoT3-CA.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100

#python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2054.yaml --cfg models/yolov5s.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100
python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2055.yaml --cfg models/yolov5s.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100
python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2055.yaml --cfg models/yolov5s-ODConv.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100
python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2055.yaml --cfg models/yolov5s_cotnet2.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100
python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2055.yaml --cfg models/yolov5s-CA.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100
python train.py --img 640 --batch 4 --epoch 600 --data data/aphid_voc_2054.yaml --cfg models/yolov5s-final.yaml --weights weights/yolov5s.pt --device '0' --patience 0 --save-period 100


#cd ..
#cd yolov5/
#./train_sh.sh





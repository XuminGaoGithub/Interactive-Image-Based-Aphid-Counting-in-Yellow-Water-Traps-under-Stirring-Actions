# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
import cv2

# Path to the folder containing XML files
xml_folder = './labels/'

# Path to the folder containing images
img_folder = './src/'

# Output folder for processed images
output_folder = './gt/'

# Iterate over each file in the XML folder
for xml_file in os.listdir(xml_folder):
    if xml_file.endswith('.xml'):
        name = os.path.splitext(xml_file)[0]
        tree = ET.parse(os.path.join(xml_folder, xml_file))
        root = tree.getroot()
        
        # Read the corresponding image
        imgfile = os.path.join(img_folder, name + '.jpg')
        im = cv2.imread(imgfile)
        
        number = 0
        for object in root.findall('object'):
            number += 1
            object_name = object.find('name').text
            Xmin = int(object.find('bndbox').find('xmin').text)
            Ymin = int(object.find('bndbox').find('ymin').text)
            Xmax = int(object.find('bndbox').find('xmax').text)
            Ymax = int(object.find('bndbox').find('ymax').text)
            color = (56, 56, 255)
            cv2.rectangle(im, (Xmin, Ymin), (Xmax, Ymax), color, thickness=5, lineType=cv2.LINE_AA)
        im = cv2.resize(im, (2000, 2000))
        count_number = "Aphids:{}".format(number)
        cv2.putText(im, count_number, (150, 150), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 0), 12)

        output_path = os.path.join(output_folder, name + '_gt.jpg')
        cv2.imwrite(output_path, im)


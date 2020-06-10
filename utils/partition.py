# Partitions a dataset into train and test sets

import shutil
import os
import re


def partition_dir(src_img, src_xml, train_img, train_xml, test_img, test_xml, ratio):
       
    images = [f for f in os.listdir(src_img)
              if re.search(r'([a-zA-Z0-9\s_\\.\-\(\):])+(.jpg|.jpeg|.png)$', f)]

     
    num_images = len(images)
    num_test_images = math.ceil(ratio*num_images)
    
    print(num_test_images)
        
    for i in range(num_test_images):
        idx = random.randint(0, len(images)-1)
        
        filename = images[idx]
        filename_path = os.path.join(src_img, filename)
        
        xml_filename = os.path.splitext(filename)[0]+'.xml'
        xml_path = os.path.join(src_xml, xml_filename)
        
        #copy image + XML files across only if accompanying XML file exists
        if os.path.isfile(xml_path):     
                shutil.copyfile(filename_path, os.path.join(test_img, filename))
                shutil.copyfile(xml_path,os.path.join(test_xml,xml_filename))
        else:
            print("WARNING: the following XML file does not exist:" + xml_path)
        images.remove(images[idx])

    for filename in images:
        xml_filename = os.path.splitext(filename)[0]+'.xml'
        xml_path = os.path.join(src_xml, xml_filename)
        filename_path = os.path.join(src_img, filename)
        
        #copy image + XML files across only if accompanying XML file exists
        if os.path.isfile(xml_path):
                shutil.copyfile(filename_path, os.path.join(train_img, filename))
                shutil.copyfile(xml_path, os.path.join(train_xml, xml_filename))
        else:
            print("WARNING: the following XML file does not exist:" + xml_path)

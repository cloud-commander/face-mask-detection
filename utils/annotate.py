import os
from lxml import etree as ET
import cv2
import wget
import numpy as np
from PIL import Image, ImageFile


url = 'https://raw.githubusercontent.com/cloud-commander/face-mask-detection/master/utils/lbpcascade_frontalface_improved.xml'
#filename = wget.download(url)
face_cascade = cv2.CascadeClassifier(wget.download(url))

def annotate(IMG_INPUT,XML_OUTPUT):
	for subdir, dirs, files in os.walk(IMG_INPUT):
		for file in files:
			
			img_path=os.path.join(subdir, file)
			img_name=os.path.basename(img_path)

			if img_path.lower().endswith(('.png', '.jpg', '.jpeg')):

				img = cv2.imread(img_path)
				gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
				h,w,bpp = np.shape(img)
				imgp = Image.open(img_path)
	#            b, landmarks = detect_faces(imgp)
				faces = face_cascade.detectMultiScale(gray, 1.3, 5)


	#            g=show_bboxes(imgp, b, landmarks)
				#print(len(faces))
				if len(faces) == 1 :
					try :

						for bounding_boxes in faces:
							face = img[int(bounding_boxes[1]):int(bounding_boxes[3]),
							int(bounding_boxes[0]):int(bounding_boxes[2])]

							
							subdir_path, subdir_name = os.path.split(subdir)

							root = ET.Element("annotation",verified="yes")
							ET.SubElement(root, "folder").text=IMG_INPUT

							ET.SubElement(root, "filename").text = img_name
							#ET.SubElement(root, "path").text = img_path

							source=ET.SubElement(root, "source")
							ET.SubElement(source, "database").text = "Cloud Commander"

							size=ET.SubElement(root, "size")
							ET.SubElement(size, "width").text = str(w)
							ET.SubElement(size, "height").text = str(h)
							ET.SubElement(size, "depth").text = str(bpp)

							ET.SubElement(root, "segmented").text = "0"

							obj=ET.SubElement(root, "object")
							ET.SubElement(obj, "name").text = subdir_name
							ET.SubElement(obj, "pose").text = "Frontal"
							ET.SubElement(obj, "truncated").text = "0"
							ET.SubElement(obj, "difficult").text = "0"

							box=ET.SubElement(obj, "bndbox")
							ET.SubElement(box, "xmin").text = str(int(bounding_boxes[0]))
							ET.SubElement(box, "ymin").text = str(int(bounding_boxes[1]))
							ET.SubElement(box, "xmax").text = str(int(bounding_boxes[2])+int(bounding_boxes[1]))
							ET.SubElement(box, "ymax").text = str(int(bounding_boxes[3]))

							tree = ET.ElementTree(root)
							tree.write(os.path.join(XML_OUTPUT, os.path.splitext(img_name)[0] + '.xml'))
							
							
					except RuntimeError :
						with open("delete.txt", "a") as myfile:
							myfile.write(img_path+"\n")
						

					else :
						with open("delete.txt", "a") as myfile:
								myfile.write(img_path+"\n")
#Generates XML Annotations for images that contain human faces

import os
from lxml import etree as ET
import cv2
import wget
import numpy as np
from PIL import Image, ImageFile
import face_recognition


def annotate(IMG_INPUT,XML_OUTPUT, CLASS):
	for subdir, dirs, files in os.walk(IMG_INPUT):
		for file in files:
			
			img_path=os.path.join(subdir, file)
			img_name=os.path.basename(img_path)

			if img_path.lower().endswith(('.png', '.jpg', '.jpeg')):

				img = face_recognition.load_image_file(img_path)
				face_locations = face_recognition.face_locations(img, number_of_times_to_upsample=0, model="cnn")
							


	#            g=show_bboxes(imgp, b, landmarks)
				#print(len(face_locations))
				if len(face_locations) == 1 :
					try :

						for face_location in face_locations:
							#face = img[int(bounding_boxes[1]):int(bounding_boxes[3]),
							#int(bounding_boxes[0]):int(bounding_boxes[2])]
							top, right, bottom, left = face_location
							
							subdir_path, subdir_name = os.path.split(subdir)

							root = ET.Element("annotation",verified="yes")
							ET.SubElement(root, "folder").text=CLASS

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
							ET.SubElement(obj, "name").text = CLASS
							ET.SubElement(obj, "pose").text = "Frontal"
							ET.SubElement(obj, "truncated").text = "0"
							ET.SubElement(obj, "difficult").text = "0"

							box=ET.SubElement(obj, "bndbox")
							ET.SubElement(box, "xmin").text = str(top)
							ET.SubElement(box, "ymin").text = str(right)
							ET.SubElement(box, "xmax").text = str(bottom)
							ET.SubElement(box, "ymax").text = str(left)

							tree = ET.ElementTree(root)
							tree.write(os.path.join(XML_OUTPUT, os.path.splitext(img_name)[0] + '.xml'))
							
							
					except RuntimeError :
						with open("delete.txt", "a") as myfile:
							myfile.write(img_path+"\n")
						

					else :
						with open("delete.txt", "a") as myfile:
								myfile.write(img_path+"\n")

# Configuration file to set the various directories needed for the project

##################### DIRECTORY STRUCTURE ###############################
#- content
#	- models
#		- official
#		- research
#		- samples
#		- tutorials
#		- pre-trained-model	
#	- drive
#		- Machine Learning
#			- Datasets
#			- Projects
#				- project_dir
#					- Dev
#					- Complete			
#	- project_dir
#		- dataset
#			- unprepapared
#				- images
#				- annotations
#				- mask
#			- prepared
#				- record
#				- train
#					- images
#					- annotations
#				- test
#					- images
#					- annotations					
#			- tmp1
#			- tmp2							
#		- scripts
#			- preprocessing		
#				
#		- training
#			- checkpoints
#			- config
#			- trained_graphs
#				- inference_graph
#				- tf_lite_graph
#			- trained-models
#				- tflite
#				- tfjs
#############################################################################


### Enter the name of the project ####
PROJECT_DIR = "/Face-Mask-Detection" #
######################################



### Your Google Drive Folders - ***CREATE THESE MANUALLY***
DRIVE_BASE = "/content/drive/My\ Drive"
DRIVE_ML = DRIVE_BASE + "/'Machine Learning'"
DRIVE_DATASETS = DRIVE_ML + "/Datasets"
DRIVE_PROJECTS = DRIVE_ML + "/Projects"
DRIVE_TF = DRIVE_ML + "/TensorFlow"
DRIVE_CURRENT_PROJECT = DRIVE_PROJECTS + PROJECT_DIR 
DRIVE_DEV = DRIVE_CURRENT_PROJECT + "/Dev/"
DRIVE_COMPLETE = DRIVE_CURRENT_PROJECT + "/Complete/"

#Sets the base directory for our project"
BASE_DIR = "/content"

#Folder that will hold the models from TensorFlow
TF_MODEL_DIR = BASE_DIR + "/models" 

#Sets the project folder directory
LEARN_DIR = BASE_DIR + PROJECT_DIR

#Sets the unprepared dataset directoies
DATASET_DIR = LEARN_DIR + "/dataset"
DATASET_DIR_UNPREP = DATASET_DIR + "/unprepared"
DATASET_DIR_UNPREP_IMG = DATASET_DIR_UNPREP + "/images"
DATASET_DIR_UNPREP_ANNO = DATASET_DIR_UNPREP + "/annotations"
DATASET_DIR_UNPREP_MASKS = DATASET_DIR_UNPREP + "/mask"

#Sets the prepared dataset directories
DATASET_DIR_PREP = DATASET_DIR + "/prepared"
DATASET_DIR_PREP_TRAIN = DATASET_DIR_PREP  + "/train"
DATASET_DIR_PREP_TEST = DATASET_DIR_PREP  + "/test"
DATASET_DIR_PREP_TRAIN_IMG = DATASET_DIR_PREP_TRAIN + "/images"
DATASET_DIR_PREP_TRAIN_ANNO = DATASET_DIR_PREP_TRAIN + "/annotations" 	#HOLDS THE XML ANNOTATIONS
DATASET_DIR_PREP_TEST_IMG = DATASET_DIR_PREP_TEST + "/images"
DATASET_DIR_PREP_TEST_ANNO = DATASET_DIR_PREP_TEST + "/annotations"		#HOLDS THE XML ANNOTATIONS
DATASET_DIR_PREP_RECORD = DATASET_DIR_PREP + "/record"

#Sets the temp dataset directories
DATASET_DIR_TMP1 = DATASET_DIR + "/tmp1"
DATASET_DIR_TMP2 = DATASET_DIR + "/tmp2"

#Sets the preprocessing scripts directory
PRE_PROCESS_DIR = LEARN_DIR + "/scripts/preprocessing"

#Sets the training directory
TRAIN_DIR = LEARN_DIR + "/training"

#Sets the config file directory
CONFIG_DIR = TRAIN_DIR + "/config/"

#Sets the checkpoint directory
CKPT_DIR = TRAIN_DIR + "/checkpoints"

#Sets the trained graph directories
GRAPH_DIR = TRAIN_DIR + "/trained_graphs"
INF_GRAPH = GRAPH_DIR + "/inference_graph"
TF_LITE_GRAPH = GRAPH_DIR + "/tf_lite_graph"

#Sets the trained model directories
TRAINED_MODELS = TRAIN_DIR+ "/trained-models"
TF_LITE_MODEL = TRAINED_MODELS + "/tflite"
TF_JS_MODEL = TRAINED_MODELS + "/tfjs"

#Tensors for model conversion
INPUT_TENSORS = "normalized_input_image_tensor"
OUTPUT_TENSORS = "TFLite_Detection_PostProcess,TFLite_Detection_PostProcess:1,TFLite_Detection_PostProcess:2,TFLite_Detection_PostProcess:3"

#UTILS URLS
ANNOTATE = "https://raw.githubusercontent.com/cloud-commander/face-mask-detection/master/utils/annotate.py"
PLACE_MASKS = "https://raw.githubusercontent.com/cloud-commander/face-mask-detection/master/utils/place_masks.py"
PARTITION = "https://raw.githubusercontent.com/cloud-commander/face-mask-detection/master/utils/partition.py"
XML_TO_CSV = "https://raw.githubusercontent.com/cloud-commander/face-mask-detection/master/utils/xml_to_csv.py"
TF_RECORD = "https://raw.githubusercontent.com/cloud-commander/face-mask-detection/master/utils/generate_tfrecord.py"
MOVE_FILES = "https://raw.githubusercontent.com/cloud-commander/face-mask-detection/master/utils/move_files.py"
CASCADE = "https://raw.githubusercontent.com/cloud-commander/face-mask-detection/master/utils/lbpcascade_frontalface_improved.xml"

#CONFIG URLS
CONSTANTS = "https://raw.githubusercontent.com/cloud-commander/face-mask-detection/master/config/constants.py"
LABEL_MAP = "https://raw.githubusercontent.com/cloud-commander/face-mask-detection/master/config/label_map.pbtxt"

#DATASET URLS
UNMASKED_FACES_DATASET = "https://raw.githubusercontent.com/cloud-commander/face-mask-detection/master/data/1k_faces_00.zip"
MASKED_FACES_DATASET = "https://raw.githubusercontent.com/cloud-commander/face-mask-detection/master/data/1k_faces_01.zip"
MASKS_DATASET = "https://raw.githubusercontent.com/cloud-commander/face-mask-detection/master/data/mask_photos.tar.xz"

#PRE TRAINED MODELS - COMMENT OUT AS APPROPRIATE
#PRETRAINED_MODEL_NAME="facessd_mobilenet_v2_quantized_320x320_open_image_v4"
#PRETRAINED_MODEL_URL="http://download.tensorflow.org/models/object_detection/facessd_mobilenet_v2_quantized_320x320_open_image_v4.tar.gz"
#PRETRAINED_MODEL_DIR= "/content/models/" + PRETRAINED_MODEL_NAME
#PRETRAINED_MODEL_CONFIG = "https://raw.githubusercontent.com/cloud-commander/face-mask-detection/master/config/face_pipeline.config"

#PRETRAINED_MODEL_NAME="ssd_mobilenet_v1_quantized_300x300_coco14_sync_2018_07_18"
#PRETRAINED_MODEL_URL="http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_quantized_300x300_coco14_sync_2018_07_18.tar.gz"
#PRETRAINED_MODEL_DIR= "/content/models/" + PRETRAINED_MODEL_NAME
#PRETRAINED_MODEL_CONFIG = "https://raw.githubusercontent.com/cloud-commander/face-mask-detection/master/config/mobilenet_v1_pipeline.config"

PRETRAINED_MODEL_NAME="ssd_mobilenet_v2_quantized_300x300_coco_2019_01_03"
PRETRAINED_MODEL_URL="http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_quantized_300x300_coco_2019_01_03.tar.gz"
PRETRAINED_MODEL_DIR= "/content/models/" + PRETRAINED_MODEL_NAME
PRETRAINED_MODEL_CONFIG = "https://raw.githubusercontent.com/cloud-commander/face-mask-detection/master/config/mobilenet_v2_pipeline.config"

# Loads a list with the edges of the required directory structure
DIRECTORIES = [PRE_PROCESS_DIR, DATASET_DIR_UNPREP_IMG, \
               DATASET_DIR_UNPREP_ANNO, DATASET_DIR_PREP_TRAIN_IMG, \
               DATASET_DIR_PREP_TRAIN_ANNO, DATASET_DIR_PREP_TEST_IMG, \
               DATASET_DIR_PREP_TEST_ANNO, DATASET_DIR_PREP_RECORD, \
	       DATASET_DIR_TMP1, DATASET_DIR_TMP2, CONFIG_DIR,  \
               INF_GRAPH, TF_LITE_GRAPH, CKPT_DIR, PRETRAINED_MODEL_DIR , \
               TF_LITE_MODEL, TF_JS_MODEL  ]

#create the required directories
import os
for DIR in DIRECTORIES:
    os.makedirs(DIR, exist_ok=True)

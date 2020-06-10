import cv2
import numpy as np
import face_recognition
from lxml import etree as ET
from PIL import Image, ImageFile



def save(face_image_file, current_image_file):
    face_image_file.save(current_image_file)
    print(f'Save to {current_image_file}')
    

def create_mask(current_image_file, current_mask_file, model):
    show = False

    KEY_FACIAL_FEATURES = ('nose_bridge', 'chin')
    face_image_file: ImageFile = None
    mask_image_file: ImageFile = None

    face_image_np = face_recognition.load_image_file(current_image_file)
    face_locations = face_recognition.face_locations(
        face_image_np, model=model)
    face_landmarks = face_recognition.face_landmarks(
        face_image_np, face_locations)
    face_image_file = Image.fromarray(face_image_np)
    mask_image_file = Image.open(current_mask_file)

    found_face = False
    for face_landmark in face_landmarks:

        # check whether facial features meet requirement
        skip = False
        for facial_feature in KEY_FACIAL_FEATURES:
            if facial_feature not in face_landmark:
                skip = True
                break
            if skip:
                continue

            # mask face
            found_face = True
            place_mask(face_landmark, mask_image_file, face_image_file)

    if found_face:
        if show:
            face_image_file.show()

        # save
        save(face_image_file,current_image_file)
    else:
        print('Found no face.')


def place_mask(face_landmark: dict, mask_image_file, face_image_file):
    nose_bridge = face_landmark['nose_bridge']
    nose_point = nose_bridge[len(nose_bridge) * 1 // 4]
    nose_v = np.array(nose_point)

    chin = face_landmark['chin']
    chin_len = len(chin)
    chin_bottom_point = chin[chin_len // 2]
    chin_bottom_v = np.array(chin_bottom_point)
    chin_left_point = chin[chin_len // 8]
    chin_right_point = chin[chin_len * 7 // 8]

    # split mask and resize
    width = mask_image_file.width
    height = mask_image_file.height
    width_ratio = 1.2
    new_height = int(np.linalg.norm(nose_v - chin_bottom_v))

    # left
    mask_left_img = mask_image_file.crop((0, 0, width // 2, height))
    mask_left_width = get_distance_from_point_to_line(
        chin_left_point, nose_point, chin_bottom_point)
    mask_left_width = int(mask_left_width * width_ratio)
    mask_left_img = mask_left_img.resize((mask_left_width, new_height))

    # right
    mask_right_img = mask_image_file.crop((width // 2, 0, width, height))
    mask_right_width = get_distance_from_point_to_line(
        chin_right_point, nose_point, chin_bottom_point)
    mask_right_width = int(mask_right_width * width_ratio)
    mask_right_img = mask_right_img.resize((mask_right_width, new_height))

    # merge mask
    size = (mask_left_img.width + mask_right_img.width, new_height)
    mask_img = Image.new('RGBA', size)
    mask_img.paste(mask_left_img, (0, 0), mask_left_img)
    mask_img.paste(mask_right_img, (mask_left_img.width, 0), mask_right_img)

    # rotate mask
    angle = np.arctan2(
        chin_bottom_point[1] - nose_point[1], chin_bottom_point[0] - nose_point[0])
    rotatedmask_image_file = mask_img.rotate(angle, expand=True)

    # calculate mask location
    center_x = (nose_point[0] + chin_bottom_point[0]) // 2
    center_y = (nose_point[1] + chin_bottom_point[1]) // 2

    offset = mask_img.width // 2 - mask_left_img.width
    radian = angle * np.pi / 180
    box_x = center_x + int(offset * np.cos(radian)) - \
        rotatedmask_image_file.width // 2
    box_y = center_y + int(offset * np.sin(radian)) - \
        rotatedmask_image_file.height // 2

    # add mask
    face_image_file.paste(mask_img, (box_x, box_y), mask_img)


def get_distance_from_point_to_line(point, line_point1, line_point2):
    distance = np.abs((line_point2[1] - line_point1[1]) * point[0] +
                      (line_point1[0] - line_point2[0]) * point[1] +
                      (line_point2[0] - line_point1[0]) * line_point1[1] +
                      (line_point1[1] - line_point2[1]) * line_point1[0]) / \
        np.sqrt((line_point2[1] - line_point1[1]) * (line_point2[1] - line_point1[1]) +
                (line_point1[0] - line_point2[0]) * (line_point1[0] - line_point2[0]))
    return int(distance)

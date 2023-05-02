import os
import cv2
import glob
import xml.etree.ElementTree as ET
from albumentations import (
    Compose, HorizontalFlip, VerticalFlip, RandomRotate90, ShiftScaleRotate, RandomBrightnessContrast,
)

def read_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    return tree, root

def apply_augmentations(image, boxes, labels, aug):
    transformed = aug(image=image, bboxes=boxes, labels=labels)
    return transformed['image'], transformed['bboxes']

def update_xml(xml_tree, new_boxes):
    root = xml_tree.getroot()
    for i, box in enumerate(new_boxes):
        obj = root.findall('object')[i]
        bndbox = obj.find('bndbox')
        bndbox.find('xmin').text = str(int(box[0]))
        bndbox.find('ymin').text = str(int(box[1]))
        bndbox.find('xmax').text = str(int(box[2]))
        bndbox.find('ymax').text = str(int(box[3]))
    return xml_tree

def save_image_and_annotation(image, xml_tree, output_img_path, output_xml_path):
    cv2.imwrite(output_img_path, image)
    xml_tree.write(output_xml_path)

def process_batch(input_images_folder, input_xml_folder, output_images_folder, output_xml_folder):
    aug = Compose([
        HorizontalFlip(p=0.5),
        VerticalFlip(p=0.5),
        ShiftScaleRotate(shift_limit=0.3, scale_limit=0.4, rotate_limit=70, p=0.5, border_mode=cv2.BORDER_REPLICATE),
        RandomBrightnessContrast(p=0.5),
    ], bbox_params={'format': 'pascal_voc', 'label_fields': ['labels'], 'check_each_transform': True})

    image_files_jpg = glob.glob(os.path.join(input_images_folder, '*.jpg'))
    image_files_png = glob.glob(os.path.join(input_images_folder, '*.png'))
    image_files = image_files_jpg + image_files_png
    print(f'Processing {len(image_files)} images...')

    for img_path in image_files:
        print(f'Processing {img_path}')
        img_name = os.path.basename(img_path)
        xml_path = os.path.join(input_xml_folder, os.path.splitext(img_name)[0] + '.xml')

        image = cv2.imread(img_path, cv2.IMREAD_COLOR)
        tree, root = read_xml(xml_path)
        boxes = []
        labels = []

        for obj in root.findall('object'):
            label = obj.find('name').text
            bndbox = obj.find('bndbox')
            xmin = int(bndbox.find('xmin').text)
            ymin = int(bndbox.find('ymin').text)
            xmax = int(bndbox.find('xmax').text)
            ymax = int(bndbox.find('ymax').text)
            boxes.append([xmin, ymin, xmax, ymax])
            labels.append(label)

        for i in range(10):
            augmented_image, new_boxes = apply_augmentations(image, boxes, labels, aug)

            # Remove any bounding box that goes beyond the image dimensions
            valid_boxes = []
            for box in new_boxes:
                xmin, ymin, xmax, ymax = box
                if xmin >= 0 and ymin >= 0 and xmax <= augmented_image.shape[1] and ymax <= augmented_image.shape[0]:
                    valid_boxes.append(box)

            if not valid_boxes:
                continue

            new_xml_tree = update_xml(tree, valid_boxes)

            output_img_path = os.path.join(output_images_folder, os.path.splitext(img_name)[0] + f'_aug{i}.jpg')
            output_xml_path = os.path.join(output_xml_folder, os.path.splitext(img_name)[0] + f'_aug{i}.xml')

            save_image_and_annotation(augmented_image, new_xml_tree, output_img_path, output_xml_path)
            print(f'Saved augmented image and XML to {output_img_path}')

if __name__ == '__main__':
    input_images_folder = r'D:\work\28-03 tue\PHOTOEDIT\test'  # Update with your input images folder path
    input_xml_folder = r'D:\work\28-03 tue\PHOTOEDIT\test'  # Update with your input XML folder path
    output_images_folder = r'D:\work\28-03 tue\PHOTOEDIT\New folder'  # Update with your output images folder path
    output_xml_folder = r'D:\work\28-03 tue\PHOTOEDIT\New folder'  # Update with your output XML folder path

    # Create output folders if they don't exist
    os.makedirs(output_images_folder, exist_ok=True)
    os.makedirs(output_xml_folder, exist_ok=True)

    process_batch(input_images_folder, input_xml_folder, output_images_folder, output_xml_folder)
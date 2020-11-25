import glob
import os

import cv2

kitti_to_yolo_label_map = {}

# annotations_path = input ("input path to annotations labels\t")
# images_path = input ("input path to annotations images\t")
# labels = input ("input labels_path\t")
# converted_annotations_path = input ("output path to converted annotations\t")

annotations_path = "/mnt/7A94CE8894CE45FB/DATA/VA/labels_640_360/labels/"
images_path = "/mnt/7A94CE8894CE45FB/DATA/VA/images_640_360/images"
labels = "annot_labels.txt"
converted_annotations_path = "/mnt/7A94CE8894CE45FB/DATA/VA/labels_640_360_converted"

if not  os.path.exists (annotations_path):
    print("annotations path does not exists")
    exit(1)

if not  os.path.isfile (labels):
    print("lables path does not exists")
    exit(1)

if not  os.path.exists (converted_annotations_path):
    print("converted output path does not exists")
    exit(1)

if not  os.path.exists (images_path):
    print("images path does not exists")
    exit(1)

with open (labels , 'r') as f:
    lines = f.readlines ()
    i = 0
    for l in lines:
        kitti_to_yolo_label_map.update ({l[ 0:-1 ]: i})
        i += 1

if os.path.samefile (annotations_path , converted_annotations_path):
    print ('input and output path cannot be same')
    exit (1)

annotations = glob.glob (annotations_path + '/*.txt')

print("total files :-", len(annotations))

for a in annotations:
    print (a)
    with open (a , 'r') as f:
        lines = f.readlines ()
        # img = None
        base_filename = os.path.basename(a)
        image_file = images_path + '/' + base_filename[0:-4] + ".jpg"
        if not os.path.isfile(image_file):
            print("image does not exists")
            continue
        img = cv2.imread (image_file)
        if img is not None:
            rows , cols , _ = img.shape
            print (rows , cols)
            yolo_marks = [ ]
            for l in lines:
                label = l[ 0:-1 ]
                print (label)
                words = label.split (' ')
                label_index = kitti_to_yolo_label_map.get (words[ 0 ] , None)
                if label_index is not None:
                    print (words)
                    roi_tlx = int (float(words[ 4 ]))
                    roi_tly = int (float(words[ 5 ]))
                    roi_brx = int (float(words[ 6 ]))
                    roi_bry = int (float(words[ 7 ]))

                    w = roi_brx - roi_tlx
                    h = roi_bry - roi_tly

                    relative_center_x = float ((roi_tlx + w / 2) / cols)
                    relative_center_y = float ((roi_tly + h / 2) / rows)
                    relative_width = float (w / cols)
                    relative_height = float (h / rows)

                    yolo_marks.append (str (label_index) + " " +
                                       str (relative_center_x) + " " +
                                       str (relative_center_y) + " " +
                                       str (relative_width) + " " +
                                       str (relative_height))

                    cv2.rectangle (img , (roi_tlx , roi_tly) , (roi_brx , roi_bry) , (0 , 255 , 0) , 2)

            cv2.imshow ('image' , img)
            cv2.waitKey (1)
            if len(yolo_marks) != 0:
                with open (converted_annotations_path + '/' + os.path.basename (a) , 'w') as f:
                    pass
                for m in yolo_marks:
                    with open (converted_annotations_path + '/' + os.path.basename (a) , 'a') as f:
                        f.write (m + '\n')

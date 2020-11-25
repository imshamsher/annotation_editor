import glob
import os

import cv2

yolo_to_kitti_label_map = {}

# annotations_path = input ("input path to annotations labels\t")
# images_path = input ("input path to annotations images\t")
# labels = input ("input labels_path\t")
# converted_annotations_path = input ("output path to converted annotations\t")

annotations_path = "./converted"
images_path = "./sample"
labels = "annot_labels.txt"
converted_annotations_path = "./labels_kitti_converted"
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
        yolo_to_kitti_label_map.update ({str(i):l[ 0:-1 ]})
        i += 1
input(yolo_to_kitti_label_map)

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
        else:
            print("\n\nimage found\n\n")
        img = cv2.imread (image_file)
        if img is not None:
            rows , cols , _ = img.shape
            print (rows , cols)
            kitti_marks = []
            for l in lines:
                label = l[ 0:-1 ]
                print (label)
                words = label.split (' ')
                label_index = yolo_to_kitti_label_map.get (words[ 0 ] , None)
                print(label_index)
                if label_index is not None:
                    print (words)

                    relative_center_x = float(words[1])
                    relative_center_y = float(words[2])
                    relative_width = float(words[3])
                    relative_height = float(words[4])

                    roi_tlx = int((relative_center_x - relative_width / 2) * cols)
                    roi_tly = int((relative_center_y - relative_height / 2) * rows)
                    w = int(relative_width * cols)
                    h = int(relative_height * rows)
                    roi_brx = roi_tlx + w
                    roi_bry = roi_tly + h

                    kitti_marks.append (str (label_index) + " 0.0 0 0.0 " +
                                       str (roi_tlx) + " " +
                                       str (roi_tly) + " " +
                                       str (roi_brx) + " " +
                                       str (roi_bry) + " 0.0 0.0 0.0 0.0 0.0 0.0 0.0")

                    cv2.putText(img,label_index,(roi_tlx , roi_tly-3),1,1,(0,0,0),1)
                    cv2.rectangle (img , (roi_tlx , roi_tly) , (roi_brx , roi_bry) , (0 , 255 , 0) , 1)

            cv2.imshow ('image' , img)
            cv2.waitKey (0)
            if len(kitti_marks) != 0:
                with open (converted_annotations_path + '/' + os.path.basename (a) , 'w') as f:
                    pass
                for m in kitti_marks:
                    with open (converted_annotations_path + '/' + os.path.basename (a) , 'a') as f:
                        f.write (m + '\n')

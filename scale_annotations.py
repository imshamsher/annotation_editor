import glob
import os
import cv2

scale_w = 640
scale_h = 360


annotations_path = "./labels_kitti_converted"
images_path = "./sample"
converted_annotations_path = "./labels_640_360_converted"


if not  os.path.exists (annotations_path):
    print("annotations path does not exists")
    exit(1)


if not  os.path.exists (converted_annotations_path):
    print("converted output path does not exists")
    exit(1)


if os.path.samefile (annotations_path , converted_annotations_path):
    print ('input and output path cannot be same')
    exit (1)

if not  os.path.exists (images_path):
    print("images path does not exists")
    exit(1)

annotations = glob.glob (annotations_path + '/*.txt')

print("total files :-", len(annotations))

for a in annotations:
    print (a)
    with open (a , 'r') as f:
        lines = f.readlines ()

        base_filename = os.path.basename(a)
        image_file = images_path + '/' + base_filename[0:-4] + ".jpg"
        if not os.path.isfile(image_file):
            print("image does not exists")
            continue
        img = cv2.imread(image_file)

        if img is not None:
            orig_h , orig_w , _ = img.shape
            print (orig_w , orig_h)

            kitti_marks = [ ]
            for l in lines:
                label = l[ 0:-1 ]
                print (label)
                words = label.split (' ')
                print (words)
                words[ 4 ] = str(int (int (words[ 4 ]) * scale_w/orig_w))
                words[ 5 ] = str(int (int (words[ 5 ]) * scale_h/orig_h))
                words[ 6 ] = str(int (int (words[ 6 ]) * scale_w/orig_w))
                words[ 7 ] = str(int (int (words[ 7 ]) * scale_h/orig_h))

                updated_kitti_marks = ''
                for w in words:
                    updated_kitti_marks += w + " "

                kitti_marks.append (updated_kitti_marks)

        if len(kitti_marks) != 0:
            with open (converted_annotations_path + '/' + os.path.basename (a) , 'w') as f:
                pass
            for m in kitti_marks:
                with open (converted_annotations_path + '/' + os.path.basename (a) , 'a') as f:
                    f.write (m + '\n')

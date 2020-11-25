# annotation_editor
A tool for editing label file saved in different formats
## Current supported formats
- yolo
- kitti

## yolo to kitti annotations conversions
#### edit following paths to run yolo_to_kitti.py
- annotations_path = "./yolo_marking"
- images_path = "./sample"
- labels = "annot_labels.txt"
- converted_annotations_path = "./labels_kitti_converted"

*annotaions_path*: it is the path where yolo format marked label files are present.
*images_path*: It is the path where images with respect to label files path are present.
*labels*: It is the path where labels name file is present.
*converted_annotations_path*: The path where the converted annotations from yolo to kitti
are present.

## kitti to yolo annotations conversions
#### edit following paths to run yolo_to_kitti.py
- annotations_path = "./kitti_marking"
- images_path = "./sample"
- labels = "annot_labels.txt"
- converted_annotations_path = "./labels_kitti_converted"

*annotaions_path*: it is the path where kitti format marked label files are present.
*images_path*: It is the path where images with respect to label files path are present.
*labels*: It is the path where labels name file is present.
*converted_annotations_path*: The path where the converted annotations from kitti to yolo
are present.


## merge annotations
A tool to merge annotaions from different label marking with respect to same image.
For example there are separate label marking for different classes like person, vehicle etc.
And you want them to added in common label files.
#### edit following paths to run merge_annotations.py
- merged = "./merged"
- folder_path = ""

*merged*: The path where the merged annotations are to be saved.
*folder_path*: The path where marking data set is present.


## scale annotations
A tool to scale annotations from original available images to some other scaled data set.
For example the marking has been done on 1080p resolution images and now you want to 
use the marking dataset with different resolution image by scaling say with width of
640 and height of 360.
#### edit following paths to run scale_annotations.py

- annotations_path = "./labels_kitti_converted"
- images_path = "./sample"
- converted_annotations_path = "./labels_640_360_converted"

*annotaions_path*: it is the path where kitti format marked label files are present.
*images_path*: It is the path where images with respect to label files path are present.
*converted_annotations_path*: The path where the converted annotations from kitti to yolo
are present.
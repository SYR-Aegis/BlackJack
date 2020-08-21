#! /usr/bin/python3

import tensorflow as tf
import os
import cv2
import numpy as np

from PIL import Image
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(im_height, im_width, 3).astype(np.uint8)

PATH_TO_CKPT = "trained_model/frozen_inference_graph.pb"
PATH_TO_LABELS = "labelmap.pbtxt"
NUM_CLASSES = 52

label_map = {
    1:"2h", 2:"3h", 3:"4h", 4:"5h", 5:"6h", 6:"7h", 7:"8h", 8:"9h", 9:"10h", 10:"jh", 11:"qh", 12:"kh", 13:"ah",
    14:"2d", 15:"3d", 16:"4d", 17:"5d", 18:"6d", 19:"7d", 20:"8d", 21:"9d", 22:"10d", 23:"jd", 24:"qd", 25:"kd", 26:"ad",
    17:"2c", 28:"3c", 29:"4c", 30:"5c", 31:"6c", 32:"7c", 33:"8c", 34:"9c", 35:"10c", 36:"jc", 37:"qc", 38:"kc", 39:"ac",
    40:"2s", 41:"3s", 42:"4s", 43:"5s", 44:"6s", 45:"7s", 46:"8s", 47:"9s", 48:"10s", 49:"js", 50:"qs", 51:"ks", 52:"as"
}

detection_graph = tf.Graph()

with detection_graph.as_default():
    od_graph_def = tf.compat.v1.GraphDef()
    with tf.io.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

labels = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(
    labels, max_num_classes=NUM_CLASSES, use_display_name=True
)
category_index = label_map_util.create_category_index(categories)

with detection_graph.as_default():
    with tf.compat.v1.Session(graph=detection_graph) as sess:
        # read image
        img = np.array(Image.open("test.jpg"))

        # expand dimensions since the model expects an image to have shape: [1, None, None, 3]
        img_expand = np.expand_dims(img, axis=0)

        # extract image tensor
        image_tensor = detection_graph.get_tensor_by_name("image_tensor:0")
        # extract detection boxes
        boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
        #extract detection scores
        scores = detection_graph.get_tensor_by_name("detection_scores:0")
        #extract detection classes
        classes = detection_graph.get_tensor_by_name("detection_classes:0")
        # extract number of detections
        num_detections = detection_graph.get_tensor_by_name("num_detections:0")

        # actual detection
        (boxes, scores, classes, num_detections) = sess.run(
            [boxes, scores, classes, num_detections],
            feed_dict={image_tensor: img_expand}
        )

        # visualization of the results of a detection
        vis_util.visualize_boxes_and_labels_on_image_array(
            img,
            np.squeeze(boxes),
            np.squeeze(classes).astype(np.int32),
            np.squeeze(scores),
            category_index,
            use_normalized_coordinates=True,
            line_thickness=8
        )

        # display output
        cv2.imshow('obj_detection', cv2.resize(img, (800,600)))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        scores.flatten()
        classes.flatten()

        detected_items = list()

        for row, r in zip(scores, range(len(scores))):
            for score, i in zip(row, range(len(row))):
                if score>=0.5:
                    detected_items.append(label_map[category_index[int(classes[r][i])]["id"]])
        
        print(set(detected_items))

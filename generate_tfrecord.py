#! /usr/bin/python3

"""
Usage:
  # From tensorflow/models/
  # Create train data:
  python generate_tfrecord.py --csv_input=data/train_labels.csv  --output_path=train.record
  # Create test data:
  python generate_tfrecord.py --csv_input=data/test_labels.csv  --output_path=test.record
"""

import os
import io
import sys
import pandas as pd
import tensorflow as tf

from PIL import Image
from object_detection.utils import dataset_util
from collections import namedtuple, OrderedDict

flags = tf.app.flags
flags.DEFINE_string('csv_input', './labels.csv', 'Path to the CSV input')
flags.DEFINE_string('output_path', './train.record', 'Path to output TFRecord')
flags.DEFINE_string('img_dir', './img/', 'Path to images')
FLAGS = flags.FLAGS

# add class labels
def class_text_to_int(row_label):
    if row_label == '2h':
        return 1
    elif row_label == "3h":
        return 2
    elif row_label == "4h":
        return 3
    elif row_label == "5h":
        return 4
    elif row_label == "6h":
        return 5
    elif row_label == "7h":
        return 6
    elif row_label == "8h":
        return 7
    elif row_label == "9h":
        return 8
    elif row_label == "10h":
        return 9
    elif row_label == "jh":
        return 10
    elif row_label == "qh":
        return 11
    elif row_label == "kh":
        return 12
    elif row_label == "ah":
        return 13
    elif row_label == "2d":
        return 14
    elif row_label == "3d":
        return 15
    elif row_label == "4d":
        return 16
    elif row_label == "5d":
        return 17
    elif row_label == "6d":
        return 18
    elif row_label == "7d":
        return 19
    elif row_label == "8d":
        return 20
    elif row_label == "9d":
        return 21
    elif row_label == "10d":
        return 22
    elif row_label == "jd":
        return 23
    elif row_label == "qd":
        return 24
    elif row_label == "kd":
        return 25
    elif row_label == "ad":
        return 26
    elif row_label == "2c":
        return 27
    elif row_label == "3c":
        return 28
    elif row_label == "4c":
        return 29
    elif row_label == "5c":
        return 30
    elif row_label == "6c":
        return 31
    elif row_label == "7c":
        return 32
    elif row_label == "8c":
        return 33
    elif row_label == "9c":
        return 34
    elif row_label == "10c":
        return 35
    elif row_label == "jc":
        return 36
    elif row_label == "qc":
        return 37
    elif row_label == "kc":
        return 38
    elif row_label == "ac":
        return 39
    elif row_label == "2s":
        return 40
    elif row_label == "3s":
        return 41
    elif row_label == "4s":
        return 42
    elif row_label == "5s":
        return 43
    elif row_label == "6s":
        return 44
    elif row_label == "7s":
        return 45
    elif row_label == "8s":
        return 46
    elif row_label == "9s":
        return 47
    elif row_label == "10s":
        return 48
    elif row_label == "js":
        return 49
    elif row_label == "qs":
        return 50
    elif row_label == "ks":
        return 51
    elif row_label == "as":
        return 52
    else:
        return -1

# return a list which is grouped by given group
def split(df, group):
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)

    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]

def create_tf_record(group, path):

    if group.filename not in os.listdir(path):
        print("Could not find {}".format(group.filename))
        sys.exit(0)

    with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid:
        encoded_jpg = fid.read()
    
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)

    width, height = image.size

    filename = group.filename.encode('utf8')
    print(filename)
    image_format = b'jpg'
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for index, row in group.object.iterrows():
        xmins.append(row['xmin'] / width)
        xmaxs.append(row['xmax'] / width)
        ymins.append(row['ymin'] / height)
        ymaxs.append(row['ymax'] / height)
        classes_text.append(row['class'].encode('utf8'))
        classes.append(class_text_to_int(row['class']))

    tf_example = tf.train.Example(features = tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))

    return tf_example

def main(_):
    print("Loading TFRecordWriter ...")
    writer = tf.python_io.TFRecordWriter(FLAGS.output_path)
    print("TFRecordWriter Loaded!")

    print("Setting image path ...")
    path = os.path.join(FLAGS.img_dir)
    print("Image path set!")

    print("Reading csv file ...")
    img_data = pd.read_csv(FLAGS.csv_input)
    print("csv file loaded!")

    # split dataframe with filenames
    grouped = split(img_data, 'filename')

    file_errors = 0

    for group in grouped:

        try:
            tf_example = create_tf_record(group, path)
            writer.write(tf_example.SerializeToString())
        except:
            file_errors += 1

    writer.close()

    print("FINISHED. There were {} errors".format(file_errors))

    output_path = os.path.join(os.getcwd(), FLAGS.output_path)
    print('Successfully created the TFRecords: {}'.format(output_path))


if __name__ == '__main__':
    tf.app.run()
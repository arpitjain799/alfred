"""

this script will using pycoco API
draw our converted annotation to check
if result is right or not

"""
from pycocotools.coco import COCO
import os
import sys
import cv2
from pycocotools import mask as maskUtils
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import skimage.io as io
from alfred.utils.log import logger as logging
import cv2
from alfred.vis.image.det import visualize_det_cv2_part
from alfred.vis.image.common import get_unique_color_by_id


# USED_CATEGORIES_IDS = [i for i in range(1, 16)]


def vis_coco(coco_img_root, ann_f):
    data_dir = coco_img_root
    coco = COCO(ann_f)

    cats = coco.loadCats(coco.getCatIds())
    logging.info('cats: {}'.format(cats))
    img_ids = coco.getImgIds()
    logging.info('all images we got: {}'.format(len(img_ids)))

    # draw instances
    for img_id in img_ids:
        img = coco.loadImgs(img_id)[0]
        print('checking img: {}, id: {}'.format(img, img_id))

        img_f = os.path.join(data_dir, img['file_name'])
        anno_ids = coco.getAnnIds(imgIds=img['id'])
        annos = coco.loadAnns(anno_ids)

        logging.info('showing anno: {}'.format(annos))
        if len(annos[0]['segmentation']) == 0:
            logging.info('no segmentation found, using opencv vis.')
            img = cv2.imread(img_f)

            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.36
            font_thickness = 1
            line_thickness = 1

            for ann in annos:
                b = ann['bbox']
                x1 = int(b[0])
                y1 = int(b[1])
                x2 = int(x1 + b[2])
                y2 = int(y1 + b[3])
                cls_id = ann['category_id']
                unique_color = get_unique_color_by_id(cls_id)
                cv2.rectangle(img, (x1, y1), (x2, y2),
                              unique_color, line_thickness, cv2.LINE_AA)
                text_label = '{}'.format(cls_id)
                (ret_val, _) = cv2.getTextSize(
                    text_label, font, font_scale, font_thickness)
                txt_bottom_left = (x1+4, y1-4)
                cv2.rectangle(img, (txt_bottom_left[0]-4, txt_bottom_left[1] - ret_val[1]-2),
                              (txt_bottom_left[0] + ret_val[0] +
                               2, txt_bottom_left[1]+4),
                              (0, 0, 0), -1)
                cv2.putText(img, text_label, txt_bottom_left, font,
                            font_scale, (237, 237, 237), font_thickness, cv2.LINE_AA)
            cv2.imshow('rr', img)
            cv2.waitKey(0)
        else:
            I = io.imread(img_f)
            plt.imshow(I)
            plt.axis('off')
            coco.showAnns(annos)
            plt.show()


# 导入opencv
import cv2
import numpy as np
from typing import Tuple, List


def calc_center_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    """
    计算两个点的距离
    :param p1: 点1
    :param p2: 点2
    :return: 距离
    """
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def is_center_too_close_to(points_list: List[Tuple[int, int]], center: Tuple[int, int], threshold: int = 10) -> bool:
    """
    判断 center 是否和 points_list 中的任意一个点太近，用于过滤重复识别的点
    :param points_list: 已有的点列表
    :param center: 新的点
    :param threshold: 阈值
    :return: 是否太近
    """
    for p in points_list:
        if calc_center_distance(p, center) < threshold:
            return True
    return False


def find_match_points(img_entire: np.ndarray, img_gray: np.ndarray) -> List[Tuple[int, int]]:


    # match many object on image

    threshorld = 0.8
    res =cv2.matchTemplate(image=img_gray,
                           templ=img_entire,
                           method=cv2.TM_CCOEFF_NORMED,
                           )

    # loc = (array([150, 200]), array([100, 300])) 表示两个匹配点的坐标分别是 (150, 100) 和 (200, 300)。
    loc = np.where(res>=threshorld)

    match_points = []
    for points in zip(*loc[::-1]):
    # points 将会是 (100, 150) 和 (300, 200)，因为 loc 被反转且解包给 zip
        center = (points[0] + img_gray.shape[1] // 2, points[1] + img_gray.shape[0] // 2)
        if is_center_too_close_to(match_points, center):
            continue
        else:
            match_points.append(center)
    #         cv2.rectangle(img_entire, points, (points[0] + img_gray.shape[1], points[1] + img_gray.shape[0]),
    #                       (0, 255, 0), 2)
    #
    #
    # cv2.imwrite('./imgs/output.png', img_entire)

    return match_points

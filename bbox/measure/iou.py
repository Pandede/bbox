import math

from ..bbox import BoundingBox
from ..transform import smallest_enclosing
from .area import intersect, union


def iou(bbox1: BoundingBox, bbox2: BoundingBox) -> float:
    """
    Compute IoU score of bounding boxes.

    Args:
        bbox1 (BoundingBox): The predict bounding box.
        bbox2 (BoundingBox): The groundtruth bounding box.

    Returns:
        float: The IoU score
    """
    # Compute the intersection area
    inter_area = intersect(bbox1, bbox2)

    # Compute IoU score
    score = inter_area / (bbox1.area + bbox2.area - inter_area + 1e-7)

    return score


def giou(bbox1: BoundingBox, bbox2: BoundingBox) -> float:
    """
    Compute GIoU score of bounding boxes.

    Args:
        bbox1 (BoundingBox): The predict bounding box.
        bbox2 (BoundingBox): The groundtruth bounding box.

    Returns:
        float: the GIoU score
    """
    iou_score = iou(bbox1, bbox2)
    union_area = union(bbox1, bbox2)
    se_area = smallest_enclosing(bbox1, bbox2).area

    # Compute GIOU
    score = iou_score - (se_area - union_area) / se_area

    return score


def diou(bbox1: BoundingBox, bbox2: BoundingBox) -> float:
    """
    Compute DIoU score of bounding boxes.

    Args:
        bbox1 (BoundingBox): The predict bounding box.
        bbox2 (BoundingBox): The groundtruth bounding box.

    Returns:
        float: the DIoU score
    """
    iou_score = iou(bbox1, bbox2)

    # Compute the L2-distance of the center points
    center_dist = (bbox1.x - bbox2.x) ** 2 + (bbox1.y - bbox2.y) ** 2

    # Compute the L2-distance of the diagonal points in the smallest enclosing bounding box
    sx1, sy1, sx2, sy2 = smallest_enclosing(bbox1, bbox2).to_xyxy()
    se_dist = (sx1 - sx2) ** 2 + (sy1 - sy2) ** 2

    return iou_score - center_dist / se_dist


def ciou(bbox1: BoundingBox, bbox2: BoundingBox) -> float:
    """
    Compute CIoU score of bounding boxes.

    Args:
        bbox1 (BoundingBox): The predict bounding box.
        bbox2 (BoundingBox): The groundtruth bounding box.

    Returns:
        float: the CIoU score
    """
    iou_score = iou(bbox1, bbox2)
    diou_score = diou(bbox1, bbox2)

    # Compute v
    # 4 / (math.pi ** 2) = 0.4052847345693511
    v = 0.4052847345693511 * (math.atan(bbox1.w / bbox1.h) - math.atan(bbox2.w / bbox2.h)) ** 2

    # Compute alpha
    alpha = v / (1 - iou_score + v)

    return diou_score - alpha * v

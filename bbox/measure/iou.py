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

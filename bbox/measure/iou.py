from ..bbox import BoundingBox


def iou(bbox1: BoundingBox, bbox2: BoundingBox) -> float:
    """
    Compute IoU score of bounding boxes.

    Args:
        bbox1 (BoundingBox): The predict bounding box.
        bbox2 (BoundingBox): The groundtruth bounding box.

    Returns:
        float: the IoU score
    """
    x1, y1, x2, y2 = bbox1.to_xyxy()
    a1, b1, a2, b2 = bbox2.to_xyxy()

    # Compute the coordinate of top-left point and bottom-right point of the overlapping
    overlap_x1 = max(x1, a1)
    overlap_y1 = max(y1, b1)
    overlap_x2 = min(x2, a2)
    overlap_y2 = min(y2, b2)

    # Compute the overlapped area
    overlap_area = max(0, overlap_x2 - overlap_x1) * max(0, overlap_y2 - overlap_y1)

    # Compute the area of the overlapped area
    score = overlap_area / (bbox1.area + bbox2.area - overlap_area + 1e-7)

    return score
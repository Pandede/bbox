from ..bbox import BoundingBox


def intersect(bbox1: BoundingBox, bbox2: BoundingBox) -> int:
    """
    Compute the intersection area of bounding boxes.

    Args:
        bbox1 (BoundingBox): The first bounding box.
        bbox2 (BoundingBox): The second bounding box.

    Returns:
        int: The intersection area.
    """
    x1, y1, x2, y2 = bbox1.to_xyxy()
    a1, b1, a2, b2 = bbox2.to_xyxy()

    # Compute the coordinate of top-left point and bottom-right point of the overlapping
    overlap_x1 = max(x1, a1)
    overlap_y1 = max(y1, b1)
    overlap_x2 = min(x2, a2)
    overlap_y2 = min(y2, b2)

    if overlap_x2 - overlap_x1 <= 0 or overlap_y2 - overlap_y1 <= 0:
        return 0
    else:
        return (overlap_x2 - overlap_x1) * (overlap_y2 - overlap_y1)


def union(bbox1: BoundingBox, bbox2: BoundingBox) -> int:
    """
    Compute the union area of bounding boxes.

    Args:
        bbox1 (BoundingBox): The first bounding box.
        bbox2 (BoundingBox): The second bounding box.

    Returns:
        int: The union area.
    """
    inter = intersect(bbox1, bbox2)
    return bbox1.area + bbox2.area - inter

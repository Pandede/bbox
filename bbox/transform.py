from .bbox import BoundingBox


def union(bbox1: BoundingBox, bbox2: BoundingBox) -> BoundingBox:
    """
    Create a bounding box for enclosing the given bounding boxes.

    Args:
        bbox1 (BoundingBox): The first bounding box.
        bbox2 (BoundingBox): The second bounding box.

    Returns:
        BoundingBox: The minimum enclosing bounding box.
    """
    x1, y1, x2, y2 = bbox1.to_xyxy()
    a1, b1, a2, b2 = bbox2.to_xyxy()

    return BoundingBox.from_xyxy(min(x1, a1), min(y1, b1), max(x2, a2), max(y2, b2))


def intersect(bbox1: BoundingBox, bbox2: BoundingBox) -> BoundingBox:
    """
    Create a bounding box of their intersection.

    If there is no intersection, returns a bounding box with XYWH `((bbox1.x + bbox2.x) / 2, (bbox1.y + bbox2.y) / 2), 0, 0`.

    Args:
        bbox1 (BoundingBox): The first bounding box.
        bbox2 (BoundingBox): The second bounding box.

    Returns:
        BoundingBox: The intersecting bounding box.
    """
    x1, y1, x2, y2 = bbox1.to_xyxy()
    a1, b1, a2, b2 = bbox2.to_xyxy()

    # Compute the coordinate of top-left point and bottom-right point of the overlapping
    overlap_x1 = max(x1, a1)
    overlap_y1 = max(y1, b1)
    overlap_x2 = min(x2, a2)
    overlap_y2 = min(y2, b2)

    if overlap_x2 - overlap_x1 <= 0 or overlap_y2 - overlap_y1 <= 0:
        cx = (bbox1.x + bbox2.x) // 2
        cy = (bbox1.y + bbox2.y) // 2
        return BoundingBox(x=cx, y=cy, w=0, h=0)
    else:
        return BoundingBox.from_xyxy(max(x1, a1), max(y1, b1), min(x2, a2), min(y2, b2))

from .bbox import BoundingBox


def smallest_enclosing(bbox1: BoundingBox, bbox2: BoundingBox) -> BoundingBox:
    """
    Create a bounding box of their smallest enclosing area.

    Args:
        bbox1 (BoundingBox): The first bounding box.
        bbox2 (BoundingBox): The second bounding box.

    Returns:
        BoundingBox: The smallest enclosing bounding box.
    """
    x1, y1, x2, y2 = bbox1.to_xyxy()
    a1, b1, a2, b2 = bbox2.to_xyxy()

    return BoundingBox.from_xyxy(min(x1, a1), min(y1, b1), max(x2, a2), max(y2, b2))


bound = smallest_enclosing

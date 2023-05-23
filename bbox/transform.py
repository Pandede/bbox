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


def scaling(bbox: BoundingBox, top: float = 1.0, bottom: float = 1.0, left: float = 1.0, right: float = 1.0) -> BoundingBox:
    """
    Scaling the bounding box along the single direction.

    Args:
        bbox (BoundingBox): The bounding box to be resized.
        top (float, optional): The scaling ratio along the top edge. Defaults to 1.0.
        bottom (float, optional): The scaling ratio along the bottom edge. Defaults to 1.0.
        left (float, optional): The scaling ratio along the left edge. Defaults to 1.0.
        right (float, optional): The scaling ratio along the right edge. Defaults to 1.0.

    Returns:
        BoundingBox: The resized bounding box.
    """
    assert top >= 0, 'scale top cannot be negative'
    assert bottom >= 0, 'scale bottom cannot be negative'
    assert left >= 0, 'scale left cannot be negative'
    assert right >= 0, 'scale right cannot be negative'

    dw, dh = bbox.w // 2, bbox.h // 2
    return BoundingBox.from_xyxy(
        bbox.x - dw * left,
        bbox.y - dh * top,
        bbox.x + dw * right,
        bbox.y + dh * bottom
    )


def scaling_all(bbox: BoundingBox, scale: float = 1.0) -> BoundingBox:
    """
    Scaling the bounding box according to the ratio.

    Args:
        bbox (BoundingBox): The bounding box to be resized.
        scale (float, optional): The scaling ratio. Defaults to 1.0.

    Returns:
        BoundingBox: The resized bounding box.
    """
    assert scale >= 0, 'scale cannot be negative'
    return scaling(bbox, top=scale, bottom=scale, left=scale, right=scale)

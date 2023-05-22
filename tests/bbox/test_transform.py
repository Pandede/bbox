from typing import Tuple

import pytest

from bbox import BoundingBox
from bbox.transform import bound, smallest_enclosing

XYXY = Tuple[int, int, int, int]


@pytest.mark.parametrize(
    'xyxy1,xyxy2,se_xyxy', (
        ((0, 0, 10, 10), (20, 20, 30, 30), (0, 0, 30, 30)),
        ((0, 0, 10, 10), (0, 0, 10, 10), (0, 0, 10, 10)),
        ((0, 0, 10, 10), (5, 5, 15, 15), (0, 0, 15, 15)),
        ((0, 0, 20, 20), (5, 5, 15, 15), (0, 0, 20, 20)),
        ((0, 10, 10, 20), (10, 0, 20, 10), (0, 0, 20, 20))
    )
)
def test_smallest_enclosing(xyxy1: XYXY, xyxy2: XYXY, se_xyxy: XYXY):
    bbox1 = BoundingBox.from_xyxy(*xyxy1)
    bbox2 = BoundingBox.from_xyxy(*xyxy2)
    se_bbox = BoundingBox.from_xyxy(*se_xyxy)
    assert smallest_enclosing(bbox1, bbox2) == bound(bbox1, bbox2) == se_bbox

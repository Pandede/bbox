from typing import Tuple

import pytest

from bbox import BoundingBox
from bbox.measure.iou import intersect, union

XYXY = Tuple[int, int, int, int]


@pytest.mark.parametrize(
    'xyxy1,xyxy2,union_area', (
        ((0, 0, 10, 10), (20, 20, 30, 30), 200),
        ((0, 0, 10, 10), (0, 0, 10, 10), 100),
        ((0, 0, 10, 10), (5, 5, 15, 15), 175),
        ((0, 0, 20, 20), (5, 5, 15, 15), 400),
        ((0, 10, 10, 20), (10, 0, 20, 10), 200)
    )
)
def test_union(xyxy1: XYXY, xyxy2: XYXY, union_area: float):
    bbox1 = BoundingBox.from_xyxy(*xyxy1)
    bbox2 = BoundingBox.from_xyxy(*xyxy2)
    assert union(bbox1, bbox2) == union_area


@pytest.mark.parametrize(
    'xyxy1,xyxy2,inter_area', (
        ((0, 0, 10, 10), (20, 20, 30, 30), 0),
        ((0, 0, 10, 10), (0, 0, 10, 10), 100),
        ((0, 0, 10, 10), (5, 5, 15, 15), 25),
        ((0, 0, 20, 20), (5, 5, 15, 15), 100),
        ((0, 10, 10, 20), (10, 0, 20, 10), 0.0)
    )
)
def test_intersect(xyxy1: XYXY, xyxy2: XYXY, inter_area: float):
    bbox1 = BoundingBox.from_xyxy(*xyxy1)
    bbox2 = BoundingBox.from_xyxy(*xyxy2)
    assert intersect(bbox1, bbox2) == inter_area

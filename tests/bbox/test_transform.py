from typing import Tuple

import pytest

from bbox import BoundingBox
from bbox.transform import union, intersect

XYXY = Tuple[int, int, int, int]


@pytest.mark.parametrize(
    'xyxy1,xyxy2,union_xyxy', (
        ((0, 0, 10, 10), (20, 20, 30, 30), (0, 0, 30, 30)),
        ((0, 0, 10, 10), (0, 0, 10, 10), (0, 0, 10, 10)),
        ((0, 0, 10, 10), (5, 5, 15, 15), (0, 0, 15, 15)),
        ((0, 0, 20, 20), (5, 5, 15, 15), (0, 0, 20, 20)),
        ((0, 10, 10, 20), (10, 0, 20, 10), (0, 0, 20, 20))
    )
)
def test_union(xyxy1: XYXY, xyxy2: XYXY, union_xyxy: XYXY):
    bbox1 = BoundingBox.from_xyxy(*xyxy1)
    bbox2 = BoundingBox.from_xyxy(*xyxy2)
    union_bbox = BoundingBox.from_xyxy(*union_xyxy)
    assert union(bbox1, bbox2) == union_bbox


@pytest.mark.parametrize(
    'xyxy1,xyxy2,inter_xyxy', (
        ((0, 0, 10, 10), (20, 20, 30, 30), (15, 15, 15, 15)),
        ((0, 0, 10, 10), (0, 0, 10, 10), (0, 0, 10, 10)),
        ((0, 0, 10, 10), (5, 5, 15, 15), (5, 5, 10, 10)),
        ((0, 0, 20, 20), (5, 5, 15, 15), (5, 5, 15, 15)),
        ((0, 10, 10, 20), (10, 0, 20, 10), (10, 10, 10, 10))
    )
)
def test_intersect(xyxy1: XYXY, xyxy2: XYXY, inter_xyxy: XYXY):
    bbox1 = BoundingBox.from_xyxy(*xyxy1)
    bbox2 = BoundingBox.from_xyxy(*xyxy2)
    inter_bbox = BoundingBox.from_xyxy(*inter_xyxy)
    assert intersect(bbox1, bbox2) == inter_bbox

from typing import Tuple

import pytest

from bbox import BoundingBox
from bbox.transform import bound, scaling, scaling_all, smallest_enclosing

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


@pytest.mark.parametrize(
    'xyxy,top,bottom,left,right,scale_xyxy', (
        ((0, 0, 100, 100), 1.0, 1.0, 1.0, 1.0, (0, 0, 100, 100)),
        ((0, 0, 100, 100), 1.2, 1.0, 1.0, 1.0, (0, -10, 100, 100)),
        ((0, 0, 100, 100), 1.0, 1.2, 1.0, 1.0, (0, 0, 100, 110)),
        ((0, 0, 100, 100), 1.0, 1.0, 1.2, 1.0, (-10, 0, 100, 100)),
        ((0, 0, 100, 100), 1.0, 1.0, 1.0, 1.2, (0, 0, 110, 100)),
        ((0, 0, 100, 100), 1.2, 1.2, 1.2, 1.2, (-10, -10, 110, 110)),
        ((0, 0, 100, 100), 0.8, 1.0, 1.0, 1.0, (0, 10, 100, 100)),
        ((0, 0, 100, 100), 1.0, 0.8, 1.0, 1.0, (0, 0, 100, 90)),
        ((0, 0, 100, 100), 1.0, 1.0, 0.8, 1.0, (10, 0, 100, 100)),
        ((0, 0, 100, 100), 1.0, 1.0, 1.0, 0.8, (0, 0, 90, 100)),
        ((0, 0, 100, 100), 0.8, 0.8, 0.8, 0.8, (10, 10, 90, 90))
    )
)
def test_scaling(xyxy: XYXY, top: float, bottom: float, left: float, right: float, scale_xyxy: XYXY):
    bbox = BoundingBox.from_xyxy(*xyxy)
    scale_bbox = BoundingBox.from_xyxy(*scale_xyxy)
    assert scaling(bbox, top, bottom, left, right) == scale_bbox


def test_scaling_with_negative_scale():
    bbox = BoundingBox.from_xyxy(0, 0, 100, 100)
    with pytest.raises(AssertionError, match='scale top cannot be negative'):
        scaling(bbox, top=-0.1)
    with pytest.raises(AssertionError, match='scale bottom cannot be negative'):
        scaling(bbox, bottom=-0.1)
    with pytest.raises(AssertionError, match='scale left cannot be negative'):
        scaling(bbox, left=-0.1)
    with pytest.raises(AssertionError, match='scale right cannot be negative'):
        scaling(bbox, right=-0.1)


@pytest.mark.parametrize(
    'xyxy,scale,scale_xyxy', (
        ((0, 0, 100, 100), 1.0, (0, 0, 100, 100)),
        ((0, 0, 100, 100), 1.2, (-10, -10, 110, 110)),
        ((0, 0, 100, 100), 0.8, (10, 10, 90, 90)),
    )
)
def test_scaling_all(xyxy: XYXY, scale: float, scale_xyxy: XYXY):
    bbox = BoundingBox.from_xyxy(*xyxy)
    scale_bbox = BoundingBox.from_xyxy(*scale_xyxy)
    assert scaling_all(bbox, scale) == scale_bbox


def test_scaling_all_with_negative_scale():
    bbox = BoundingBox.from_xyxy(0, 0, 100, 100)
    with pytest.raises(AssertionError, match='scale cannot be negative'):
        scaling_all(bbox, scale=-0.1)

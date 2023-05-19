from typing import Tuple

import pytest

from bbox import BoundingBox
from bbox.measure.iou import giou, iou

XYXY = Tuple[int, int, int, int]


@pytest.mark.parametrize(
    'xyxy1,xyxy2,score', (
        ((0, 0, 10, 10), (20, 20, 30, 30), 0.0),
        ((0, 0, 10, 10), (0, 0, 10, 10), 1.0),
        ((0, 0, 10, 10), (5, 5, 15, 15), 0.142857),
        ((0, 0, 20, 20), (5, 5, 15, 15), 0.25),
        ((0, 0, 10, 10), (10, 10, 20, 20), 0.0)
    )
)
def test_iou(xyxy1: XYXY, xyxy2: XYXY, score: float):
    bbox1 = BoundingBox.from_xyxy(*xyxy1)
    bbox2 = BoundingBox.from_xyxy(*xyxy2)
    assert iou(bbox1, bbox2) == pytest.approx(score)


@pytest.mark.parametrize(
    'xyxy1,xyxy2,score', (
        ((0, 0, 10, 10), (20, 20, 30, 30), -1.0),
        ((0, 0, 10, 10), (0, 0, 10, 10), 1.0),
        ((0, 0, 10, 10), (5, 5, 15, 15), -0.746032),
        ((0, 0, 20, 20), (5, 5, 15, 15), -0.5),
        ((0, 0, 10, 10), (10, 10, 20, 20), -1.0)
    )
)
def test_giou(xyxy1: XYXY, xyxy2: XYXY, score: float):
    bbox1 = BoundingBox.from_xyxy(*xyxy1)
    bbox2 = BoundingBox.from_xyxy(*xyxy2)
    assert giou(bbox1, bbox2) == pytest.approx(score)

from typing import Tuple

import pytest

from bbox import BoundingBox
from bbox.measure.iou import giou, iou, diou

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
        ((0, 0, 10, 10), (20, 20, 30, 30), -0.777778),
        ((0, 0, 10, 10), (0, 0, 10, 10), 1.0),
        ((0, 0, 10, 10), (5, 5, 15, 15), -0.0793651),
        ((0, 0, 20, 20), (5, 5, 15, 15), 0.25),
        ((0, 0, 10, 10), (10, 10, 20, 20), -0.5)
    )
)
def test_giou(xyxy1: XYXY, xyxy2: XYXY, score: float):
    bbox1 = BoundingBox.from_xyxy(*xyxy1)
    bbox2 = BoundingBox.from_xyxy(*xyxy2)
    assert giou(bbox1, bbox2) == pytest.approx(score)


@pytest.mark.parametrize(
    'xyxy1,xyxy2,score', (
        ((0, 0, 10, 10), (20, 20, 30, 30), -0.4444444),
        ((0, 0, 10, 10), (0, 0, 10, 10), 1.0),
        ((0, 0, 10, 10), (5, 5, 15, 15), 0.01530612),
        ((0, 0, 20, 20), (5, 5, 15, 15), 0.25),
        ((0, 0, 10, 10), (10, 10, 20, 20), -0.25)
    )
)
def test_diou(xyxy1: XYXY, xyxy2: XYXY, score: float):
    bbox1 = BoundingBox.from_xyxy(*xyxy1)
    bbox2 = BoundingBox.from_xyxy(*xyxy2)
    assert diou(bbox1, bbox2) == pytest.approx(score)

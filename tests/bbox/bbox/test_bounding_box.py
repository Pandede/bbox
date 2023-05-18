import pytest

from bbox import BoundingBox


class TestBoundingBox:
    @pytest.mark.parametrize(
        'x,y,w,h', (
            # Normal
            (10, 10, 10, 10),
            # Zero
            (0, 10, 10, 10),
            (10, 0, 10, 10),
            (10, 10, 0, 10),
            (10, 10, 10, 0),
            (0, 0, 0, 0),
            # Negative
            (-1, 10, 10, 10),
            (10, -1, 10, 10),
            (-1, -1, 10, 10)
        )
    )
    def test_init(self, x: int, y: int, w: int, h: int):
        BoundingBox(x=x, y=y, w=w, h=h)

    def test_init_with_negative_width(self):
        with pytest.raises(ValueError):
            BoundingBox(x=0, y=0, w=-1, h=0)

    def test_init_with_negative_height(self):
        with pytest.raises(ValueError):
            BoundingBox(x=0, y=0, w=0, h=-1)

    @pytest.mark.parametrize(
        'x1,y1,x2,y2,x,y,w,h', (
            # Normal
            (0, 0, 10, 10, 5, 5, 10, 10),
            # Rearrange points
            (10, 10, 0, 0, 5, 5, 10, 10),
            (0, 10, 10, 0, 5, 5, 10, 10),
            (10, 0, 0, 10, 5, 5, 10, 10),
            # Negative
            (-10, -10, -20, -20, -15, -15, 10, 10),
            # Zero
            (10, 10, 10, 20, 10, 15, 0, 10),
            (10, 20, 20, 20, 15, 20, 10, 0),
            (10, 10, 10, 10, 10, 10, 0, 0)
        )
    )
    def test_from_xyxy(self, x1: int, y1: int, x2: int, y2: int, x: int, y: int, w: int, h: int):
        bbox = BoundingBox.from_xyxy(x1, y1, x2, y2)
        assert bbox.x == x
        assert bbox.y == y
        assert bbox.w == w
        assert bbox.h == h

    @pytest.mark.parametrize(
        't,l,w,h,x,y,w_,h_', (
            # Normal
            (0, 0, 10, 10, 5, 5, 10, 10),
            # Negative
            (-10, -10, 10, 10, -5, -5, 10, 10),
            # Zero
            (10, 10, 10, 0, 15, 10, 10, 0),
            (10, 10, 0, 10, 10, 15, 0, 10),
        )
    )
    def test_from_tlwh(self, t: int, l: int, w: int, h: int, x: int, y: int, w_: int, h_: int):
        bbox = BoundingBox.from_tlwh(t, l, w, h)
        assert bbox.x == x
        assert bbox.y == y
        assert bbox.w == w_
        assert bbox.h == h_

    def test_width(self):
        bbox = BoundingBox(x=0, y=0, w=10, h=10)
        assert bbox.width == 10

    def test_height(self):
        bbox = BoundingBox(x=0, y=0, w=10, h=10)
        assert bbox.height == 10

    @pytest.mark.parametrize(
        'w,h,area', (
            (10, 10, 100),
            (0, 0, 0),
            (0, 100, 0),
            (100, 0, 0)
        )
    )
    def test_area(self, w: int, h: int, area: int):
        assert BoundingBox(x=0, y=0, w=w, h=h).area == area

    def test_eq(self):
        target = BoundingBox(x=0, y=1, w=2, h=3)
        assert target == BoundingBox(x=0, y=1, w=2, h=3)
        assert target != BoundingBox(x=1, y=1, w=2, h=3)
        assert target != BoundingBox(x=0, y=2, w=2, h=3)
        assert target != BoundingBox(x=0, y=1, w=3, h=3)
        assert target != BoundingBox(x=0, y=1, w=2, h=4)

    def test_anchor(self):
        bbox = BoundingBox(x=0, y=0, w=10, h=10)
        assert bbox.anchor(1) == (-5, 5)
        assert bbox.anchor(2) == (0, 5)
        assert bbox.anchor(3) == (5, 5)
        assert bbox.anchor(4) == (-5, 0)
        assert bbox.anchor(5) == (0, 0)
        assert bbox.anchor(6) == (5, 0)
        assert bbox.anchor(7) == (-5, -5)
        assert bbox.anchor(8) == (0, -5)
        assert bbox.anchor(9) == (5, -5)

    def test_anchor_with_invalid_index(self):
        bbox = BoundingBox(x=0, y=0, w=10, h=10)
        with pytest.raises(IndexError, match='expected index between 1 to 9, got 10'):
            bbox.anchor(10)
        with pytest.raises(IndexError, match='expected index between 1 to 9, got 0'):
            bbox.anchor(0)

    @pytest.mark.parametrize(
        'x1,y1,x2,y2,x,y,w,h', (
            # Normal
            (0, 0, 10, 10, 5, 5, 10, 10),
            # Negative
            (-20, -20, -10, -10, -15, -15, 10, 10),
            # Zero
            (10, 10, 10, 20, 10, 15, 0, 10),
            (10, 20, 20, 20, 15, 20, 10, 0),
            (10, 10, 10, 10, 10, 10, 0, 0)
        )
    )
    def test_to_xyxy(self, x1: int, y1: int, x2: int, y2: int, x: int, y: int, w: int, h: int):
        assert BoundingBox(x=x, y=y, w=w, h=h).to_xyxy() == (x1, y1, x2, y2)

    @pytest.mark.parametrize(
        't,l,w,h,x,y,w_,h_', (
            # Normal
            (0, 0, 10, 10, 5, 5, 10, 10),
            # Negative
            (-10, -10, 10, 10, -5, -5, 10, 10),
            # Zero
            (10, 10, 10, 0, 15, 10, 10, 0),
            (10, 10, 0, 10, 10, 15, 0, 10),
        )
    )
    def test_to_tlwh(self, t: int, l: int, w: int, h: int, x: int, y: int, w_: int, h_: int):
        assert BoundingBox(x=x, y=y, w=w, h=h).to_tlwh() == (t, l, w, h)

from typing import Tuple

from pydantic import BaseModel, NonNegativeInt


class BoundingBox(BaseModel):
    """
    A base class for handling the bounding box

    Attributes:
        x (int): The x-coordinate of the center point of the bounding box.
        y (int): The y-coordinate of the center point of the bounding box.
        w (int): The width of the bounding box. Raises error if it is negative.
        h (int): The height of the bounding box. Raises error if it is negative.
    """
    x: int
    y: int
    w: NonNegativeInt
    h: NonNegativeInt

    @classmethod
    def from_xyxy(cls, x1: int, y1: int, x2: int, y2: int) -> 'BoundingBox':
        """
        Initialize a bounding box with pair of diagonal points.

        Args:
            x1 (int): The x-coordinate of the first point.
            y1 (int): The y-coordinate of the first point.
            x2 (int): The x-coordinate of the second point.
            y2 (int): The y-coordinate of the second point.

        Returns:
            BoundingBox: The corresponding bounding box.

        Examples:
            Create a bounding box with diagonal points:
            >>> bbox_a = BoundingBox.from_xyxy(0, 0, 10, 10)
            >>> bbox_a
            BoundingBox(x=5, y=5, w=10, h=10)

            All of them are identical:
            >>> bbox_a = BoundingBox.from_xyxy(0, 0, 10, 10)
            >>> bbox_b = BoundingBox.from_xyxy(10, 10, 0, 0)
            >>> bbox_c = BoundingBox.from_xyxy(0, 10, 10, 0)
            >>> bbox_d = BoundingBox.from_xyxy(10, 0, 0, 10)
            >>> bbox_a == bbox_b == bbox_c == bbox_d
            True

        """
        # Make sure (x1, y1) is at top-left and (x2, y2) is at bottom-right
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1

        w = x2 - x1
        h = y2 - y1
        x = x1 + w // 2
        y = y1 + h // 2
        return cls(x=x, y=y, w=w, h=h)

    @classmethod
    def from_tlwh(cls, t: int, l: int, w: int, h: int) -> 'BoundingBox':
        """
        Initialize a bounding box with top-left point, width and height.

        Args:
            t (int): The y-coordinate of the top-left point. Equivalent to `y1`.
            l (int): The x-coordinate of the top-left point. Equivalent to `x1`.
            w (int): The width of the bounding box. Raises error if it is negative.
            h (int): The height of the bounding box. Raises error if it is negative.

        Returns:
            BoundingBox: The corresponding bounding box.
        """
        x = l + w // 2
        y = t + h // 2
        return cls(x=x, y=y, w=w, h=h)

    @property
    def width(self) -> int:
        """
        The width of the bounding box.
        """
        return self.w

    @property
    def height(self) -> int:
        """
        The height of the bounding box.
        """
        return self.h

    @property
    def area(self) -> int:
        """
        The area of the bounding box.
        """
        return self.w * self.h

    def __eq__(self, bbox: 'BoundingBox') -> bool:
        """
        Determines whether the bounding boxes are identical.

        Args:
            bbox (BoundingBox): The another bounding box.

        Returns:
            bool: `True` if they are identical else `False`
        """
        if self.x != bbox.x:
            return False
        if self.y != bbox.y:
            return False
        if self.w != bbox.w:
            return False
        if self.h != bbox.h:
            return False
        return True

    def anchor(self, index: int) -> Tuple[int, int]:
        """
        Get the edge point of the bounding box.

        The value of `index` can refer to the number position on numpad.

        Args:
            index (int): The corresponding number for the pointed position.

        Raises:
            IndexError: If the index is not between 1 to 9.

        Returns:
            Tuple[int, int]: The xy-coordinate of the corresponding point.

        Examples:
            >>> bbox = BoundingBox(x=5, y=5, w=10, h=10)

            Assign `index=1` to get the bottom-left point:
            >>> bbox.anchor(1)
            (0, 10)

            Assign `index=5` to get the center point:
            >>> bbox.anchor(5)
            (5, 5)

            Raises `IndexError` if the index is invalid:
            >>> bbox.anchor(10)
            Traceback (most recent call last):
            ...
            IndexError: expected index between 1 to 9, got 10
        """
        dw = self.w // 2
        dh = self.h // 2
        if index == 1:
            return self.x - dw, self.y + dh
        elif index == 2:
            return self.x, self.y + dh
        elif index == 3:
            return self.x + dw, self.y + dh
        elif index == 4:
            return self.x - dw, self.y
        elif index == 5:
            return self.x, self.y
        elif index == 6:
            return self.x + dw, self.y
        elif index == 7:
            return self.x - dw, self.y - dh
        elif index == 8:
            return self.x, self.y - dh
        elif index == 9:
            return self.x + dw, self.y - dh
        else:
            raise IndexError(f'expected index between 1 to 9, got {index}')

    def to_xyxy(self) -> Tuple[int, int, int, int]:
        """
        Format the bounding box in tuple of `(x1, y1, x2, y2)`

        Returns:
            Tuple[int, int, int, int]: The tuple in format `(x1, y1, x2, y2)`
        """
        return self.anchor(7) + self.anchor(3)

    def to_tlwh(self) -> Tuple[int, int, int, int]:
        """
        Format the bounding box in tuple of `(t, l, w, h)`

        Returns:
            Tuple[int, int, int, int]: The tuple in format `(t, l, w, h)`
        """
        return self.anchor(7) + (self.w, self.h)

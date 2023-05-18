# bbox

Dealing with the bounding box is pretty common and important in the related tasks of object detection or tracking, such as `Yolo` and `Deepsort`. Handling with `bbox` can greatly reduce the development time and reduce the chance of errors on bounding box.

## Quick start
### Basic operations
```python
from bbox import BoundingBox

# Create a bounding box in format `xywh`
bbox = BoundingBox(x=0, y=0, w=10, h=10)

# ... or in format `xyxy`
bbox = BoundingBox.from_xyxy(0, 0, 10, 10)

# ... or in format `tlwh`
bbox = BoundingBox.from_tlwh(0, 0, 10, 10)

# Get the width and height
print(bbox.width, bbox.height)  # 10 10

# ... or in short form
w, h = bbox.w, bbox.h   # 10 10

# Get the area
print(bbox.area)    # 100

# Check if the bounding boxes are identical
bbox_a = BoundingBox(x=0, y=0, w=10, h=10)
bbox_b = BoundingBox.from_xyxy(-5, -5, 5, 5)
print(bbox_a == bbox_a) # True
```

### Anchor
```python
from bbox import BoundingBox

# Get the coordinate of edge point by calling `anchor(index)`
# The returned point refers to the position of number on NumPad:
# 7---8---9
# |       |
# 4   5   6
# |       |
# 1---2---3

bbox = BoundingBox.from_xyxy(0, 0, 10, 10)

# Get the coordinate of bottom-left point
print(bbox.anchor(1))   # (0, 10)

# Get the coordinate of center point
print(bbox.anchor(5))   # (5, 5)
```

### Format
```python
from bbox import BoundingBox

# The `BoundingBox` object stores the attributes `xywh`
bbox = BoundingBox(x=5, y=5, w=10, h=10)
print((bbox.x, bbox.y, bbox.w, bbox.h))   # (5, 5, 10, 10)

# Format it to `xyxy`
print(bbox.to_xyxy())   # (0, 0, 10, 10)

# Format it to `tlwh`
print(bbox.to_tlwh())   # (0, 0, 10, 10)
```
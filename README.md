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

## Measurement
### Area
```python
from bbox import BoundingBox
from bbox.measure import union, intersect

bbox_a = BoundingBox.from_xyxy(0, 0, 10, 10)
bbox_b = BoundingBox.from_xyxy(5, 5, 15, 15)

# Get the union area of bounding boxes
print(union(bbox_a, bbox_b))    # 175

# Get the intersection area of bounding boxes
print(intersect(bbox_a, bbox_b))    # 25
```

### IoU (Intersection over Union)
```python
from bbox import BoundingBox
from bbox.measure import iou, giou, diou, ciou

bbox_a = BoundingBox.from_xyxy(0, 0, 10, 10)
bbox_b = BoundingBox.from_xyxy(5, 5, 15, 15)

# Compute the IoU and its variation
print(f'IoU: {iou(bbox_a, bbox_b):.6f}')    # IoU: 0.142857
print(f'GIoU: {giou(bbox_a, bbox_b):.6f}')  # GIoU: -0.079365
print(f'DIoU: {diou(bbox_a, bbox_b):.6f}')  # DIoU: 0.0153061
print(f'CIoU: {ciou(bbox_a, bbox_b):.6f}')  # CIoU: 0.0153061
```
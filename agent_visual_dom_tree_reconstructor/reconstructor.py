"""Reconstructs hierarchical DOM trees from spatial visual bounding elements."""
from typing import Dict, List, Optional, Tuple, Any

class VisualElement:
    def __init__(self, elem_id: str, role: str, x: int, y: int, w: int, h: int, text: str = ""):
        self.elem_id = elem_id
        self.role = role
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.children: List["VisualElement"] = []

    def contains(self, other: "VisualElement") -> bool:
        return (
            self.x <= other.x and
            self.y <= other.y and
            (self.x + self.w) >= (other.x + other.w) and
            (self.y + self.h) >= (other.y + other.h)
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.elem_id,
            "role": self.role,
            "bounds": [self.x, self.y, self.w, self.h],
            "text": self.text,
            "children": [c.to_dict() for c in self.children]
        }

class VisualDOMReconstructor:
    """Builds a hierarchical tree from flat bounding elements using spatial inclusion."""

    @staticmethod
    def build_tree(elements: List[VisualElement]) -> List[VisualElement]:
        # Sort elements by area descending: larger boxes are potential parents
        sorted_elems = sorted(elements, key=lambda e: e.w * e.h, reverse=True)
        root_nodes: List[VisualElement] = []

        for elem in sorted_elems:
            placed = False
            # Try to place inside an existing parent
            for root in root_nodes:
                if root.contains(elem):
                    VisualDOMReconstructor._insert_child(root, elem)
                    placed = True
                    break
            if not placed:
                root_nodes.append(elem)

        return root_nodes

    @staticmethod
    def _insert_child(parent: VisualElement, child: VisualElement):
        for c in parent.children:
            if c.contains(child):
                VisualDOMReconstructor._insert_child(c, child)
                return
        parent.children.append(child)

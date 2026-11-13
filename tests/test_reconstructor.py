"""Unit tests for agent-visual-dom-tree-reconstructor."""
import unittest
from agent_visual_dom_tree_reconstructor.reconstructor import VisualDOMReconstructor, VisualElement

class TestVisualDOM(unittest.TestCase):
    def test_containment_hierarchy(self):
        container = VisualElement("c1", "container", 0, 0, 500, 500)
        child = VisualElement("btn1", "button", 10, 10, 50, 50)
        unrelated = VisualElement("box2", "panel", 600, 0, 100, 100)

        tree = VisualDOMReconstructor.build_tree([child, container, unrelated])
        self.assertEqual(len(tree), 2)  # container and unrelated
        self.assertEqual(len(tree[0].children), 1)
        self.assertEqual(tree[0].children[0].elem_id, "btn1")

if __name__ == "__main__":
    unittest.main()

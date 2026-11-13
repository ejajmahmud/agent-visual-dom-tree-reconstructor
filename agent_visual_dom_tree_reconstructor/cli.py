"""CLI for agent-visual-dom-tree-reconstructor."""
import sys
import argparse
from .reconstructor import VisualDOMReconstructor, VisualElement

def main():
    parser = argparse.ArgumentParser(description="Agent Visual DOM Tree Reconstructor CLI")
    parser.add_argument("--demo", action="store_true", help="Run visual DOM tree reconstruction demo")
    args = parser.parse_args()

    if args.demo:
        window = VisualElement("win", "dialog", 0, 0, 800, 600)
        card = VisualElement("card", "panel", 50, 50, 400, 300)
        btn = VisualElement("btn", "button", 60, 60, 100, 40, text="Submit")
        tree = VisualDOMReconstructor.build_tree([btn, card, window])
        print(f"[+] Reconstructed visual hierarchy: {tree[0].to_dict()}")
    else:
        parser.print_help()
    sys.exit(0)

if __name__ == "__main__":
    main()

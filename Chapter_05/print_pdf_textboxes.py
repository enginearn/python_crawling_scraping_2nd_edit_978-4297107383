#!/usr/bin/env python3

import sys
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTContainer, LTTextBox, LTComponent
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage


def find_textboxes_recursively(component: LTComponent) -> list[LTTextBox]:
    if isinstance(component, LTTextBox):
        return [component]
    if isinstance(component, LTContainer):
        boxes = []
        for child in component:
            boxes.extend(find_textboxes_recursively(child))
        return boxes
    return []


def main():
    """_summary_"""
    laparams = LAParams(detect_vertical=True)
    resource_manager = PDFResourceManager()
    device = PDFPageAggregator(resource_manager, laparams=laparams)
    interpreter = PDFPageInterpreter(resource_manager, device)

    with open(sys.argv[1], "rb") as f:
        for page in PDFPage.get_pages(f):
            interpreter.process_page(page)
            layout = device.get_result()
            boxes = find_textboxes_recursively(layout)
            boxes.sort(key=lambda b: (-b.y1, b.x0))
            for box in boxes:
                print("-" * 20)
                print(box.get_text().split())


if __name__ == "__main__":
    main()
    sys.exit(0)

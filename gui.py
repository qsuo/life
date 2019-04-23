#!/usr/bin/python3.6

import sys

from PySide2.QtWidgets import QApplication, QLabel, QWidget, QGraphicsScene, QGraphicsView
from PySide2.QtWidgets import QPushButton, QHBoxLayout
from PySide2.QtCore import Slot
from PySide2.QtCore import Qt

WIDTH = 1200
HEIGHT = 750


def main():
    app = QApplication(sys.argv)
    
    
        

    scene = QGraphicsScene()
    scene.addText("Hello, world!")
    
    
    #scene.

    view = QGraphicsView(scene)
        
    view.setSceneRect(0, 0, 900, 900)
    button = QPushButton("Run")
    
    scene.setBackgroundBrush(Qt.green)

    layout = QHBoxLayout()
    layout.addWidget(view)
    layout.addWidget(button)
    layout.addStretch(1)

    window = QWidget()
    window.resize(1000, 1000)
    window.setLayout(layout)
    window.setWindowTitle('Simple')

    window.show()
    app.exec_()

if __name__ == '__main__':
    main()



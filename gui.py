#!/usr/bin/python3.6

import sys
import time

from PySide2.QtWidgets import QApplication, QLabel, QWidget, QGraphicsScene, QGraphicsView
from PySide2.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout

from PySide2.QtCore import Slot
from PySide2.QtCore import Qt, QRectF

WIDTH = 1200
HEIGHT = 750


def MainWindow(QWidget):
    def __init__(self, parent=None):


@Slot()
def draw(scene):
    scene.addRect(200, 200, 100, 100, brush=Qt.blue)
    scene.update()

def main():
    app = QApplication(sys.argv)
    
    
        

    scene = QGraphicsScene()
    
    

    #scene.

    view = QGraphicsView(scene)
        
    view.setSceneRect(0, 0, 500, 500)

    size = view.sceneRect()
    print(size.bottomRight())
    print(size.topLeft())
     
    button = QPushButton("Step")
    
    button.clicked.connect(draw) 

    scene.addRect(0, 0, 100, 100, brush=Qt.gray)
    scene.addRect(400, 400, 100, 100, brush=Qt.green)

    layout = QVBoxLayout()
    layout.addWidget(view)
    layout.addWidget(button)
    #layout.addStretch(1)

    window = QWidget()
    window.setLayout(layout)
    #window.resize(500, 500)
    #window.setFixedSize(window.size())

    
    
    
    window.setWindowTitle('Simple')

    window.show()
    
    
    
    app.exec_()
    

    
if __name__ == '__main__':
    main()



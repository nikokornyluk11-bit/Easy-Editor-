from PyQt5 import Qt
from PyQt5.QtWidgets import QApplication,QFileDialog, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout, QInputDialog
from PIL import Image, ImageFilter
import os

app = QApplication([])
win = QWidget()
win.show()
win.resize(900,600)
win.setWindowTitle("Easy Editor")

workdir = ''
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, extensions):
    filenames = []
    for files in filenames:
        for extension in extension:
            if files.endwith(extensions):
                filenames.append(files)
    return filenames

def showFilenameList():
    extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensions)
    list_folder.clear()
    for filename in filenames:
        list_folder.addItem(filename)

def showChosenImage():
    if  list_folder.currentRow() >= 0:
        filename = list_folder.currentItem().text()
        workimage.loadImage(filename)
        image_path = os.path.join(workdir, workimage.filename)
        workimage.showImage(image_path)

class ImageProcessor():
    def __init__(self, cur_image, cur_file, subfolder_name):
        self.cur_image = cur_image
        self.cur_file = cur_file
        self.subfolder_name = subfolder_name
   
    def loadImage(self, filename):
        self.filename = filename
        image_path = os.path.join(workdir, filename)
        self.cur_image = Image.open(image_path)

    def showImage(self, path):
        image_label.hide()
        pixmapimage = QPixmap(path)
        w, h = image_label.width(), image_label.height()
        pixmapimage = pixmapimage.scaled(w, h, KeepAspectRatio)
        image_label.setPixmap(pixmapimage)
        image_label.show()




image_label = QLabel('Image')
folder_button = QPushButton('Folder') 
list_folder = QListWidget()
left_button = QPushButton('Left') 
right_button = QPushButton('Right') 
mirror_button = QPushButton('Mirror') 
sharp_button = QPushButton('Sharpness') 
bw_button = QPushButton('B and W') 

layout_main_V = QHBoxLayout()
layout_h1 = QVBoxLayout()
layout_h2 = QVBoxLayout()

layout_h1.addWidget(folder_button)
layout_h1.addWidget(list_folder)
layout_h2.addWidget(image_label)

layout_button = QHBoxLayout()
layout_button.addWidget(left_button)
layout_button.addWidget(right_button)
layout_button.addWidget(mirror_button)
layout_button.addWidget(sharp_button)
layout_button.addWidget(bw_button)

layout_h2.addLayout(layout_button)
layout_main_V.addLayout(layout_h1)
layout_main_V.addLayout(layout_h2)
win.setLayout(layout_main_V)

folder_button.clicked.connect(showFilenameList)
list_folder.currentRowChanged.connect(showChosenImage)

app.exec_()
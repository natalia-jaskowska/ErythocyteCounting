import sys

import cv2
import numpy as np
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from cell_count import cell_count
from ui_blood_count import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Main GUI class, constructor creates buttons connections and initialize a
    list of intermediate images and current image as zero.
    """

    def __init__(self):
        super().__init__()
        self.intermediateImages = []
        self.currentImage = 0
        self.setupUi(self)

        self.loadButton.clicked.connect(self.loadImage)
        self.nextButton.clicked.connect(self.nextImage)
        self.previousButton.clicked.connect(self.previousImage)

        self.centralWidget().dragEnterEvent = self.dragEnterEvent
        self.centralWidget().dropEvent = self.dropEvent

    def previousImage(self):
        """
        Get previous image and set previous image if intermediate image exists
        """
        self.currentImage = max(0, self.currentImage - 1)
        if len(self.intermediateImages) > 0:
            self.stageLabel.setText(self.intermediateImages[self.currentImage][1])
            self.setImage(self.intermediateImage,
                          self.intermediateImages[self.currentImage][0])

    def nextImage(self):
        """
        Get next image and set next image if intermediate image exists
        """
        self.currentImage = min(len(self.intermediateImages) - 1, self.currentImage + 1)
        if len(self.intermediateImages) > 0:
            self.stageLabel.setText(self.intermediateImages[self.currentImage][1])
            self.setImage(self.intermediateImage,
                          self.intermediateImages[self.currentImage][0])

    def setImage(self, image_widget, img):
        """
        Set an image based on image widget and image. 
        Convert gray scaled image to RGB, check dimensions and set  type (if float type convert to int)
        """
        if img.dtype != np.uint8:
            img = (img.clip(min=0, max=1) * 255).astype(np.uint8)
        if len(img.shape) == 2:
            img = img.reshape(*img.shape, 1)
        if img.shape[2] == 1:
            img = np.concatenate((img, img, img), axis=2)
        img = img.copy()
        height, width, _ = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        image_widget.setPixmap(pixmap)

    def loadAndProcessImage(self, filepath):
        """
        Load an image, if image does not exist set image.
        Process image from BGR to RGB, count cells, set image and load next image.
        """
        self.intermediateImages = []
        self.currentImage = 0

        img = cv2.imread(filepath)

        if img is None:
            self.inputImage.setPixmap(None)
            self.outputImage.setPixmap(None)
            self.intermediateImage.setPixmap(None)
            self.erythrocyteLabel.setText('N/A')
            self.stageLabel.setText('N/A')
        else:
            img = img[:, :, ::-1]
            cc, imgs = cell_count(img)
            self.erythrocyteLabel.setText(str(cc))

            self.intermediateImages = [(img, 'Input image')] + imgs
            self.currentImage = 0

            self.setImage(self.inputImage, img)
            self.setImage(self.outputImage, imgs[-1][0])
            self.nextImage()

    def loadImage(self):
        """
        Open a file dialog and get the selected file's name.
        Load the image from the file and display it in the label.
        """
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open Image', '/')
        if fileName:
            self.loadAndProcessImage(fileName)

    def dragEnterEvent(self, event):
        """
        Drag an event
        """
        event.acceptProposedAction()

    def dropEvent(self, event):
        """
        Load the image from the dropped file and display it in the label
        """
        filePath = event.mimeData().urls()[0].toLocalFile()
        self.loadAndProcessImage(filePath)

    @staticmethod
    def main() -> int:
        app = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        return app.exec_()


if __name__ == '__main__':
    exit(MainWindow.main())

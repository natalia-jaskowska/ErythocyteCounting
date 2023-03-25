from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel


class ResizableLabel(QLabel):
    """
    A class used to resize a label

    Methods
    -------
    setPixmap(pixelmap)
        if pixmap exists then set scaled pixmap
        
    resizeEvent(event)
        if orig pixmap exists then set pixmap and return resize event
    """

    def __init__(self, *a, **k):
        self.origPixelMap = None
        QLabel.__init__(self, *a, **k)
        self.setMinimumSize(1, 1)
        self.setScaledContents(False)

    def setPixmap(self, pixelmap):
        self.origPixelMap = pixelmap
        if pixelmap is not None:
            w, h = self.width(), self.height()
            super().setPixmap(self.origPixelMap.scaled(w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def resizeEvent(self, event):
        if self.origPixelMap is not None:
            w, h = self.width(), self.height()
            super().setPixmap(self.origPixelMap.scaled(w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        return super().resizeEvent(event)

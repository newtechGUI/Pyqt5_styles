from PyQt5.QtWidgets import QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class Button(QPushButton):
    def __init__(self, name, text, bg_color, pd, bg_hover):
        super(Button, self).__init__()

        self.name = name
        self.text = text
        self.bg_color = bg_color
        self.pd = pd
        self.bg_hover = bg_hover

        self.styles = "QPushButton { background-color: %s; padding: %i }" \
                      "QPushButton::hover { background-color: %s; }"\
                      % (self.bg_color, self.pd, self.bg_hover)

        self.setObjectName(self.name)
        self.setText(self.text)
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet(self.styles)

class LineEdit(QLineEdit):
    def __init__(self, name, plhd, w, h, bg_color):
        super(LineEdit, self).__init__()

        self.name = name
        self.plhd = plhd
        self.w = w
        self.h = h
        self.bg_color = bg_color

        self.styles = "QLineEdit { background-color: %s; }" \
                      % self.bg_color

        self.setObjectName(self.name)
        self.setPlaceholderText(self.plhd)
        self.setFixedWidth(self.w)
        self.setFixedHeight(self.h)
        self.setStyleSheet(self.styles)


import os
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QVBoxLayout, QMainWindow
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class ImageCanvas(QGraphicsView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    def wheelEvent(self, event):
        """Handle zoom in/out on mouse wheel."""
        zoom_in_factor = 1.25
        zoom_out_factor = 1 / zoom_in_factor

        old_pos = self.mapToScene(event.pos())

        if event.angleDelta().y() > 0:
            zoom_factor = zoom_in_factor
        else:
            zoom_factor = zoom_out_factor

        self.scale(zoom_factor, zoom_factor)

        new_pos = self.mapToScene(event.pos())
        delta = new_pos - old_pos
        self.translate(delta.x(), delta.y())

class PNGGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Image Scrapper')
        self.setGeometry(300, 300, 1600, 900)  # Larger initial window size
        self.setWindowIcon(QIcon(resource_path('icon.png')))

        # Create the layout
        self.layout = QVBoxLayout()

        # Create the canvas (GraphicsView and GraphicsScene)
        self.scene = QGraphicsScene()
        self.canvas = ImageCanvas(self.scene)
        self.canvas.setScene(self.scene)

        # Add the canvas to the layout
        widget = QtWidgets.QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
        self.layout.addWidget(self.canvas)

        # Create a button to select the folder and start the process
        self.folder_btn = QtWidgets.QPushButton('Select Folder')
        self.folder_btn.clicked.connect(self.select_folder)
        self.layout.addWidget(self.folder_btn)

        self.selected_folder = None
        self.column_padding = 150  # Padding between columns
        self.current_scene_width = 0  # Keep track of the width of the scene

    def select_folder(self):
        # Open folder dialog and immediately start processing
        self.selected_folder = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if self.selected_folder:
            self.generate_canvas()

    def generate_canvas(self):
        # Clear the canvas before starting
        self.scene.clear()

        if not self.selected_folder:
            return

        try:
            image_extensions = ['jpg', 'png', 'tif']

            # Collect all subfolders
            all_folders = []
            for root, dirs, files in os.walk(self.selected_folder):
                all_folders.append(root)

            # Arrange images from each folder into columns
            x_position = 50   # Initial X position for placing images
            for folder_path in all_folders:
                y_position = 50  # Start from the top for placing images vertically
                # Add images from this folder
                y_position, widest_image_width = self.add_images_to_scene(
                    folder_path, image_extensions, x_position, y_position)
                # Update x_position for the next column
                x_position += widest_image_width + self.column_padding

        except Exception as e:
            print(f"An error occurred: {str(e)}")  # Console error logging

    def add_images_to_scene(self, folder_path, image_extensions, x_position, y_position):
        images = [f for f in os.listdir(folder_path)
                  if f.split('.')[-1].lower() in image_extensions]
        widest_image_width = 0  # Track the widest image in this column
        for img in images:
            img_path = os.path.join(folder_path, img)
            try:
                # Load image using QPixmap and add to the scene (no scaling down)
                pixmap = QPixmap(img_path)
                if pixmap.isNull():
                    print(f"Could not load image {img_path}")
                    continue
                item = QGraphicsPixmapItem(pixmap)  # Full size
                item.setPos(x_position, y_position)
                self.scene.addItem(item)

                # Update the widest image width encountered
                if pixmap.width() > widest_image_width:
                    widest_image_width = pixmap.width()

                # Add label with font size 22
                label = f"{os.path.basename(folder_path)} - {img}"
                font = QFont("Arial", 22)  # Font size set to 22
                text_item = self.scene.addText(label)
                text_item.setFont(font)
                text_item.setPos(x_position, y_position + pixmap.height() + 10)  # Position the label under the image

                # Update Y position after placing the image
                y_position += pixmap.height() + 80  # Space between images

                # Update the width of the canvas
                self.update_scene_size(x_position + pixmap.width(), y_position)

            except Exception as e:
                print(f"Could not add image {img}: {str(e)}")

        return y_position, widest_image_width  # Return updated y_position and the widest image width

    def update_scene_size(self, new_width, new_height):
        """Update the scene size to accommodate new items."""
        if new_width > self.current_scene_width:
            self.current_scene_width = new_width
        self.scene.setSceneRect(0, 0, self.current_scene_width + 200, new_height + 200)

def main():
    app = QtWidgets.QApplication([])
    window = PNGGeneratorApp()
    window.showMaximized()
    app.exec_()

if __name__ == '__main__':
    main()

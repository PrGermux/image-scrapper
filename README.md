# Image Scrapper

**Image Scrapper** is a Python application designed for efficiently scraping, displaying, and navigating through images stored in a hierarchical folder structure. This tool leverages PyQt5 for its graphical user interface, providing an interactive, zoomable, and scrollable canvas to visualize images from multiple directories.

#### Key Features:
- **Folder Traversal**: Automatically scans a root directory and recursively includes all subfolders, displaying images from every level of the hierarchy.
- **Interactive Canvas**: Displays images on a dynamic, infinite canvas with zoom and pan capabilities, allowing for easy navigation of large datasets.
- **Image Organization**: Groups images from each folder into vertical columns, with folder names and image names clearly labeled below each image.
- **File Type Support**: Supports commonly used image file formats, including JPG, PNG, and TIFF.
- **Customizable Layout**: Dynamically adjusts the canvas size to accommodate all images and folders, ensuring a smooth viewing experience.
- **Performance Optimization**: Handles large image datasets efficiently while maintaining interactivity and responsiveness.

#### Usage
This tool is ideal for:
- Researchers or analysts working with image datasets.
- Professionals who need to explore images organized in nested folders.
- Developers requiring an easy-to-use image visualization tool.

#### Python Branch and Complexity
- **Python Branch**: This project utilizes PyQt5 for GUI development, with Python’s `os` module for file handling and `QGraphicsView` for interactive graphics rendering.
- **Complexity**: The application handles recursive folder traversal, dynamic canvas resizing, and interactive image rendering, making it moderately complex. The integration of zoom and pan functionalities ensures a professional-grade user experience.

#### Code Structure
- **Main Interface**: Built using PyQt5's `QGraphicsView` and `QGraphicsScene` to support infinite canvas functionality with zoom and pan capabilities.
- **Folder and File Handling**: Recursively traverses directories to identify image files and display them in structured columns.
- **Dynamic Canvas Layout**: Automatically adjusts the canvas size and positioning of images and labels, ensuring clarity and usability.

#### Demonstration:

![Animation](https://github.com/user-attachments/assets/555b13c7-26b4-4181-a845-f8b0fc6a010a)

#### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/image-scrapper.git
   cd image-scrapper
   ```
2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

#### Usage
Run the main application:
```sh
python main.py
```

Select the root folder containing images, and the application will automatically scrape all subfolders and display the images in an organized layout on the canvas.

#### Freezing
To package the application as a standalone executable:
```sh
pyinstaller --onefile --windowed --icon=icon.png --add-data "icon.png;." --name "Image Scrapper" main.py
```

#### Dependencies
- Python 3.x
- PyQt5

#### Future Enhancements
- **Thumbnail Generation**: Add an option to load smaller thumbnails for improved performance with extremely large datasets.
- **Image Filtering**: Allow filtering by file type or other metadata.
- **Annotation Support**: Add support for basic annotation or markup on images.
- **Save Layout**: Provide the ability to save the current canvas layout for later use.

#### License
This project is licensed under the MIT License for non-commercial use.

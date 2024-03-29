# Image Converter and Resizer

This Python script allows you to convert all non-transparent pixels of an image to black, resize it to a new dimension, and save the processed image. It's particularly useful for handling images with transparency, like PNG files, where you might want to normalize the color of all visible pixels while maintaining their transparency.

## Requirements

To run this script, you need Python installed on your system along with the Pillow library, which is a fork of PIL (Python Imaging Library).

### Installing Pillow

You can install Pillow using pip. Run the following command in your terminal:

`pip install Pillow`

## Usage

To use this script, you need to provide the source image path as an argument. The script processes the image by converting all non-transparent pixels to black, resizes the image to 4000x4000 pixels (default size), and saves it as `resized-image.png` in the current directory.

### Running the Script

Navigate to the directory containing the script and run the following command: `python convert_and_resize_image.py <source_image_path>`
Replace `<source_image_path>` with the path to your source image. For example:

ie. python logo-formatter.py ./path/to/your/image.png


# HEIC to JPG Converter

This Python application is a simple and efficient tool for converting HEIC images to JPG format. It uses the PIL and pillow_heif libraries to handle the image conversion, and tkinter for the graphical user interface. The application allows users to select a directory, and it will find and convert all HEIC files within that directory (including subdirectories).

## Features

- GUI for easy usage
- Converts all HEIC files in a selected directory (including subdirectories)
- Progress bar to track the conversion process
- Error handling for failed conversions
- Option to move failed conversions to a separate directory

## Installation

1. Clone this repository
2. Install the required Python libraries (see dependencies)

## Usage

1. Run `python heic_to_jpg.py`
2. Click "Select Directory" and choose the directory containing your HEIC files
3. Confirm the conversion
4. If any files fail to convert, you will be given the option to move them to a separate directory

## Dependencies

- Python 3
- PIL
- pillow_heif
- tkinter

# OCR Application

## Introduction
This OCR (Optical Character Recognition) application is designed to efficiently convert images to text using Python and Tesseract OCR. It features a modern GUI built with CustomTkinter and supports various image formats.

## Features
- **Image to Text Conversion**: Convert images to editable text using Tesseract OCR.
- **Multi-language Support**: Extract text in various languages (initially set to English).
- **User-friendly GUI**: Easy-to-navigate graphical user interface for seamless operation.

## Installation

### Prerequisites
- Python 3.x
- PIL (Pillow)
- CustomTkinter
- pytesseract
- OpenCV (optional for future image processing enhancements)

### Setting Up Tesseract OCR
1. Download and install Tesseract OCR from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract).
2. Ensure that the path to the Tesseract executable is correctly set:
   ```bash
   # Example for Windows
   C:\> set TESSDATA_PREFIX=C:\Program Files\Tesseract-OCR\tessdata


## Install Python Dependencies
Install the required Python libraries using pip:

   pip install customtkinter pytesseract Pillow opencv-python


## Usage:
To run the application, navigate to the application directory and execute: python app.py

## How to Use:
  Launch the Application: Run the script and the GUI will appear.
  Add Image: Click the 'Browse Image' button to load the image you want to process.
  Set Language and Output Path: Enter the desired language code and the output path for saving the extracted text.
  Extract Text: Click 'Extract Text' to convert the image to text.

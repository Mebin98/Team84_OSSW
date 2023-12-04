# RGB Color Detection Scripts

![test_image](https://github.com/Mebin98/Team84_OSSW/assets/121173175/de38b194-02b1-478a-8701-2af9f53ce9e5)

<img width="419" alt="blue" src="https://github.com/Mebin98/Team84_OSSW/assets/121173175/315acea3-5845-4fc6-9960-894d37c5d7fc">
<img width="416" alt="green" src="https://github.com/Mebin98/Team84_OSSW/assets/121173175/44fe0150-899c-42c0-8e6b-fd11b3beb31e">
<img width="416" alt="red" src="https://github.com/Mebin98/Team84_OSSW/assets/121173175/9bf016b7-3e4b-46aa-9381-a048a5b9d086">



## Introduction

This repository houses a set of Python scripts that are designed to detect and extract RGB (Red, Green, and Blue) color values from images. There are individual scripts for each color channel detection (`Detection_Red.py`, `Detection_Green.py`, `Detection_Blue.py`) and a comprehensive script (`Detection_RGB.py`) for a full RGB color analysis.

## Features

- Modular color detection with individual scripts for Red, Green, and Blue channels.
- Integrated RGB detection for a combined color analysis.
- Example image (`test_image.jpg`) included for quick testing.

## Installation

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/Mebin98/Team84_OSSW

Navigate to the cloned repository's directory:
cd Team84-OSSW


Usage
To detect specific color channels in an image, run the corresponding script with the image file as an argument. You can use the provided test_image.jpg or replace it with the path to your image.

Detect the Red color channel:

python Detection_Red.py test_image.jpg

Detect the Green color channel:

python Detection_Green.py test_image.jpg

Detect the Blue color channel:

python Detection_Blue.py test_image.jpg

For full RGB detection:

python Detection_RGB.py test_image.jpg


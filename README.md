# PillowProject

A Python script that creates a humorous meme about students frantically looking for their class mayor before attendance submission, featuring multiple cat images with bisaya text overlays.

## Description
This project uses PIL (Python Imaging Library) to create a composite image that captures the relatable student experience of last-minute attendance panic. The meme features:
- A custom background image
- Multiple cat images positioned strategically
- Filipino text overlays expressing student emotions
- A clean white header with the main caption
- 
## Features
- **Image Composition**: Combines a background image with multiple cat overlays
- **Text Rendering**: Adds Filipino text captions using custom fonts
- **Image Resizing**: Automatically resizes cat images to fit the composition
- **Multiple Font Sizes**: Uses different font sizes for headers and captions
- **Automatic Display**: Shows the final result after creation

## Requirements
- Python 3.x
- PIL (Pillow library)
- Font file: `arial.ttf`
- Image files in `images/` directory:
  - `background_img.jpg` (background image)
  - `cat1.png` through `cat8.png` (cat images)

## Installation
1. Install the required library:
```
pip install Pillow
```

## Usage

Simply run the Python script:
```bash
python script.py
```

The script will:
1. Load the background image
2. Add a white header rectangle with the POV text
3. Position and resize 8 different cat images
4. Add bisaya text captions to some cats
5. Save the final image as `CSELEC3_3A_AbarquezAga_Activity1.png`
6. Display the created savd image

## Output
The script generates a PNG file named `CSELEC3_3A_AbarquezAga_Activity1.png` in the same directory.

## Customization
You can easily customize the meme by:
- Replacing cat images in the `images/` folder
- Modifying text captions and positions
- Changing font sizes or colors
- Adjusting image positions and sizes
- Using a different background image

## Credits
- Background image credits to Campus Access
- Created for CSELEC3_3A class activity

## License
This project is for educational purposes as part of a class activity.

## Author
Aga O. Abarquez

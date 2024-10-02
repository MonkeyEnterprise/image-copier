# ImageCopier

`ImageCopier` is a Python class designed to copy random images from a source directory to a destination directory, ensuring no duplicate images are copied based on the content of the images. The script uses MD5 hashing to detect duplicates and avoid copying them.

## Features

- Selects a random set of images from a source directory.
- Copies images to a destination directory.
- Ensures no duplicate images are copied by comparing the content using MD5 hashes.
- Automatically creates the destination directory if it doesn't exist.

## Requirements

To run this script, you need the following dependencies:

- Python 3.x
- The following Python libraries:
  - `shutil` (standard library)
  - `os` (standard library)
  - `random` (standard library)
  - `hashlib` (standard library)
  - `Pillow` (for image processing)

You can install the `Pillow` library by running:

```bash
pip install pillow
```

## Installation

1. Clone or download this repository to your local machine.
2. Ensure that you have Python 3.x installed.
3. Install the required libraries mentioned above (use `pip install pillow` if `Pillow` is not installed).

## Usage

### Running the Script

You can run the script directly from the terminal or command line:

```bash
python image_copier.py
```

When you run the script, it will ask you to provide the following:

- **Source directory**: The path to the directory containing the images you want to copy from.
- **Destination directory**: The path to the directory where you want to copy the images.
- **Number of images**: The number of random images you want to copy.

### Example

1. Run the script:

```bash
python image_copier.py
```

2. When prompted, provide the necessary input:

```bash
Give the source directory: /path/to/source
Give the destination directory: /path/to/destination
Give the number of images to copy: 100
```

The script will then:

- Randomly select 100 images (or fewer, if the source directory contains less than 100 images).
- Generate MD5 hashes for each image to ensure duplicates are skipped.
- Copy unique images to the destination directory.
- Print the status of each copied image.

### Code Overview

#### Class: `ImageCopier`

The main functionality is encapsulated in the `ImageCopier` class.

##### Constructor: `__init__(self, source_dir, destination_dir, num_images=250)`

- **Parameters**:
  - `source_dir` (str): The path to the source directory containing images.
  - `destination_dir` (str): The path to the destination directory where images will be copied.
  - `num_images` (int): The number of random images to copy (default is 250).

##### Method: `hash_image(self, image_path)`

- **Parameters**:
  - `image_path` (str): The path to the image file.
  
- **Returns**:
  - The MD5 hash of the image content. Returns `None` if the image cannot be processed.

##### Method: `copy_images(self)`

- Selects random images from the source directory and copies unique images to the destination directory.
  
- If the destination directory does not exist, it creates it automatically.

- Raises:
  - `FileNotFoundError` if the source directory doesn't contain valid images.

### Handling Duplicates

The script detects duplicates by comparing the MD5 hash of each image. If the hash of an image matches one that has already been copied, it skips that image and continues copying the next random image.

## Example Code

Here's an example of how the class is instantiated and used:

```python
# Example of use
if __name__ == "__main__":
    source_directory = input("Give the source directory: ")
    destination_directory = input("Give the destination directory: ")
    num_images = int(input("Give the number of images to copy: "))

    copier = ImageCopier(source_directory, destination_directory, num_images=int(num_images))
    copier.copy_images()
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

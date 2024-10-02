import os
import shutil
import random
import hashlib
from PIL import Image

class ImageCopier:
    """
    A class to copy random images from a source directory to a destination directory,
    ensuring no duplicate images are copied based on image content.

    Attributes
    ----------
    source_dir : str
        The path to the source directory containing images.
    destination_dir : str
        The path to the destination directory where images will be copied.
    num_images : int
        The number of images to copy (default is 250).

    Methods
    -------
    hash_image(image_path):
        Generates an MD5 hash of the image to detect duplicates.
    copy_images():
        Selects random images and copies unique ones to the destination directory.
    """

    def __init__(self, source_dir, destination_dir, num_images=250):
        """
        Initializes the ImageCopier with source and destination directories and the number of images to copy.

        Parameters
        ----------
        source_dir : str
            The path to the source directory containing images.
        destination_dir : str
            The path to the destination directory where images will be copied.
        num_images : int, optional
            The number of images to copy (default is 250).
        """
        self.source_dir = source_dir
        self.destination_dir = destination_dir
        self.num_images = num_images
        self.seen_hashes = set()

    def hash_image(self, image_path):
        """
        Generates an MD5 hash of the image to detect duplicates.

        Parameters
        ----------
        image_path : str
            The path to the image file.

        Returns
        -------
        str or None
            The MD5 hash of the image, or None if the image could not be processed.
        """
        try:
            img = Image.open(image_path)
            img_hash = hashlib.md5(img.tobytes()).hexdigest()
            return img_hash
        except Exception as e:
            print(f"Error processing {image_path}: {e}")
            return None

    def copy_images(self):
        """
        Selects random images from the source directory and copies unique images
        to the destination directory, ensuring no duplicate images are copied.

        If the destination directory does not exist, it is created.

        Raises
        ------
        FileNotFoundError
            If the source directory does not exist or contains no valid images.
        """
        if not os.path.exists(self.destination_dir):
            os.makedirs(self.destination_dir)

        # Get all files from the source directory
        all_images = [f for f in os.listdir(self.source_dir) if os.path.isfile(os.path.join(self.source_dir, f))]
        
        if not all_images:
            raise FileNotFoundError(f"No files found in source directory: {self.source_dir}")

        # Ensure we don't select more than what's available
        num_images_to_copy = min(self.num_images, len(all_images))

        # Randomly select files
        random_images = random.sample(all_images, num_images_to_copy)
        
        copied_count = 0
        for image_name in random_images:
            image_path = os.path.join(self.source_dir, image_name)
            image_hash = self.hash_image(image_path)
            
            if image_hash and image_hash not in self.seen_hashes:
                self.seen_hashes.add(image_hash)
                shutil.copy(image_path, self.destination_dir)
                copied_count += 1
                print(f"Copied {image_name} to {self.destination_dir}")
            else:
                print(f"Duplicate found: {image_name}, skipping...")

        print(f"Successfully copied {copied_count} unique images.")


if __name__ == "__main__":
    source_directory = input("Give the source directory: ")
    destination_directory = input("Give the destination directory: ")
    num_images = int(input("Give the number of images to copy: "))
    
    copier = ImageCopier(source_directory, destination_directory, num_images=num_images)
    copier.copy_images()

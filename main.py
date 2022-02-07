import os
from sys import exit
import PIL
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
import numpy as np

from create_folder import create_dir
from pdf2image import convert_from_path
from args import parse_arguments


def print_line():
    print("--------------")


def main():
    args = parse_arguments()        

    if args.output_path:
        img_folder = os.path.join(args.output_path, "img")
        if not os.path.isdir(img_folder):
            os.makedirs(img_folder)
    else:
        img_folder = os.path.join(os.path.abspath(os.getcwd()), "img")
        if not os.path.isdir(img_folder):
            os.makedirs(img_folder)

    print(f"Working directory is: '{img_folder}'")
    print_line()

    for pdf in args.files:
        # Split PDF to single images
        file_name = (pdf.split('/')[-1]).split('.')[0]
        sub_img_folder = create_dir(img_folder, file_name)
        print(f"--- {pdf} ---")
        print(f"Spliting to images...")

        if args.jpeg:
            convert_from_path(pdf, output_folder=sub_img_folder, output_file='', fmt='jpeg', strict=False, jpegopt={"quality": 100, "progressive": True, "optimize": True})
        else:
            convert_from_path(pdf, output_folder=sub_img_folder, output_file='', fmt='png', strict=False)
        
        # Get images 
        print(f"Concatenating....")
        list_images = []
        for file in os.listdir(sub_img_folder):
            if file.split('.')[-1] in ['png', 'jpeg']:
                list_images.append(file)
        list_images.sort()


        # Concatenate images
        images = [PIL.Image.open(os.path.join(sub_img_folder, i)) for i in list_images]
        if args.invert:
            images = [PIL.ImageOps.invert(image) for image in images]
        min_shape = sorted([(np.sum(i.size), i.size) for i in images])[0][1]

        if args.vertical:
            images_combined = np.vstack( (np.asarray( i.resize(min_shape) ) for i in images))
        else:
            images_combined = np.hstack( ( np.asarray(i.resize(min_shape) ) for i in images))

        
        # Save the image
        images_combined = PIL.Image.fromarray(images_combined)
        save_file = os.path.join(sub_img_folder, (file_name + '.png'))
        images_combined.save(save_file)
        print(f"Success! Saved as: '{save_file}'")
        print_line()

    
if __name__ == '__main__':
    exit(main())
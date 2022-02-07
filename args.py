import argparse
from os import path
from os import getcwd

from importlib_metadata import files

class Options:
    def __init__(self, files, output_path, image_type, invert, vertical):
        self.files = files
        self.output_path = output_path
        self.jpeg = image_type
        self.invert = invert
        self.vertical = vertical

    def __str__(self):
        return f"{self.files}, {self.output_path}, {self.image_type}, {self.invert}"

    def print(self):
        print("---- ARGS ----")
        print(f"Files:\t\t{self.files}")
        print(f"Output:\t\t{self.output_path}")
        print(f"Type JPEG:\t{self.image_type}")
        print(f"Invert:\t\t{self.invert}")

    def ispath(self, dir):
        if path.isdir(dir):
            return True
        False
        

def parse_arguments():
    parser = argparse.ArgumentParser(description='Converting PDF files to an image')

    parser.add_argument('-f', '--files', dest='files', action='append', nargs='+', 
        required=True, help='Path to the PDF file to be converted')
    parser.add_argument('-o', '--output-path', dest='output_dest', nargs='?', default=path.abspath(getcwd()),
        help='Output result path (default: current working directory)')
    parser.add_argument('--jpeg', dest='file_type', action='store_true',
        help='Output file type (default: png)')
    parser.add_argument('-i', '--invert-colors', dest='invert', action='store_true',
        help='Output image will have inverted colors (default: False)')
    parser.add_argument('-v', '--vertical', dest='vertical', action='store_true',
        help='Resulting image will be vertical (default: horizontal)')

    args = vars(parser.parse_args())


    options = Options(args['files'][0], args['output_dest'], args['file_type'], args['invert'], args['vertical'])
    return options

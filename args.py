import argparse
from ast import parse
from os import path
from os import getcwd

class Options:
    def __init__(self, files, output_path, image_type, invert):
        self.files = files
        self.output_path = output_path
        self.image_type = image_type
        self.invert = invert


def parseArguments():
    parser = argparse.ArgumentParser(description='Parsing arguments')

    parser.add_argument(['-f', '--files'], dest='files', action='append' ,nargs='+', metavar='[XXX.pdf YYY.pdf ...]', 
        required=True, help='Path to the PDF file to be converted')
    parser.add_argument('--png', dest='file_type', action='store_false',
        help='Output file type (default: jpg)')
    parser.add_argument(['-o', '--output-path'], dest='output_dest', nargs='?', default=path.abspath(getcwd()),
        help='Output result path (default: current working directory)')
    parser.add_argument(['-i', '--invert-colors'], dest='invert', action='store_false', nargs='?',
        help='Output image will have inverted colors (default: False)')
    

    return Options(parser.files, parser.output_dest, parser.file_type, parser.invert)
# PDF to images
A small script that converts a list of PDF files to individual images and also a big stacked (horizontally or vertically) image.

### Dependencies
- `pdf2image`
- `numpy`

### Usage
`python3 main.py -h`
```
  -h, --help                        show this help message and exit
  -f FILES [FILES ...], --files FILES [FILES ...]
                                    Path to the PDF files to be converted
  -o [OUTPUT_DEST], --output-path [OUTPUT_DEST]
                                    Output result path (default: current working directory)
  -j, --jpeg                        Export as JPEG instead (default: png)
  -i, --invert-colors               Output image will have inverted colors (default: False)
  -v, --vertical                    Resulting image will be vertical (default: horizontal)
```

`python3 main.py -f doc1.pdf doc2.pdf`

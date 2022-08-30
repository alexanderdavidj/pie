#! /usr/bin/env python3

from PIL import Image
import argparse
import os.path

__version__ = "0.0.0"

def convertbytes(bytes):
    for i in ["bytes", "KB", "MB", "GB", "TB"]:
        if bytes < 1024.0:
            return "%3.1f %s" % (bytes, i)
        bytes /= 1024.0
        
def main():
    parser = argparse.ArgumentParser(
        prog="pie", description="Process an image's pixels")
    parser.add_argument("-f", "--file", type=str,
                        required=True, help="Path to image file")
    parser.add_argument("-o", "--out", type=str, required=False,
                        default="pixel.txt", help="Output file name")
    parser.add_argument("-d", "--div", type=str, required=False,
                        default="-", help="Pixel string dividier")
    parser.add_argument("-s", "--size", action="store_true", required=False,
                        default=False, help="Include image dimensions in the file")
    parser.add_argument("-c", "--compress", action="store_true", required=False,
                        default=False, help="Compress processed file by removing whitespace")
    parser.add_argument("-v", "--verbose", action="store_true",
                        required=False, default=False, help="Enable verbose mode")
    parser.add_argument("--version", action="version",
                        version="%(prog)s " + __version__)

    args = parser.parse_args()

    def debug(message):
        if (args.verbose):
            print("[pie] %s" % message)

    def format(p1, p2, rgb):
        array = [rgb[0], rgb[1], rgb[2], "%d%s%d" % (p1, args.div, p2)]

        return array

    pixels = []
    pixelcount = 0

    im = Image.open(args.file)
    pix = im.convert("RGB")

    if (args.size):
        pixels.append([im.size[0], im.size[1]])
        debug("Adding image dimensions to processed file")
    else:
        debug("Ommitted adding image dimensions to processed file")

    debug("Creating pixels array")
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            pixels.append(format(i, j, pix.getpixel((i, j))))
            pixelcount += 1

    debug("Created pixels array with {:,} pixels".format(pixelcount))

    debug("Creating file %s" % args.out)
    file = open(args.out, "w")
    content = str(pixels).replace("\'", "\"")

    if (args.compress):
        debug("Compressing processed file")
        file.write(content.replace(" ", ""))

        debug("Wrote and compressed file content")
    else:
        debug("Writing file content")
        file.write(content)

        debug("Wrote file content without compressing")

    file.close()
    debug("Processed file is ready")
    debug("Processed file came out to %s" %
          convertbytes(os.path.getsize(args.out)))


if __name__ == "__main__":
    main()

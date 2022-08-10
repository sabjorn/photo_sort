import os
import argparse
import logging
import pathlib
import datetime

parser = argparse.ArgumentParser()
parser.add_argument("input", help="input directory for photos")
parser.add_argument(
    "-v",
    "--verbose",
    help="increase output verbosity",
    action="store_true")
args = parser.parse_args()

logging_level = logging.INFO
if(args.verbose):
    logging_level = logging.DEBUG

logging.basicConfig(format="%(message)s", level=logging_level)


valid_images = [".jpg", ".jpeg", ".mp4"]
for f in os.listdir(args.input):
    ext = os.path.splitext(f)[1]

    if ext.lower() not in valid_images:
        continue

    logging.debug(f"image file: {f}")

    input_fullpath = os.path.join(args.input, f)
    logging.debug(input_fullpath)

    c_time = pathlib.Path(input_fullpath).stat().st_ctime
    dt_c = datetime.datetime.fromtimestamp(c_time)
    logging.debug(dt_c)

    year = dt_c.strftime("%Y")
    month = dt_c.strftime("%M")
    day = dt_c.strftime("%d")
    output_directory = os.path.join("./", year, month, day)
    logging.debug(f"creating directory: {output_directory}")
    os.makedirs(output_directory, exist_ok=True)
 
    hour = dt_c.strftime("%H")
    minute = dt_c.strftime("%M")
    second = dt_c.strftime("%S")
    ms = dt_c.strftime("%f")
    output_filename = f"{year}-{month}-{day}_{hour}.{minute}.{second}.{ms}{ext}"

    output_fullpath = os.path.join(output_directory, output_filename)
    logging.debug(f"writing symlink {f} to {output_fullpath}")
    try:
        os.symlink(input_fullpath, output_fullpath)
    except FileExistsError:
        logging.error(f"{f} already exists in {output_directory}, skipping")

import os
import argparse
import logging
import pathlib
import time
import hashlib

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

valid_images = [".jpg", ".jpeg", ".mp4", ".cr2"]
for f in os.listdir(args.input):
    ext = os.path.splitext(f)[1]

    if ext.lower() not in valid_images:
        logging.debug(f"no image found in {f}")
        continue

    logging.debug(f"image file: {f}")

    input_fullpath = os.path.join(args.input, f)
    logging.debug(input_fullpath)
    
    ti_m = os.path.getmtime(input_fullpath)
    m_ti = time.ctime(ti_m)
    t_obj = time.strptime(m_ti)

    year = time.strftime("%Y", t_obj)
    month = time.strftime("%m", t_obj)
    day = time.strftime("%d", t_obj)
    output_directory = os.path.join("./", year, month, day)
    logging.debug(f"creating directory: {output_directory}")
    os.makedirs(output_directory, exist_ok=True)
 
    hour = time.strftime("%H", t_obj)
    minute = time.strftime("%M", t_obj)
    second = time.strftime("%S", t_obj)

    m = hashlib.md5()
    m.update(bytes(f, encoding="utf-8"))
    hash = m.hexdigest()[:6] 
    output_filename = f"{year}-{month}-{day}_{hour}.{minute}.{second}.{hash}{ext}"

    output_fullpath = os.path.join(output_directory, output_filename)
    logging.debug(f"writing symlink {f} to {output_fullpath}")
    try:
        os.symlink(
                os.path.relpath(input_fullpath, output_directory),
                output_fullpath
                )
    except FileExistsError:
        logging.error(f"{f} already exists in {output_directory}, skipping")

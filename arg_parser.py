from pathlib import Path
import argparse
import configs

from arg_converters import (
    flatten_paths,
    convert_to_path
)


DESCRIPTION = f"""
    Simple script to get total duration of multiple video files. When passed a directory path
    the script will look for files matching file extensions then aggregate and show the total
    length of the files.
    
    Examples:
    total-video-duration "{str(Path.home())}/Videos" -fx mp4 mov -r 
    """

arg_parser = argparse.ArgumentParser(description=DESCRIPTION)
arg_parser.add_argument("base_dir",
    type=convert_to_path,
    nargs='+',
    help="Path to the parent folder to look for video files"
)
arg_parser.add_argument(
    "-fx",
    "--file_extension",
    nargs="*",
    type=str,
    default=configs.FILE_EXTENSIONS,
    help=f"Video files to look for having extensions. Default: {configs.FILE_EXTENSIONS}",
)
arg_parser.add_argument(
    "-r",
    "--recursive",
    default=configs.RECURSIVE,
    action="store_true",
    help="Recursively look for video files",
)

parsed_args = arg_parser.parse_args()
parsed_args.base_dir = flatten_paths(parsed_args.base_dir)

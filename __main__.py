#!/usr/bin/python3
import cv2
import datetime
from pathlib import Path
from arg_parser import parsed_args
from collections.abc import Iterable


base_dir: Path = parsed_args.base_dir
file_extensions: list[str] = parsed_args.file_extension
is_recursive: bool = parsed_args.recursive


def get_video_duration(file_path: str) -> float: # returns seconds
    video = cv2.VideoCapture(file_path)
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS)
    return 0 if fps ==0 else frames / fps


def get_total_duration(
        base_dirs: list[Path],
        file_extensions: list[str],
        is_recursive: bool
    ):

    globs: list[Iterable[Path]] = []
    for base_dir in base_dirs:
        for file_extension in file_extensions:
            if is_recursive:
                glob = base_dir.glob(f"**/*.{file_extension}")
            else:
                glob = base_dir.glob(f"*.{file_extension}")
            globs.append(glob)
    
    total_duration = 0 # seconds
    for glob in globs:
        for file in glob:
            absolute_file_path = str(file.absolute())
            total_duration += get_video_duration(absolute_file_path)
    
    total_duration = datetime.timedelta(seconds=round(total_duration))
    print("Total duration is:", total_duration)


def main():
    get_total_duration(base_dir, file_extensions, is_recursive)

if __name__ == '__main__':
    main()

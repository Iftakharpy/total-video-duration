#!/usr/bin/python3
import cv2
from datetime import timedelta as dt
from pathlib import Path
from arg_parser import parsed_args
from typing import Iterable, Callable


base_dir: Path = parsed_args.base_dir
file_extensions: list[str] = parsed_args.file_extension
is_recursive: bool = parsed_args.recursive
is_verbose: bool = parsed_args.verbose

TITLE_LENGTH = 60
TITLE_CHAR = "="
TITLE_EMPTY_SPACE_FILLER = " "

def get_video_duration(file_path: str) -> float: # returns seconds
    video = cv2.VideoCapture(file_path)
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS)
    return 0 if fps ==0 else frames / fps


def get_total_duration(
        base_dirs: list[Path],
        file_extensions: list[str],
        is_recursive: bool,
        video_duration_callback: Callable[[float, str], None]=None
    ):

    globs: list[Iterable[Path]] = []
    for base_dir in base_dirs:
        for file_extension in file_extensions:
            if is_recursive:
                glob = base_dir.glob(f"**/*.{file_extension}")
            else:
                glob = base_dir.glob(f"*.{file_extension}")
            globs.append(glob)
    
    total_videos = 0
    total_duration = 0 # seconds
    if is_verbose:
        print("".center(TITLE_LENGTH, TITLE_CHAR))
        print("Processing Video files".center(TITLE_LENGTH, TITLE_EMPTY_SPACE_FILLER))
        print("".center(TITLE_LENGTH, TITLE_CHAR))
    for glob in globs:
        for file in glob:
            absolute_file_path = str(file.absolute())
            video_duration = get_video_duration(absolute_file_path)
            if is_verbose and video_duration_callback:
                video_duration_callback(video_duration, absolute_file_path)
            
            total_videos += 1
            total_duration += video_duration
    
    return total_duration, total_videos


def main():
    total_duration, total_videos = get_total_duration(
        base_dir,
        file_extensions,
        is_recursive,
        video_duration_callback=lambda duration, video_file: print(f"{dt(seconds=round(duration))} - {video_file}")
    )
    
    total_duration = dt(seconds=round(total_duration))
    if is_verbose:
        print()
        print("".center(TITLE_LENGTH, TITLE_CHAR))
        print("Summary".center(TITLE_LENGTH, TITLE_EMPTY_SPACE_FILLER))
    
    print("".center(TITLE_LENGTH, TITLE_CHAR))
    print(f"Videos: {total_videos}")
    print(f"Total Duration: {total_duration}")
    print("".center(TITLE_LENGTH, TITLE_CHAR))



if __name__ == '__main__':
    main()

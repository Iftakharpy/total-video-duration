# total_video_duration
Shows total video duration of video files in a folder, multiple folders or glob patterned folders recursively or non-recursively.

## Requirements
- `Python 3.11` or newer
- Install requirements

## Installation
1. Install `Python 3.11` or newer
2. Clone the repository using `git`
3. Open the cloned repository in terminal
4. Run `python3 -m pip install -r requirements.txt`
5. Optionally you can add the folder to you environment `PATH` variable to be able to run it from anywhere on linux based operating system might work on windows as well. This will also require you to add `execute` permission to `total_video_duration.py` file.

## Usage Examples
```bash
❯ pwd
/home/iftakhar/Desktop/Projects/total-video-duration

❯ ./total_video_duration.py ~/Downloads/The\ Ultimate\ Design\ Patterns\ Part\ 3 -r
Total duration is: 0:52:25

❯ ./total_video_duration.py ~/Downloads/The\ Ultimate\ Design\ Patterns\ Part\ II -r
Total duration is: 1:44:22

❯ ./total_video_duration.py ~/Downloads/The\ Ultimate\ Design\ Patterns\ Part\ I -r
Total duration is: 4:02:31

❯ ./total_video_duration.py ~/Downloads/The\ Ultimate\ Design\ Patterns\ Part\ * -r
Total duration is: 6:39:18

❯ ./total_video_duration.py "~/Downloads/The Ultimate Design Patterns Part *" -r
Total duration is: 6:39:18

❯ ./total_video_duration.py "~/Downloads/Design Patterns in Python" -r
Total duration is: 9:09:12


❯ pwd
/home/iftakhar/Downloads/Design Patterns in Python

❯ total_video_duration.py . -r
Total duration is: 9:09:12
```

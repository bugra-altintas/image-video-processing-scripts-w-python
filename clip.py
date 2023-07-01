#%pip install moviepy
#%pip install imageio-ffmpeg
import sys

input = sys.argv[1]

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip("/Users/bugra/Downloads/short.mp4", 0, 1, targetname="short1.mp4")
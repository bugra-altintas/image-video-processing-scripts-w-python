import moviepy.editor as mp
import sys

inp = sys.argv[1]
out = sys.argv[2]

video = mp.VideoFileClip(inp)
video.write_videofile(out)
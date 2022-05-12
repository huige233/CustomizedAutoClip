import moviepy.editor as mpy
import argparse
import sys

parser = argparse.ArgumentParser(description = 'This is a video capture script')
parser.add_argument('--time','-t',required=True,nargs=4,type=int,help="0 1 0 2")
parser.add_argument('--input','-i',required=True,nargs=1,type=str,help='input.mp4')
parser.add_argument('--output','-o',nargs=1,type=str,help='get.mp4')
parser.add_argument('--size','-s',nargs=2,type=int,help='480 360')
clip = mpy.VideoFileClip('./'+parser.parse_args().input[0])
if not parser.parse_args().size:
    content = clip.subclip((parser.parse_args().time[0], parser.parse_args().time[1]), (parser.parse_args().time[2], parser.parse_args().time[3]))
else:
    content = clip.subclip((parser.parse_args().time[0], parser.parse_args().time[1]), (parser.parse_args().time[2], parser.parse_args().time[3])).resize((parser.parse_args().size[0], parser.parse_args().size[1]))
if not parser.parse_args().output:
    content.write_videofile('./output.mp4')
else:
    content.write_videofile('./'+parser.parse_args().output[0])
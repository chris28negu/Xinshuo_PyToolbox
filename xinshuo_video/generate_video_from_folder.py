# Author: Bo Wang
# email: chris28negu@gmail.com

import sys
from xinshuo_video.video_processing import generate_video_from_folder
	
if __name__ == '__main__':
	if len(sys.argv) != 4:
		print('Usage: python generate_video_from_folder.py images_dir save_path frame_rate')
		sys.exit(1)

	images_dir = sys.argv[1]
	save_path = sys.argv[2]
	frame_rate = int(sys.argv[3])

	print('START VIDEO GENERATION!!\n')

	generate_video_from_folder(images_dir, save_path, framerate=frame_rate)

	print('\n\nDONE! SUCCESSFUL!!\n')
import os
import cv2
import argparse

from pathlib import Path
from utils import load_video, mkdir


parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, default='./videos',
                    help='path to inputs directory')
parser.add_argument('--output', type=str, default='./outputs',
                    help='path to outputs directory')
args = parser.parse_args()


def extract_frames(in_dir, out_dir):
    out_dir = Path(out_dir)
    in_dir = Path(in_dir)

    # Cria diretorio de output
    mkdir(out_dir)

    for utt_path in in_dir.rglob('*.mp4'):
        cap = load_video(utt_path)
        frame_dir = out_dir / Path(*Path(os.path.splitext(utt_path)[0]).parts[-3:])
        mkdir(frame_dir)
        has_frame, frame = cap.read()
        count = 0
        while has_frame:
            cv2.imwrite(f'{str(frame_dir)}/frame_{count}.jpg', frame)
            has_frame, frame = cap.read()
            count += 1


if __name__ == "__main__":
    extract_frames(args.input, args.output)
    # './data/videos/', './outputs'

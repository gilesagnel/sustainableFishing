import subprocess
import argparse

def download_segment(url, start_time, end_time, output_filename):
    command = [
        "youtube-dl",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "--merge-output-format", "mkv",
        "--external-downloader", "ffmpeg",
        "--external-downloader-args", f"-ss {start_time} -to {end_time}",
        "-o", output_filename,
        url
    ]
    subprocess.run(command)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download a segment of a YouTube video.")
    parser.add_argument('start_time', help="Start time in the format HH:MM")
    parser.add_argument('end_time', help="End time in the format HH:MM")
    parser.add_argument('output_filename', help="Output filename without extension")
    parser.add_argument('--url', default='https://youtu.be/62nnWHiYGpo', help="URL of the YouTube video (default: https://youtu.be/62nnWHiYGpo)")

    args = parser.parse_args()

    download_segment(args.url, f"{args.start_time}:00.00", f"{args.end_time}:00.00", f"{args.output_filename}.mp4")

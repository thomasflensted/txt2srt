import os
import sys
from datetime import timedelta


def main():

    if (len(sys.argv) != 2):
        print("Usage: python txt2sub.py <filepath>")
        return 1

    input_file = sys.argv[1]
    new_filename = "new_file.txt"
    generate_new_text_file(input_file, new_filename)
    convert_to_srt(new_filename)


def generate_new_text_file(in_file, new_filename):

    lines = get_lines_list(in_file)

    with open(new_filename, "w") as new_file:

        seconds = 0
        for count, line in enumerate(lines):

            timeStart = create_timing_string(seconds)
            seconds += 3
            timeEnd = create_timing_string(seconds)

            new_file.write(f"{count+1}\n{timeStart} --> {timeEnd}\n{line}\n\n")


def create_timing_string(seconds):

    hours_minutes_seconds = str(timedelta(seconds=seconds)).split(":")
    return f"{hours_minutes_seconds[0].zfill(2)}:{hours_minutes_seconds[1].zfill(2)}:{hours_minutes_seconds[2].zfill(2)},000"


def get_lines_list(in_file):

    with open(in_file, "r") as in_file:

        return [line.strip() for line in in_file.readlines() if len(line.strip()) > 0]


def convert_to_srt(filename):

    base = os.path.splitext(filename)[0]
    os.rename(filename, base + ".srt")


main()

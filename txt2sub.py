import pysrt
import sys


def main():

    if (len(sys.argv) != 2):
        print("Usage: python txt2sub.py <filepath>")
        return 1

    txt_file = sys.argv[1]
    convert_to_srt(txt_file)


def convert_to_srt(file):

    with open(file) as f:

        sub_list = f.readlines()

    sub_list = [line.strip() for line in sub_list]

    sub_filename = f"{file.split('.')[0]}.srt"

    sub_file = open(sub_filename, "w")
    sub_file.close()

    subs = pysrt.open(sub_filename)
    subs[0].text = "Hello, there"


main()

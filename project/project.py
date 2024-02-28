import argparse
from week9.project.edit import EditFeature
from os import path as fp


def main():
    try:
        args = get_dict_args()
        paths = args["path"]
        edit = EditFeature(file_path=paths)
        convert_gif(args, paths, edit)
    except Exception as e:
        exit("\n--------------------------------\nPlease input argument in CLI.\n:param -p: file path (video or folder of images)\n:param -s: output name. Eg: sample\n--------------------------------")

def get_dict_args():
    parser = argparse.ArgumentParser(
        description='Creating GIF\n',
        usage="\n:param -p: file path (video or folder of images)\n:param -s: output name. Eg: sample")
    parser.add_argument("-p", "--path", help="File path: Video or Folder of images")
    parser.add_argument("-s", "--savename", help="Output file name.")
    args = parser.parse_args()
    return vars(args)


def convert_gif(args, paths, edit):
    if fp.isfile(paths): # for video
        edit.vd_to_gif(args["savename"])
    elif fp.isdir(paths): # for folder of images
        edit.img_list_to_gif(args["savename"])



if __name__=="__main__":
    main()

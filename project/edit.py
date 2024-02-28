import os
from os import path as p
from PIL import Image, ImageOps
from moviepy.editor import VideoFileClip


class EditFeature:
    def __init__(self, file_path: str, img_list=None, savename=None) -> None:
        self.file_path = file_path
        self.img_list = img_list
        self.raise_error()
        self.savename = savename



    def raise_error(self) -> None:
        # try:
        if p.isfile(self.file_path): # case: one video or one image file
            if self.get_vd_file_size() > 5:
                raise SystemExit("Input file is big; maximum size: 5 Mb")
        elif p.isdir(self.file_path): # only folder of images
            self.img_list = os.listdir(self.file_path)
            if self.get_dir_size() > 5:
                raise SystemExit("Input file is big; maximum size: 5 Mb")
        # except Exception as e:
        #     exit(f"{e}: Give me exact location of file/folder.")


    def get_dir_size(self) -> int: # get size of folder. eg: 4 Mb
        try:
            size = 0
            for fp in self.img_list:
                fp = self.file_path + "//" + fp
                size += p.getsize(fp)
            return size / 10**6
        except TypeError:
            exit("Please read guidline carefully.")

    def get_vd_file_size(self) -> int: # get video file size
        return p.getsize(self.file_path) / 10**6


    def crop_img(self, img=None, size: tuple = (640, 480)): # one image allowed
        if img: # Is image inputed?
            img = self.file_path + "//" + img
        with Image.open(img) as im1:
            im2 = ImageOps.fit(im1, size)
            im2.save(img)


    def crop_dir_of_imgs(self):
        for im in self.img_list:
            self.crop_img(img=im)


    def get_img_wh(self) -> tuple:
        with Image.open(self.file_path) as im:
            return im.size


    def get_dir_of_imgs_wh(self) -> list: # get width and height of folder of images as tuple of list
        sizes = []
        img_dir = self.file_path + "//"
        imgs_list = self.img_list
        for img in imgs_list:
            with Image.open(img_dir + img) as im:
                sizes.append(im.size)
        return sizes


    def img_list_to_gif(self, out_name="output"):
        self.crop_dir_of_imgs()
        images = []
        img_dir = self.file_path + "//"
        imgs_list = self.img_list
        print("\nConverting all images to GIF\n")
        for img in imgs_list:
            with Image.open(img_dir + img) as im:
                images.append(im.copy())

        images[0].save(
            f"{out_name}.gif", save_all=True, append_images=[*images], duration=500, loop=0
        )
        exit("\nImages to GIF COMPLETE!\n")


    def vd_to_gif(self, output_path="ouput", fps=10):
        vclip = VideoFileClip(self.file_path)
        vclip.subclip(0, 100)
        vclip.write_gif(output_path+".gif", fps=fps)
        exit("\nVideo to Gif COMPLETE!\n")


def main():
    edit = EditFeature("test_media/carshowroom.mp4") # file/folder path will be here
    edit.get_vd_file_size()


if __name__ == "__main__":
    main()

# CUSTOM-GiF

#### Video Demo 📺:

[project_demo]()

#### Description:

Convert a video file or folder of images to animated gif; before you convert, if input file is folder of images you can crop them.

#### Features:

* CLI control ✅
* Cropping images ✅
* Customizing your own GiF ✅
* Folder of images to GiF ✅
* Video to GiF ✅
* Give ouput name yourself ✅

#### How to use (Guide):

##### Warning⚠️:

* If input is folder of images, program will crop all images to width 640 height 480.

##### Requirement❗️:

* Only one file path is allowed. Eg: your_program.py -p filepath.
* Only your current working directory folder/file are allowed.
* Your input file or folder must be maximum of 5 Mb.
* If input is folder make sure to give only folder name.
* If input is folder of images be sure it is top level folder or file.
* In following picture "test_img_dir" and "walk.mp4" are top level folder/file.

![plot]([/workspaces/114047336/week9/project/image/README/top_level_exp.png](https://github.com/WaiHlyanZ/Custom-GIF/blob/main/project/image/README/top_level_exp.png))

##### Usage:

Use CLI to make a GiF.

According to above picture, commands to make a gif will be as follow:

"walk.mp4" to gif: `week9/ $ python project.py -p test_media/test_img_dir -s name `

"test_img_dir" to gif: `week9/ $ python project.py -p test_media/walk.mp4 -s name`

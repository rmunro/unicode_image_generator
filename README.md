# unicode_image_generator
Generates an image for every unicode character

This will generate a JPG file for unicode characters.

Requires python 3.x 
See the `import` statements at the top of `create_unicode_stratified.py` for additional python libraries that you might need to install.

# Usage:

`python create_unicode_stratified.py`

This will create the images in a `unicode_jpgs` directory, using the font file in this repo.

It will create an equal number of images per unicod range (block). Each block will be a different color: Latin characters will be one color, Tamil characters will be second color, etc

To change the image sizes, the font, the number of images per block, or other parameters, edit `create_unicode_stratified.py`

This code was created to experiment with StyleGAN:

https://github.com/NVlabs/stylegan

To read more about this experiment, see my artice about it:

https://towardsdatascience.com/creating-new-scripts-with-stylegan-c16473a50fd0

I'm releasing this code at the request of several people who read this article and wanted to play around with it themselves - good luck!

# Usage with StyleGAN

If you want to recreate the StyleGan experiments in my article, clone StyleGAN from the github repo above.

First, you'll need to convert the jpgs into the format that StyleGAN requires: 

`python dataset_tool.py create_from_images unicode_jpgs ~/custom-images`

Then edit `train.py` to point to your new directory. Then run the training algorithm:

`python train.py.`

StyleGAN's readme file has more details on the different parameters and options that you have. I trained my StyleGAN model from scratch with the default paramaters. 





# Description

You can use this program by calling the exact command:

python img_divider.py $image_1 $image_2 $image_n

So that some example uses of the program on images asdf.jpg, test1.png, and image2.png would be

python img_divider.py asdf.jpg
python img_divider.py test1.png 
python img_divider.py image2.png

Or, equivalently:

python img_divider.py asdf.jpg test1.png image2.png

Do not separate the filenames with commas, you can pass in as many filenames as you want. Ensure that the filenames are in the same directory for easy reference.

For each filename given, my script will open the file and divide the image into 4 sections like so:

|-----------------|
|        |        |
|   1    |   2    |
|        |        |
|-----------------|
|        |        |
|   3    |   4    |
|        |        |
|-----------------|

It then saves each of these smaller sections as a new image, of the format original_image_1, original_image_2, and so on.

So for example:

  Input: asdf.jpg 
  Output: asdf_1.jpg, asdf_2.jpg, asdf_3.jpg, asdf_4.jpg

  Input: test1.png 
  Output: test1_1.png, test1_2.png, test1_3.png, test1_4.png

  Input: a_1_1.png
  Output: a_1_1_1.png, a_1_1_2.png, a_1_1_3.png, a_1_1_4.png

# Installation

1. Download / Clone this repository

2. Run the demo via `python img_divider example.png`, or try it with any of your own images, using the instructions in the above description.

# Demo

As stated in the installation instructions, you can run the demo via `python img_divider example.png`, which will produce the example_1.png, example_2.png, example_3.png, and example_4.png files. Here are the results:

**Input** - example.png:

![Input](/example.png)

**Output**:

example_1.png:

![Output - topleft](/example_1.png)

example_2.png:

![Output - topright](/example_2.png)

example_3.png:

![Output - botleft](/example_3.png)

example_4.png:

![Output - botright](/example_4.png)


# Final Note

You can, as always, email me any questions you have. Good luck, have fun!

-Blake Edwards / Dark Element

"""
View the nearby README.txt for info on using this program.
It divides the images given into 4 equally sized sections and saves each as fname_1, fname_2, fname_3, and fname_4.

-Blake Edwards / Dark Element
"""
import cv2
import sys
import numpy as np

def split_and_handle_img_parts(f=None, recombine=False):
    """
    Check that we have args
    """
    if len(sys.argv) < 2:
        print "Image(s) must be supplied for processing, e.g. `python img_divider.py $img1 $img2 $img3`" 
        sys.exit()
        
    """
    Now loop through filenames
    """
    for fname in sys.argv[1:]:
        print "Dividing %s..." % fname 
        #Read in image
        img = cv2.imread(fname)
        h, w = img.shape[0], img.shape[1]

        """
        Now that we have the image, we get the four parts.
        """
        tl = img[:int(h/2.), :int(w/2.)]#topleft
        tr = img[:int(h/2.), int(w/2.):w]#topright
        bl = img[int(h/2.):h, :int(w/2.)]#botleft
        br = img[int(h/2.):h, int(w/2.):w]#botright

        """
        At this point if a function was provided we call it on each section.
        """
        if f:
            tl = f(tl)
            tr = f(tr)
            bl = f(bl)
            br = f(br)

        if recombine:
            """
            Then if recombine=True, we recombine the images and write them to one file.
            """
            img = np.concatenate((np.concatenate((tl,tr), axis=1), np.concatenate((bl,br), axis=1)), axis=0)
            cv2.imwrite("%s_new%s" % (fname[:-4], fname[-4:]), img)
        else:
            """
            Otherwise we write the individual parts to separate files
            """
            cv2.imwrite("%s_1%s" % (fname[:-4], fname[-4:]), tl)
            cv2.imwrite("%s_2%s" % (fname[:-4], fname[-4:]), tr)
            cv2.imwrite("%s_3%s" % (fname[:-4], fname[-4:]), bl)
            cv2.imwrite("%s_4%s" % (fname[:-4], fname[-4:]), br)

#Simple Demo example
split_and_handle_img_parts()

#Example with opencv resize and recombine
split_and_handle_img_parts(f = lambda img: cv2.resize(img, (0,0), fx=0.20, fy=0.20), recombine=True)


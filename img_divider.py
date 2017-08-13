"""
View the nearby README.txt for info on using this program.
It divides the images given into 4 equally sized sections and saves each as fname_1, fname_2, fname_3, and fname_4.

-Blake Edwards / Dark Element
"""
import cv2
import sys

"""
Check that we have args
"""
if len(sys.argv) < 2:
    print "Image(s) must be supplied for processing, e.g. `python img_divider.py $img1 $img2 $img3`"
    sys.exit()
    
"""
Now loop through filenames and call function on each
"""
for fname in sys.argv[1:]:
    print "Dividing %s..." % fname
    img = cv2.imread(fname)
    h, w = img.shape[0], img.shape[1]
    """
    Divide image into 4 equally sized sections and save each as fname_1, fname_2, fname_3, and fname_4.
    """
    cv2.imwrite("%s_1%s" % (fname[:-4], fname[-4:]), img[:int(h/2.), :int(w/2.)])
    cv2.imwrite("%s_2%s" % (fname[:-4], fname[-4:]), img[:int(h/2.), int(w/2.):w])
    cv2.imwrite("%s_3%s" % (fname[:-4], fname[-4:]), img[int(h/2.):h, :int(w/2.)])
    cv2.imwrite("%s_4%s" % (fname[:-4], fname[-4:]), img[int(h/2.):h, int(w/2.):w])

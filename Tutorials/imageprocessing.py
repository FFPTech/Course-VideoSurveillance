# Install packages
# pip install scikit-image, matplotlib, numpy
 
# import libraries
import skimage as ski # for image processing
import matplotlib.pyplot as plt # for image visualization
import numpy as np # for numerical calculations

# check version
print(ski.__version__)

# Add functions
# image display
def displayImage(image, title, colormap='gray', lockwindow=True):
    plt.figure() # Create figure window
    plt.imshow(image, cmap=colormap) # Display image on figure with chosen colormap
    plt.title(title)
    plt.show(block=lockwindow) # Lock displayed image in figure
    return 

# image filtering
def filterImage(image, threshold):
    image_filtered = image < threshold
    return image_filtered

# image masking
def maskImage(image, mask):
    image_masked = image*mask
    return image_masked

# load image
img = ski.data.camera() #load camera image and assign to variable img

# display image
displayImage(img, "Original Image")
img_f = filterImage(img, 75)
displayImage(img_f, "Filtered Image")
img_m = maskImage(img, img_f)
displayImage(img_m, "Masked Image")
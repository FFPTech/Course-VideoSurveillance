# Install packages
# pip install scikit-image, matplotlib
 
# import libraries
import skimage as ski # for image processing
import matplotlib.pyplot as plt # for image visualization

# check version
print(ski.__version__)

# load image
img = ski.data.camera() #load camera image and assign to variable img
print(type(img))

# filter image using a threshold
thresh = 75
img_filtered = img < thresh

# Display loaded image
plt.figure() # Create figure window
plt.imshow(img, cmap='gray') # Display image on figure with 'gray' colormap
plt.title('original image')
plt.show(block=False) # Show displayed image in figure

# Display loaded image
plt.figure() # Create figure window
plt.imshow(img_filtered, cmap='gray') # Display image on figure with 'gray' colormap
plt.title('filtered image')
plt.show(block=True) # Show displayed image in figure
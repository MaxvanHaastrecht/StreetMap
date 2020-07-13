from PIL import Image

# Open images, assumed to be in directory from StreetMap.py street plots.
doetinchem = Image.open('doetinchem.png')
groningen = Image.open('groningen.png')
utrecht = Image.open('utrecht.png')
zwolle = Image.open('zwolle.png')

# Retrieve width and height original images.
width = doetinchem.size[0]
height = doetinchem.size[1]

# Create new image, twice as large in both dimensions.
new_im = Image.new('RGB', (width*2,height*2))

# Paste images in new image.
new_im.paste(doetinchem, (0,0)) # top-left
new_im.paste(groningen, (width,0)) # top-right
new_im.paste(zwolle, (0,height)) # bottom-left
new_im.paste(utrecht, (width,height)) # bottom-right

# Save as jpeg and show image. Quality ranges from 1 (worst) to 95 (best).
new_im.save('city_grid.jpg', 'jpeg', quality=95)
new_im.show()

import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')

# build a list of 9 images which have different colors
font = ImageFont.truetype("readonly/fanwood-webfont.ttf", 50)
images=[]
for i in range(9):
    ic=PIL.Image.new(image.mode, (image.width,image.height+40))
    ic.paste(image, (0, 0))
    draw = ImageDraw.Draw(ic)
    text = 'channel {} intensity {}'.format(i//3,0.1+(i%3)*0.4)
    draw.text((0, image.height), text, font = font, align ="left") 
    images.append(ic)

# create a contact sheet from colors
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for i in range(9):
    px=images[i].load()
    for j in range(first_image.width):
        for k in range(first_image.height):
            cl=list(px[j,k])
            cl[i//3]=int(cl[i//3]*(0.1+(i%3)*0.4))
            px[j,k]=tuple(cl)
            
for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)

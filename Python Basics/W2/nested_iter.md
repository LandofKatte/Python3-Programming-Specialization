# Nested Iteration: Image Processing

Two dimensional tables have both rows and columns. You have probably seen many tables like this if you have used a spreadsheet program. Another object that is organized in rows and columns is a digital image. In this section we will explore how iteration allows us to manipulate these images.

A digital image is a finite collection of small, discrete picture elements called pixels. These pixels are organized in a two-dimensional grid. Each pixel represents the smallest amount of picture information that is available. Sometimes these pixels appear as small “dots”.

Each image (grid of pixels) has its own width and its own height. The width is the number of columns and the height is the number of rows. We can name the pixels in the grid by using the column number and row number. However, it is very important to remember that computer scientists like to start counting with 0! This means that if there are 20 rows, they will be named 0,1,2, and so on through 19. This will be very useful later when we iterate using range.

In the figure below, the pixel of interest is found at column c and row r.

![image](https://user-images.githubusercontent.com/103328611/201219808-9754ae89-c1f1-4d9e-994c-10b7d545b398.png)

# The RGB Color Model

Each pixel of the image will represent a single color. The specific color depends on a formula that mixes various amounts of three basic colors: red, green, and blue. This technique for creating color is known as the RGB Color Model. The amount of each color, sometimes called the intensity of the color, allows us to have very fine control over the resulting color.

The minimum intensity value for a basic color is 0. For example if the red intensity is 0, then there is no red in the pixel. The maximum intensity is 255. This means that there are actually 256 different amounts of intensity for each basic color. Since there are three basic colors, that means that you can create 2563 distinct colors using the RGB Color Model.

Here are the red, green and blue intensities for some common colors. Note that “Black” is represented by a pixel having no basic color. On the other hand, “White” has maximum values for all three basic color components.

| Color | Red | Green | Blue |
--|--|--|--|
| Red | 255 | 0 | 0 |
| Green | 0 | 255 | 0 |
| Blue | 0 | 0 | 255 |
| White | 225 | 225 | 255 |
| Black | 0 | 0 | 0 |
| Yellow | 225 | 225 | 0 |
| Magenta | 225 | 0 | 255 |

In order to manipulate an image, we need to be able to access individual pixels. This capability is provided by a module called image, provided in ActiveCode 1. The image module defines two classes: Image and Pixel.

1 If you want to explore image processing on your own outside of the browser you can install the cImage module from http://pypi.org.

Each Pixel object has three attributes: the red intensity, the green intensity, and the blue intensity. A pixel provides three methods that allow us to ask for the intensity values. They are called getRed, getGreen, and getBlue. In addition, we can ask a pixel to change an intensity value using its setRed, setGreen, and setBlue methods.

Method Name
	
Example
	
Explanation

Pixel(r,g,b)
	
Pixel(20,100,50)

Create a new pixel with 20 red, 100 green, and 50 blue.

getRed()
	
r = p.getRed()

Return the red component intensity.

getGreen()
	
r = p.getGreen()
	
Return the green component intensity.

getBlue()

r = p.getBlue()
	
Return the blue component intensity.

setRed()
	
p.setRed(100)

Set the red component intensity to 100.

setGreen()
	
p.setGreen(45)
	
Set the green component intensity to 45.

setBlue()
	
p.setBlue(156)
	
Set the blue component intensity to 156.

In the example below, we first create a pixel with 45 units of red, 76 units of green, and 200 units of blue. We then print the current amount of red, change the amount of red, and finally, set the amount of blue to be the same as the current amount of green.
```
import image

p = image.Pixel(45, 76, 200)
print(p.getRed())
p.setRed(66)
print(p.getRed())
p.setBlue(p.getGreen())
print(p.getGreen(), p.getBlue())

45
66
76 76
```


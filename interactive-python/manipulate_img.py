import cImage as image

img = image.Image('smile.gif')
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()

for col in range(img.getWidth()):
  for row in range(img.getHeight()):
    p = img.getPixel(col, row)
    newred = p.getRed()
    newgreen = 0
    newblue = 0

    newpixel = image.Pixel(newred, newgreen, newblue)
    newimg.setPixel(col, row, newpixel)

newimg.draw(win)
win.exitonclick()


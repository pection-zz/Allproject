from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

photo = Image.open(‘yourimage/filename.jpg’)
 
#Store image width and height
w, h = photo.size
print(w,h)
drawing = ImageDraw.Draw(photo)
font = ImageFont.truetype(“RobotoBlack.ttf”, 68)
text = “© Robbert Brouwers   “
text_w, text_h = drawing.textsize(text, font)
pos = w — text_w, (h — text_h) — 50
_text = Image.new('RGB', (text_w, (text_h)), color = '#000000')
drawing = ImageDraw.Draw(c_text)
drawing.text((0,0), text, fill="#ffffff", font=font)
c_text.putalpha(100)
photo.paste(c_text, pos, c_text)
photo.save('yourimage/filename_out.jpg')
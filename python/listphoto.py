from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import glob
def copyright_apply(input_image_path,
 output_image_path,
 text):
	photo = Image.open(input_image_path)

	#Store image width and heigth
	w, h = photo.size
	#print(w, h )
	# make the image editable
	drawing = ImageDraw.Draw(photo)
	black = (3, 8, 12)
	font = ImageFont.truetype("Helvetica.ttc",15)
	#get text width and heigth
	text = "© 2020 MN Furniture Store" + text + " "
	text_w, text_h = drawing.textsize(text, font)

	pos = w - text_w, (h - text_h) - 50

	c_text = Image.new('RGB', (text_w, (text_h)), color = '#000000')
	drawing = ImageDraw.Draw(c_text)

	drawing.text((0,0), text, fill="#ffffff", font=font)
	c_text.putalpha(150)


	photo.paste(c_text, pos, c_text)
	photo.save(output_image_path)
list = glob.glob("/Users/pection/Documents/MN_Business/Picture/Nowatermark/*.*")
for photo in list:
 
	 out = photo.replace("Nowatermark","Watermark")
	 copyright_apply(photo,
	 out,
	 "MN. Fornitures")
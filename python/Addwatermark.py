from PIL import Image, ImageFilter, ImageFont, ImageDraw
import glob , os ,natsort
def copyright_apply(input_image_path,
 output_image_path,
 text):
	photo = Image.open(input_image_path)
	# logo = Image.open('/Users/pection/Documents/MN_Business/LOGO/21.png')
	# watermark  = Image.open('/Users/pection/Documents/MN_Business/LOGO/WaterMarkB.png')
	#Store image width and heigth
	w, h = photo.size
	# logo.paste(photo,(0,0))
	# watermark.paste(photo)
	# make the image editable
	drawing = ImageDraw.Draw(photo)
	black = (3, 8, 12)
	font = ImageFont.truetype("Helvetica.ttc",15)
	#get text width and heigth
	text = "© 2020 " + text + " "
	text_w, text_h = drawing.textsize(text, font)
	text_h+=3
	pos = (w - text_w)-30, (h - text_h) -30

	c_text = Image.new('RGB', (text_w+20, (text_h)), color = '#000000')
	drawing = ImageDraw.Draw(c_text)

	drawing.text((10,0), text, fill="#ffffff", font=font)
	c_text.putalpha(255)


	photo.paste(c_text, pos, c_text)
	photo.save(output_image_path)
list = glob.glob('/Users/pection/Documents/MN_Business/Picture/Nowatermark/*.*')
listsort = natsort.natsorted(list)

for photo in listsort:
	name = photo.replace("/Users/pection/Documents/MN_Business/Picture/Nowatermark/ProductnumberHead","")
	# print (name)
	name=name.replace(".png","")
	out = photo.replace("Nowatermark","Watermark")
	copyright_apply(photo,
	out,
	"Product number : "+ str(name))
	 # catagory +=1

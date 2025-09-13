from PIL import Image, ImageDraw, ImageFont

# Load background image(btw credits to the Campus Access) 
background_img = Image.open('images/background_img.jpg')

# Create rectangle using Draw() function for the container of the text
rectangle = ImageDraw.Draw(background_img)
rectangle.rectangle([(0, 0), (5000, 300)], fill="white")

# Import ImageFont for the font style and size
large_font = ImageFont.truetype("arial.ttf", 42)
medium_font = ImageFont.truetype("arial.ttf", 24)

rectangle.text((50, 100), "POV: Me and my classmates frantically looking for our mayor last minute before attendance submission", fill="black", font=large_font)

# Add images(cats) to the background(using paste() function)
cat1 = Image.open('images/cat1.png')
background_img.paste(cat1, (200, 1000))

cat2 = Image.open('images/cat2.png')
overlay_cat2 = cat2.resize((300, 300)) # Made a variable for the resizing of the image
background_img.paste(overlay_cat2, (500, 1000)) # Paste(add) resized image to the background 
rectangle.text((520, 1000), "asa man ka, japppp!!!!", fill="white", font=medium_font) #Adding a text

cat3 = Image.open('images/cat3.png')
overlay_cat3 = cat3.resize((300, 300))
background_img.paste(overlay_cat3, (100, 600))
rectangle.text((120, 600), "japppp!!!!", fill="white", font=medium_font)

cat4 = Image.open('images/cat4.png')
overlay_cat4 = cat4.resize((300, 300))
background_img.paste(overlay_cat4, (1500, 600))

cat5 = Image.open('images/cat5.png')
overlay_cat5 = cat5.resize((300, 300))
background_img.paste(overlay_cat5, (1010, 1010))
rectangle.text((1010, 1010), "Pwede paapil ko attendanc? >.<", fill="white", font=medium_font)

cat6 = Image.open('images/cat6.png')
overlay_cat6 = cat6.resize((400, 300))
background_img.paste(overlay_cat6, (800, 600))
rectangle.text((800, 600), "naka attendance namo?", fill="white", font=medium_font)

cat7 = Image.open('images/cat7.png')
overlay_cat7 = cat7.resize((300, 300))
background_img.paste(overlay_cat7, (1400, 800))

cat8 = Image.open('images/cat8.png')
overlay_cat8 = cat8.resize((300, 300))
background_img.paste(overlay_cat8, (1200, 400))

# Save image
background_img.save("CSELEC3_3A_AbarquezAga_Activity1.png")
# Load image 
image = Image.open("CSELEC3_3A_AbarquezAga_Activity1.png")
# Display image
image.show()


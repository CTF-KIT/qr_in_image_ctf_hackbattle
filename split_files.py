from PIL import Image
from tqdm import tqdm

files_count = 211600

file_pattern = "output/{}.png"

height = 460
width = 460

img=Image.new('L', (height,width))

for n in tqdm(range(files_count)):
	x = n % width
	y = n // height

	pixel = Image.open(
		file_pattern.format(n)
	)

	img.paste(pixel, (x,y))

 
img.save("out.png")
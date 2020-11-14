import codecs
from tqdm import tqdm

f = open("task.png", "rb")
content = f.read()
f.close()

output_files = "output/{}.png"

image = b''

find_hex = ['42','60','82']
tryes = 0
file_num = 0

for i in tqdm(range(len(content))):
	c = content[i]

	image += c

	if codecs.encode(c, "hex") == find_hex[tryes]:
		tryes += 1
	else:
		tryes = 0

	if tryes >= len(find_hex):

		path_file = output_files.format(file_num)

		f = open(path_file, "ab")
		f.write(image)
		f.close()

		image=b''
		tryes=0

		file_num += 1


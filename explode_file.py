import codecs
from tqdm import tqdm
import hashlib

f = open("task.png", "rb")
content = f.read()
f.close()

output_files = "output/{}.png"

image = b''
hashes = {}

find_hex = ['42','60','82']
t = 0
n = 0

for i in tqdm(range(len(content))):
	c = content[i]

	image += c

	if codecs.encode(c, "hex") == find_hex[t]:
		t += 1
	else:
		t = 0

	if t >= len(find_hex):

		path_file = output_files.format(n)

		f = open(path_file, "ab")
		f.write(image)
		f.close()

		hash = hashlib.sha1(image).hexdigest()

		if hash not in hashes:
			hashes[hash] = 1
		else:
			hashes[hash] += 1

		image=b''
		t=0

		n += 1


print("images: {}\nHashes: {}".format(n, len(hashes)))
print(hashes)


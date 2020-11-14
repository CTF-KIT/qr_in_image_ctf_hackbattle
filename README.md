# ([All-in task](https://github.com/SPbCTF/hackbattle-phdays2019/tree/master/all_in))

* **solution:**

`$ exiftool task.png`

```
ExifTool Version Number         : 10.80
File Name                       : task.png
Directory                       : .
File Size                       : 14 MB
File Modification Date/Time     : 2019:05:08 12:14:40+01:00
File Access Date/Time           : 2020:11:14 19:21:43+00:00
File Inode Change Date/Time     : 2020:11:14 19:21:36+00:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1
Image Height                    : 1
Bit Depth                       : 1
Color Type                      : Grayscale
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Warning                         : [minor] Trailer data after PNG IEND chunk
Image Size                      : 1x1
Megapixels                      : 0.000001
```

line: **Warning                         : [minor] Trailer data after PNG IEND chunk**

*looks interesting...*

* **explode_file.py for unpack images**

* **split_files.py for split images in one**

!["QR CODE"](https://sun9-16.userapi.com/rcInahSKKgOhiIYpqKIZdOR05KLNZaEfpF_UKQ/eOS_YohHVBk.jpg "out qr code")

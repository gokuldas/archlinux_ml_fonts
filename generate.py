 #!/usr/bin/env python
from urllib.request import urlopen
from hashlib import md5

with open("./proto/urllist.txt", 'r') as f:
    urls = f.readlines()

sfile = "\n"
smd5  = "\n"

urls = [i.strip() for i in urls]
n = len(urls)

for count, i in enumerate(urls):
    print("Processing({:2d}/{:2d}): {}".format(count + 1, n, i))
    req = urlopen(i)
    data = req.read()
    chks = md5(data).hexdigest()
    print("MD5 checksum: {}\n".format(chks))
    sfile += "\'{}\'\n".format(i)
    smd5  += "\'{}\'\n".format(chks)
    
with open("./proto/PKGBUILD.proto", 'r') as f:
    pkgbuild = f.read()

pkgbuild = pkgbuild.replace("SRC_URLS", sfile)
pkgbuild = pkgbuild.replace("MD5_SUMS", smd5)

with open("./PKGBUILD", 'w') as f:
    f.write(pkgbuild)
    
from shutil import copyfile
copyfile("./proto/ttf-malayalam-smc-fonts.install.proto", 
         "./ttf-malayalam-smc-fonts.install")

print("PKGBUILD & .install created")

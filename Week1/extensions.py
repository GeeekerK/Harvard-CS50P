a = {".gif":"image/gif",
     ".jpg":"image/jpeg",
     ".jpeg":"image/jpeg",
     ".png":"image/png",
     ".pdf":"application/pdf",
     ".zip":"application/zip"}
b = input("plz input").strip().lower()
if  b[b.rfind("."):] in a:
    print(a[b[b.rfind("."):]])
else:
    print("application/octet-stream")

#types = {
#    "gif": "image/gif",
#    "jpg": "image/jpeg",
#    "jpeg": "image/jpeg",
#    "png": "image/png",
#    "pdf": "application/pdf",
#    "txt": "text/plain",
#    "zip": "application/zip",
#}
#s = input("File name: ").strip().lower().split(".")[-1]
#print(types.get(s, "application/octet-stream"))


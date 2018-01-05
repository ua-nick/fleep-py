import fleep

with open("testfile", "rb") as file:
    info = fleep.get(file.read(128))

print(info.type)
print(info.extension)
print(info.mime)

print(info.type_matches("image"))
print(info.extension_matches("gif"))
print(info.mime_matches("image/png"))

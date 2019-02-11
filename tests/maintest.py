import fleep

with open("testfile", "rb") as file:
    info = fleep.get(file.read(128))

assert info.type == ["raster-image"]
assert info.extension == ["png"]
assert info.mime == ["image/png"]

assert info.type_matches("raster-image")
assert info.extension_matches("png")
assert info.mime_matches("image/png")

with open("testfile-mp3", "rb") as file:
    info = fleep.get(file.read(128))

assert info.type == ["audio"]
assert info.extension == ["mp3"]
assert info.mime == ["audio/mpeg"]

assert info.type_matches("audio")
assert info.extension_matches("mp3")
assert info.mime_matches("audio/mpeg")

import fleep

def test_file(filename, type, extension, mime):
    with open(filename, "rb") as file:
        info = fleep.get(file.read(128))

    assert info.type == [type]
    assert info.extension == [extension]
    assert info.mime == [mime]

    assert info.type_matches(type)
    assert info.extension_matches(extension)
    assert info.mime_matches(mime)

test_file("testfile", "raster-image", "png", "image/png")
test_file("test.mp3", "audio", "mp3", "audio/mpeg")
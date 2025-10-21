READERS = {
    'gif': GIFReader,
    'jpg': JPEGReader,
    'png': PNGReader,
}

def get_image_reader(path):
    reader_class = READERS[extension_of(path)]
    return reader_class(path)
from __future__ import absolute_import

import os
from io import BytesIO

from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile

from ckeditor_uploader import utils

try:
    from PIL import Image, ImageOps, ImageEnhance
except ImportError:
    import Image
    import ImageOps


THUMBNAIL_SIZE = (75, 75)


def reduce_opacity(im, opacity):
    """Returns an image with reduced opacity."""
    assert opacity >= 0 and opacity <= 1
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im

def watermark(im, mark, position, opacity=1):
    """Adds a watermark to an image."""
    if opacity < 1:
        mark = reduce_opacity(mark, opacity)
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    # create a transparent layer the size of the image and draw the
    # watermark in that layer.
    layer = Image.new('RGBA', im.size, (0,0,0,0))
    if position == 'tile':
        for y in range(0, im.size[1], mark.size[1]):
            for x in range(0, im.size[0], mark.size[0]):
                layer.paste(mark, (x, y))
    elif position == 'scale':
        # scale, but preserve the aspect ratio
        ratio = min(
            float(im.size[0]) / mark.size[0], float(im.size[1]) / mark.size[1])
        w = int(mark.size[0] * ratio)
        h = int(mark.size[1] * ratio)
        mark = mark.resize((w, h))
        layer.paste(mark, ((im.size[0] - w) / 2, (im.size[1] - h) / 2))
    else:
        layer.paste(mark, position)
    # composite the watermark with the layer
    return Image.composite(layer, im, layer)


def image_verify(f):
    try:
        Image.open(f).verify()
    except IOError:
        raise utils.NotAnImageException


def create_thumbnail(file_path):
    thumbnail_filename = utils.get_thumb_filename(file_path)
    thumbnail_format = utils.get_image_format(os.path.splitext(file_path)[1])

    image = default_storage.open(file_path)
    image = Image.open(image)
    file_format = image.format

    # Convert to RGB if necessary
    # Thanks to Limodou on DjangoSnippets.org
    # http://www.djangosnippets.org/snippets/20/
    if image.mode not in ('L', 'RGB'):
        image = image.convert('RGB')

    # scale and crop to thumbnail
    imagefit = ImageOps.fit(image, THUMBNAIL_SIZE, Image.ANTIALIAS)
    thumbnail_io = BytesIO()
    imagefit.save(thumbnail_io, format=file_format)

    thumbnail = InMemoryUploadedFile(
        thumbnail_io,
        None,
        thumbnail_filename,
        thumbnail_format,
        len(thumbnail_io.getvalue()),
        None)
    thumbnail.seek(0)

    return default_storage.save(thumbnail_filename, thumbnail)


def save_compressed(file_path):
    compressed_filename = file_path
    compressed_format = utils.get_image_format(os.path.splitext(file_path)[1])

    image_path = default_storage.open(file_path)
    image = Image.open(image_path)
    file_format = image.format

    # Convert to RGB if necessary
    # Thanks to Limodou on DjangoSnippets.org
    # http://www.djangosnippets.org/snippets/20/
    if image.mode not in ('L', 'RGB'):
        image = image.convert('RGB')

    # scale and crop to compressed
    mark_path = default_storage.open('logo.png')
    mark = Image.open(mark_path)
    imagefit = image
    compressed_io = BytesIO()
    imagefit.save(compressed_io, format=file_format, quality=70)

    compressed = InMemoryUploadedFile(
        compressed_io,
        None,
        compressed_filename,
        compressed_format,
        len(compressed_io.getvalue()),
        None)
    compressed.seek(0)
    image_path.close()
    mark_path.close()
    return default_storage.save(compressed_filename, compressed)


def should_create_thumbnail(file_path):
    image = default_storage.open(file_path)
    try:
        Image.open(image)
    except IOError:
        return False
    else:
        return utils.is_valid_image_extension(file_path)

from __future__ import absolute_import

from django.conf import settings


def get_backend():
    backend = getattr(settings, "CKEDITOR_IMAGE_BACKEND", None)
    from ckeditor_uploader.image import pillow_backend as backend

    return backend

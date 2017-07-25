from django.core.urlresolvers import reverse

from ckeditor import widgets


class CKEditorUploadingWidget(widgets.CKEditorWidget):
    def _set_config(self):
        if 'filebrowserUploadUrl' not in self.config:
            self.config.setdefault('filebrowserUploadUrl', '/ckeditor/upload')
        if 'filebrowserBrowseUrl' not in self.config:
            self.config.setdefault('filebrowserBrowseUrl', '/ckeditor/browse')
        super(CKEditorUploadingWidget, self)._set_config()

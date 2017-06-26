from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.

class Timestampable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        super().save()


class Photo(Timestampable):
    photo = models.ImageField()
    caption = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.pk


class Gallery(Timestampable):
    name = models.CharField(max_length=255)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Package(Timestampable):
    title = models.CharField(max_length=1024)
    slug = models.SlugField(unique=True)
    subTitle = models.CharField(max_length=1024, null=True, blank=True)
    titlePic = models.ImageField(null=True, blank=True)
    caption = models.CharField(max_length=255, null=True, blank=True)
    body = RichTextField()
    price = models.FloatField(default=0, null=True, blank=True)
    discount = models.FloatField(default=0, null=True, blank=True)
    gallery = models.OneToOneField(Gallery, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Place(Timestampable):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Days(Timestampable):
    min = models.IntegerField(default=0)
    max = models.IntegerField(default=0)

    def __str__(self):
        return str(str(self.min) + "-" + str(self.max) + " Days ")


class Season(Timestampable):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Itenary(Timestampable):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    day = models.CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return self.name


class Blog(Timestampable):
    author = models.CharField(max_length=255, null=True, blank=True)
    authorPic = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    subTitle = models.CharField(max_length=255, null=True, blank=True)
    titlePic = models.ImageField(null=True, blank=True)
    caption = models.CharField(max_length=255, null=True, blank=True)
    body = RichTextField()

    def __str__(self):
        return self.title


class Comment(Timestampable):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Page(Timestampable):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body = RichTextField()

    def __str__(self):
        return self.title

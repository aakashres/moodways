from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse


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


class Gallery(Timestampable):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse("website:galleryDetail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"


class Photo(Timestampable):
    photo = models.ImageField()
    caption = models.CharField(max_length=255, null=True, blank=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    def __str__(self):
        return self.gallery.name + " " + str(self.pk)

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"


class Place(Timestampable):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Place"
        verbose_name_plural = "Places"


class Days(Timestampable):
    min = models.IntegerField(default=0)
    max = models.IntegerField(default=0)

    def __str__(self):
        return str(str(self.min) + "-" + str(self.max) + " Days ")

    class Meta:
        verbose_name = "Day"
        verbose_name_plural = "Days"


class Season(Timestampable):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Season"
        verbose_name_plural = "Seasons"


class Package(Timestampable):
    title = models.CharField(max_length=1024)
    slug = models.SlugField(unique=True)
    subTitle = models.CharField(max_length=1024, null=True, blank=True)
    titlePic = models.ImageField(null=True, blank=True)
    caption = models.CharField(max_length=255, null=True, blank=True)
    body = RichTextField()
    price = models.FloatField(default=0, null=True, blank=True)
    discount = models.FloatField(default=0, null=True, blank=True)
    gallery = models.ForeignKey(Gallery, null=True, blank=True)
    place = models.ForeignKey(Place, null=True, blank=True)
    day = models.ForeignKey(Days, null=True, blank=True)
    season = models.ForeignKey(Season, null=True, blank=True)
    is_promotional = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("website:packageDetail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Package"
        verbose_name_plural = "Packages"


class Itenary(Timestampable):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    day = models.CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return self.day

    class Meta:
        verbose_name = "Iternary"
        verbose_name_plural = "Iternaries"
        ordering = ["day"]


class Blog(Timestampable):
    author = models.CharField(max_length=255, null=True, blank=True)
    authorPic = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    subTitle = models.CharField(max_length=255, null=True, blank=True)
    titlePic = models.ImageField(null=True, blank=True)
    caption = models.CharField(max_length=255, null=True, blank=True)
    body = RichTextField()

    def get_absolute_url(self):
        return reverse("website:frontBlogDetail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ('-created_at',)


class Comment(Timestampable):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class Page(Timestampable):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"


class Booking(Timestampable):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    person = models.PositiveIntegerField(default=1)
    travelDate = models.DateField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    discount_code = models.CharField(max_length=15,null=True, blank=True)
    comments = models.TextField()

    def __str__(self):
        return self.name + " " + self.package.title


class Menu(Timestampable):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=50, help_text='/pages/1/')
    priority = models.IntegerField(
        help_text='Lower number comes first in menu', null=False, blank=False)
    parent = models.ForeignKey(
        'self', related_name='children', null=True, blank=True)

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
        ordering = ['priority', ]

    @staticmethod
    def get_root():
        return Menu.objects.filter(title="root").get()

    def not_deleted_children(self):
        return self.children.filter(deleted_at=None)

    def __str__(self):
        if self.parent:
            if self.parent.title != "root":
                return self.parent.title + ' : ' + self.title
        return self.title


FILE_CHOICES = (
    (1, 'Photo'),
    (2, 'Video')
)


class Slider(Timestampable):
    file = models.FileField(null=True, blank=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    fileType = models.PositiveIntegerField(default=1, choices=FILE_CHOICES)

    def __str__(self):
        return str(self.pk)


class Trailer(Timestampable):
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return str(self.pk)


class Coupon(Timestampable):
    title = models.CharField(max_length=255)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount_percent = models.FloatField(default=0)

    def __str__(self):
        return self.title

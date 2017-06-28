from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^test/$', Test.as_view(), name="test"),

    url(r'^moodwaysAdmin/gallery/create/$',
        GalleryCreateView.as_view(), name="galleryCreate"),
    url(r'^moodwaysAdmin/gallery/list/$',
        GalleryListView.as_view(), name="galleryList"),
    url(r'^moodwaysAdmin/gallery/(?P<pk>\d+)/update/$',
        GalleryUpdateView.as_view(), name="galleryUpdate"),
    url(r'^moodwaysAdmin/gallery/(?P<pk>\d+)/$',
        GalleryDetailView.as_view(), name="galleryDetail"),
    url(r'^moodwaysAdmin/photo/(?P<pk>\d+)/update/$',
        PhotoUpdateView.as_view(), name="photoUpdate"),

    url(r'^moodwaysAdmin/gallery/(?P<pk>\d+)/delete/$',
        GalleryDeleteView.as_view(), name="galleryDelete"),
    url(r'^moodwaysAdmin/photo/(?P<pk>\d+)/delete/$',
        PhotoDeleteView.as_view(), name="photoDelete"),


    url(r'^moodwaysAdmin/place/create/$',
        PlaceCreateView.as_view(), name="placeCreate"),
    url(r'^moodwaysAdmin/place/list/$',
        PlaceListView.as_view(), name="placeList"),
    url(r'^moodwaysAdmin/place/(?P<pk>\d+)/update/$',
        PlaceUpdateView.as_view(), name='placeUpdate'),
    url(r'^moodwaysAdmin/place/(?P<pk>\d+)/delete/$',
        PlaceDeleteView.as_view(), name="placeDelete"),


    url(r'^moodwaysAdmin/days/create/$',
        DaysCreateView.as_view(), name="daysCreate"),
    url(r'^moodwaysAdmin/days/list/$',
        DaysListView.as_view(), name="daysList"),
    url(r'^moodwaysAdmin/days/(?P<pk>\d+)/update/$',
        DaysUpdateView.as_view(), name="daysUpdate"),
    url(r'^moodwaysAdmin/days/(?P<pk>\d+)/delete/$',
        DaysDeleteView.as_view(), name="daysDelete"),


    url(r'^moodwaysAdmin/season/create/$',
        SeasonCreateView.as_view(), name="seasonCreate"),
    url(r'^moodwaysAdmin/season/list/$',
        SeasonListView.as_view(), name="seasonList"),
    url(r'^moodwaysAdmin/season/(?P<pk>\d+)/update/$',
        SeasonUpdateView.as_view(), name='seasonUpdate'),
    url(r'^moodwaysAdmin/season/(?P<pk>\d+)/delete/$',
        SeasonDeleteView.as_view(), name="seasonDelete"),

    url(r'^moodwaysAdmin/page/create/$',
        PageCreateView.as_view(), name="pageCreate"),
    url(r'^moodwaysAdmin/page/list/$',
        PageListView.as_view(), name="pageList"),
    url(r'^moodwaysAdmin/page/(?P<pk>\d+)/update/$',
        PageUpdateView.as_view(), name='pageUpdate'),
    url(r'^moodwaysAdmin/page/(?P<pk>\d+)/$',
        PageDetailView.as_view(), name='pageDetail'),
    url(r'^moodwaysAdmin/page/(?P<pk>\d+)/delete/$',
        PageDeleteView.as_view(), name="pageDelete"),

    url(r'^moodwaysAdmin/blog/create/$',
        BlogCreateView.as_view(), name="blogCreate"),
    url(r'^moodwaysAdmin/blog/list/$',
        BlogListView.as_view(), name="blogList"),
    url(r'^moodwaysAdmin/blog/(?P<pk>\d+)/update/$',
        BlogUpdateView.as_view(), name='blogUpdate'),
    url(r'^moodwaysAdmin/blog/(?P<pk>\d+)/$',
        BlogDetailView.as_view(), name='blogDetail'),
    url(r'^moodwaysAdmin/blog/(?P<pk>\d+)/delete/$',
        BlogDeleteView.as_view(), name="blogDelete"),


    url(r'^moodwaysAdmin/package/create/$',
        PackageCreateView.as_view(), name="packageCreate"),
    url(r'^moodwaysAdmin/package/list/$',
        PackageListView.as_view(), name="packageList"),
    url(r'^moodwaysAdmin/package/(?P<pk>\d+)/update/$',
        PackageUpdateView.as_view(), name="packageUpdate"),
    url(r'^moodwaysAdmin/package/(?P<pk>\d+)/$',
        PackageDetailView.as_view(), name="packageDetail"),
    url(r'^moodwaysAdmin/itenary/(?P<pk>\d+)/update/$',
        ItenaryUpdateView.as_view(), name="itenaryUpdate"),

    url(r'^moodwaysAdmin/package/(?P<pk>\d+)/delete/$',
        PackageDeleteView.as_view(), name="packageDelete"),
    url(r'^moodwaysAdmin/itenary/(?P<pk>\d+)/delete/$',
        ItenaryDeleteView.as_view(), name="itenaryDelete"),


    url(r'^moodwaysAdmin/comment/list/$',
        CommentListView.as_view(), name="commentList"),
    url(r'^moodwaysAdmin/comment/(?P<pk>\d+)/$',
        CommentDetailView.as_view(), name='commentDetail'),
    url(r'^moodwaysAdmin/comment/(?P<pk>\d+)/delete/$',
        CommentDeleteView.as_view(), name="commentDelete"),
]

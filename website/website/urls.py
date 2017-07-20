from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^blog/list/$',
        FrontBlogListView.as_view(), name="frontBlogList"),
    url(r'^blog/(?P<pk>\d+)/$',
        FrontBlogDetailView.as_view(), name='frontBlogDetail'),
    url(r'^page/(?P<slug>[\w-]+)/$',
        FrontPageDetailView.as_view(), name='frontPageDetail'),

    url(r'^package/list/$',
        FrontPackageListView.as_view(), name="frontPackageList"),
    url(r'^package/(?P<slug>[\w-]+)/$',
        FrontPackageDetailView.as_view(), name='frontPackageDetail'),


    url(r'^package/(?P<slug>[\w-]+)/book$',
        FrontPackageBookingView.as_view(), name="frontPackageBooking"),

    url(r'git-pull/$', GitPullView.as_view(), name='git_pull'),


    url(r'^moodwaysAdmin/$', Dashboard.as_view(), name="dashboard_main"),
    url(r'^moodwaysAdmin/dashboard/$', Dashboard.as_view(), name="dashboard"),


    url(r'^register/$', RegistrationView.as_view(), name="register"),
    url(r'^moodwaysAdmin/login/$', LoginView.as_view(), name="login"),
    url(r'^moodwaysAdmin/logout/$', LogoutView.as_view(), name="logout"),

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
    url(r'^moodwaysAdmin/comment/(?P<pk>\d+)/toggle$',
        CommentApproveDisapproveView.as_view(), name='commentToggle'),
    url(r'^moodwaysAdmin/comment/(?P<pk>\d+)/delete/$',
        CommentDeleteView.as_view(), name="commentDelete"),


    url(r'^moodwaysAdmin/menu/list/$',
        MenuListView.as_view(), name='menuList'),
    url(r'^moodwaysAdmin/menu/create/$',
        MenuCreateView.as_view(), name='menuCreate'),
    url(r'^moodwaysAdmin/menu/(?P<pk>[\d]+)/$',
        MenuDetailView.as_view(), name='menuDetail'),
    url(r'^moodwaysAdmin/menu/(?P<pk>[\d]+)/update/$',
        MenuUpdateView.as_view(), name='menuUpdate'),
    url(r'^moodwaysAdmin/menu/(?P<pk>[\d]+)/delete/$',
        MenuDeleteView.as_view(), name='menuDelete'),

    url(r'^moodwaysAdmin/slider/list/$',
        SliderListView.as_view(), name='sliderList'),
    url(r'^moodwaysAdmin/slider/create/$',
        SliderCreateView.as_view(), name='sliderCreate'),
    url(r'^moodwaysAdmin/slider/(?P<pk>[\d]+)/$',
        SliderDetailView.as_view(), name='sliderDetail'),
    url(r'^moodwaysAdmin/slider/(?P<pk>[\d]+)/update/$',
        SliderUpdateView.as_view(), name='sliderUpdate'),
    url(r'^moodwaysAdmin/slider/(?P<pk>[\d]+)/delete/$',
        SliderDeleteView.as_view(), name='sliderDelete'),

    url(r'^moodwaysAdmin/trailer/list/$',
        TrailerListView.as_view(), name='trailerList'),
    url(r'^moodwaysAdmin/trailer/create/$',
        TrailerCreateView.as_view(), name='trailerCreate'),
    url(r'^moodwaysAdmin/trailer/(?P<pk>[\d]+)/$',
        TrailerDetailView.as_view(), name='trailerDetail'),
    url(r'^moodwaysAdmin/trailer/(?P<pk>[\d]+)/update/$',
        TrailerUpdateView.as_view(), name='trailerUpdate'),
    url(r'^moodwaysAdmin/trailer/(?P<pk>[\d]+)/delete/$',
        TrailerDeleteView.as_view(), name='trailerDelete'),

    url(r'^moodwaysAdmin/booking/list/$',
        BookingListView.as_view(), name="bookingList"),
    url(r'^moodwaysAdmin/booking/(?P<pk>[\d]+)/$',
        BookingDetailView.as_view(), name="bookingDetail"),

    url(r'^moodwaysAdmin/coupon/create/$',
        CouponCreateView.as_view(), name="couponCreate"),
    url(r'^moodwaysAdmin/coupon/list/$',
        CouponListView.as_view(), name="couponList"),
    url(r'^moodwaysAdmin/coupon/(?P<pk>\d+)/update/$',
        CouponUpdateView.as_view(), name='couponUpdate'),
    url(r'^moodwaysAdmin/coupon/(?P<pk>\d+)/delete/$',
        CouponDeleteView.as_view(), name='couponDelete'),



]

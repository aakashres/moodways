from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View, CreateView, ListView, DetailView, FormView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.shortcuts import HttpResponseRedirect, HttpResponse


from .models import *
from .forms import *

from django.contrib.auth.mixins import LoginRequiredMixin


class LoginMixin(LoginRequiredMixin):
    login_url = '/moodwaysAdmin/login/'
    redirect_field_name = 'redirect_to'


class HomeMixin(object):
    def get_context_data(self, **kwargs):
        context = super(HomeMixin, self).get_context_data(**kwargs)
        context['menu_root'] = Menu.get_root()
        return context


class Dashboard(HomeMixin, TemplateView):
    template_name = "dashboard.html"


class FrontPageDetailView(HomeMixin, DetailView):
    model = Page
    template_name = 'frontPageDetail.html'


class HomeView(View):
    def get(self, request, *args, **kwargs):
        menu_root = Menu.get_root()
        sliders = Slider.objects.filter(active=True, deleted_at=None)
        trailer = Trailer.objects.filter(deleted_at=None).first()
        promotional_packages = Package.objects.filter(
            deleted_at=None, is_promotional=True)
        blogs = Blog.objects.filter(deleted_at=None).order_by("created_at")[:3]
        places = Place.objects.filter(deleted_at=None)[:6]
        seasons = Season.objects.filter(deleted_at=None)[:6]
        days = Days.objects.filter(deleted_at=None)[:6]
        context = {
            "menu_root": menu_root,
            "sliders": sliders,
            "trailer": trailer,
            "blogs": blogs,
            "places": places,
            "seasons": seasons,
            "days": days,
            "promotional_packages": promotional_packages,
        }
        return render(request, 'home.html', context)


class RegistrationView(View):
    def get(self, request):
        form = UserForm()
        context = {
            'form': form,
        }
        return render(request, 'registration.html', context)

    def post(self, request):
        form = UserForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password2')
            user.set_password(password)
            user.save()

            user = authenticate(username=user.username, password=password)
            messages.success(request, "Registration Successful")
            login(request, user)
            return redirect('website:dashboard')
        else:
            print(userForm.errors)

        context = {
            'form': form,
        }
        return render(request, 'registration.html', context)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            messages.warning(request, 'You are already registered.')
            return redirect('website:dashboard')
        try:
            return super(RegistrationView, self).dispatch(request, *args, **kwargs)
        except:
            return redirect('website:dashboard')



class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'login.html', context)

    def post(self, request):
        redirect = request.GET.get('redirect_to')
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                messages.success(request, "Logged In Successfully")
                login(request, user)
                if redirect:
                    return HttpResponseRedirect(redirect)
                return HttpResponseRedirect('/moodwaysAdmin')
        messages.warning(request, "Log In Failure")
        context = {
            'form': form,
        }
        return render(request, 'login.html', context)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            messages.warning(request, 'You are already logged in.')
            return redirect('website:dashboard')
        return super(LoginView, self).dispatch(request, *args, **kwargs)


class LogoutView(LoginMixin, View):

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(request)
        messages.success(request, "Logged Out Successfully")
        return redirect('website:login')


class GalleryCreateView(LoginMixin, SuccessMessageMixin, CreateView):
    model = Gallery
    template_name = 'galleryCreate.html'
    form_class = GalleryForm
    success_url = reverse_lazy("website:galleryList")
    success_message = "Gallery Successfully Created"


class GitPullView(LoginMixin, View):
    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            import subprocess
            x = subprocess.call(['./pull.sh'])
            return HttpResponse("Pulled and Returned" + str(x))
        return HttpResponse('Failed')


class GalleryUpdateView(LoginMixin, SuccessMessageMixin, UpdateView):
    model = Gallery
    template_name = 'galleryUpdate.html'
    form_class = GalleryForm
    success_url = reverse_lazy("website:galleryList")
    success_message = "Gallery Successfully Updated"


class GalleryDetailView(LoginMixin, FormView):
    form_class = PhotoForm
    template_name = 'galleryDetail.html'

    def dispatch(self, request, *args, **kwargs):
        self.gallery = Gallery.objects.get(pk=kwargs['pk'])
        return super(GalleryDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GalleryDetailView,
                        self).get_context_data(**kwargs)
        context['gallery'] = self.gallery
        context['photos'] = Photo.objects.filter(
            gallery=self.gallery).filter(deleted_at=None)
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.gallery = self.gallery
        instance.save()
        return HttpResponseRedirect(self.gallery.get_absolute_url())


class PhotoUpdateView(LoginMixin, SuccessMessageMixin, UpdateView):
    model = Photo
    template_name = 'photoUpdate.html'
    form_class = PhotoForm
    success_url = reverse_lazy("website:galleryList")
    success_message = "Photo Successfully Updated"


class GalleryListView(LoginMixin, ListView):
    model = Gallery
    template_name = 'galleryList.html'
    context_object_name = 'galleries'

    def get_queryset(self):
        return Gallery.objects.filter(deleted_at=None)


class GalleryDeleteView(LoginMixin, SuccessMessageMixin, DeleteView):
    model = Gallery
    template_name = 'delete.html'
    success_url = reverse_lazy("website:galleryList")
    success_message = "Gallery Successfully Deleted"


class PhotoDeleteView(LoginMixin, SuccessMessageMixin, DeleteView):
    model = Photo
    template_name = 'delete.html'
    success_url = reverse_lazy("website:galleryList")
    success_message = "Photo Successfully Deleted"


class PlaceCreateView(LoginMixin, SuccessMessageMixin, CreateView):
    model = Place
    template_name = 'placeCreate.html'
    form_class = PlaceForm
    success_url = reverse_lazy("website:placeList")
    success_message = "Place Successfully Created"


class PlaceUpdateView(LoginMixin, SuccessMessageMixin, UpdateView):
    model = Place
    template_name = 'placeUpdate.html'
    form_class = PlaceForm
    success_url = reverse_lazy("website:placeList")
    success_message = "Place Successfully Updated"


class PlaceListView(LoginMixin, ListView):
    model = Place
    template_name = 'placeList.html'
    context_object_name = 'places'

    def get_queryset(self):
        return Place.objects.filter(deleted_at=None)


class PlaceDeleteView(LoginMixin, SuccessMessageMixin, DeleteView):
    model = Place
    template_name = 'delete.html'
    success_url = reverse_lazy("website:placeList")
    success_message = "Place Successfully Deleted"


class DaysCreateView(LoginMixin, SuccessMessageMixin, CreateView):
    model = Days
    template_name = 'daysCreate.html'
    form_class = DaysForm
    success_url = reverse_lazy("website:daysList")
    success_message = "Days Successfully Created"


class DaysUpdateView(LoginMixin, SuccessMessageMixin, UpdateView):
    model = Days
    template_name = 'daysUpdate.html'
    form_class = DaysForm
    success_url = reverse_lazy("website:daysList")
    success_message = "Days Successfully Updated"


class DaysListView(LoginMixin, ListView):
    model = Days
    template_name = 'daysList.html'
    context_object_name = 'days'

    def get_queryset(self):
        return Days.objects.filter(deleted_at=None)


class DaysDeleteView(LoginMixin, SuccessMessageMixin, DeleteView):
    model = Days
    template_name = 'delete.html'
    success_url = reverse_lazy("website:daysList")
    success_message = "Days Successfully Deleted"


class SeasonCreateView(LoginMixin, SuccessMessageMixin, CreateView):
    model = Season
    template_name = 'seasonCreate.html'
    form_class = SeasonForm
    success_url = reverse_lazy("website:seasonList")
    success_message = "Season Successfully Created"


class SeasonUpdateView(LoginMixin, SuccessMessageMixin, UpdateView):
    model = Season
    template_name = 'seasonUpdate.html'
    form_class = SeasonForm
    success_url = reverse_lazy("website:seasonList")
    success_message = "Season Successfully Updated"


class SeasonListView(LoginMixin, ListView):
    model = Season
    template_name = 'seasonList.html'
    context_object_name = 'seasons'

    def get_queryset(self):
        return Season.objects.filter(deleted_at=None)


class SeasonDeleteView(LoginMixin, SuccessMessageMixin, DeleteView):
    model = Season
    template_name = 'delete.html'
    success_url = reverse_lazy("website:seasonList")
    success_message = "Season Successfully Deleted"


class PackageCreateView(LoginMixin, SuccessMessageMixin, CreateView):
    model = Package
    template_name = 'packageCreate.html'
    form_class = PackageForm
    success_url = reverse_lazy("website:packageList")
    success_message = "Package Successfully Created"


class PackageUpdateView(LoginMixin, SuccessMessageMixin, UpdateView):
    model = Package
    template_name = 'packageUpdate.html'
    form_class = PackageForm
    success_url = reverse_lazy("website:packageList")
    success_message = "Package Successfully Updated"


class PackageDetailView(LoginMixin, FormView):
    form_class = ItenaryForm
    template_name = 'packageDetail.html'

    def dispatch(self, request, *args, **kwargs):
        self.package = Package.objects.get(pk=kwargs['pk'])
        return super(PackageDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PackageDetailView,
                        self).get_context_data(**kwargs)
        context['package'] = self.package
        context['itenaries'] = Itenary.objects.filter(
            package=self.package).filter(deleted_at=None)
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.package = self.package
        instance.save()
        return HttpResponseRedirect(self.package.get_absolute_url())


class PackageListView(LoginMixin, ListView):
    model = Package
    template_name = 'packageList.html'
    context_object_name = 'packages'

    def get_queryset(self):
        return Package.objects.filter(deleted_at=None)


class ItenaryUpdateView(LoginMixin, SuccessMessageMixin, UpdateView):
    model = Itenary
    template_name = 'itenaryUpdate.html'
    form_class = ItenaryForm
    success_url = reverse_lazy("website:packageList")
    success_message = "Itenary Successfully Updated"


class PackageDeleteView(LoginMixin, SuccessMessageMixin, DeleteView):
    model = Package
    template_name = 'delete.html'
    success_url = reverse_lazy("website:packageList")
    success_message = "Package Successfully Deleted"


class ItenaryDeleteView(LoginMixin, SuccessMessageMixin, DeleteView):
    model = Itenary
    template_name = 'delete.html'
    success_url = reverse_lazy("website:packageDetail", kwargs=self.kwargs)
    success_message = "Itenary Successfully Deleted"


class PageCreateView(LoginMixin, SuccessMessageMixin, CreateView):
    model = Page
    template_name = 'pageCreate.html'
    form_class = PageForm
    success_url = reverse_lazy("website:pageList")
    success_message = "Page Successfully Created"


class PageUpdateView(LoginMixin, SuccessMessageMixin, UpdateView):
    model = Page
    template_name = 'pageUpdate.html'
    form_class = PageForm
    success_url = reverse_lazy("website:pageList")
    success_message = "Page Successfully Updated"


class PageListView(LoginMixin, ListView):
    model = Page
    template_name = 'pageList.html'
    context_object_name = 'pages'

    def get_queryset(self):
        return Page.objects.filter(deleted_at=None)


class PageDetailView(LoginMixin, DetailView):
    model = Page
    template_name = 'pageDetail.html'


class PageDeleteView(LoginMixin, SuccessMessageMixin, DeleteView):
    model = Page
    template_name = 'delete.html'
    success_url = reverse_lazy("website:pageList")
    success_message = "Page Successfully Deleted"


class BlogCreateView(LoginMixin, SuccessMessageMixin, CreateView):
    model = Blog
    template_name = 'blogCreate.html'
    form_class = BlogForm
    success_url = reverse_lazy("website:blogList")
    success_message = "Blog Successfully Created"


class BlogUpdateView(LoginMixin, SuccessMessageMixin, UpdateView):
    model = Blog
    template_name = 'blogUpdate.html'
    form_class = BlogForm
    success_url = reverse_lazy("website:blogList")
    success_message = "Blog Successfully Updated"


class BlogListView(LoginMixin, ListView):
    model = Blog
    template_name = 'blogList.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(deleted_at=None)


class BlogDetailView(LoginMixin, DetailView):
    model = Blog
    template_name = 'blogDetail.html'


class BlogDeleteView(LoginMixin, SuccessMessageMixin, DeleteView):
    model = Blog
    template_name = 'delete.html'
    success_url = reverse_lazy("website:blogList")
    success_message = "Blog Successfully Deleted"


class CommentListView(LoginMixin, ListView):
    model = Comment
    template_name = 'commentList.html'
    context_object_name = 'comments'

    def get_queryset(self):
        return Comment.objects.filter(deleted_at=None)


class CommentDetailView(LoginMixin, DetailView):
    model = Comment
    template_name = 'commentDetail.html'


class CommentApproveDisapproveView(LoginMixin, View):
    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        comment = Comment.objects.get(id=id)
        if comment.approved:
            comment.approved = False
        else:
            comment.approved = True
        comment.save()
        return redirect("website:commentList")


class CommentDeleteView(LoginMixin, SuccessMessageMixin, DeleteView):
    model = Comment
    template_name = 'delete.html'
    success_url = reverse_lazy("website:commentList")
    success_message = "Comment Successfully Deleted"


class MenuCreateView(LoginMixin, SuccessMessageMixin, CreateView):
    model = Menu
    template_name = 'menuCreate.html'
    form_class = MenuForm
    success_url = reverse_lazy("website:menuList")
    success_message = "Menu Successfully Added"


class MenuUpdateView(LoginMixin, SuccessMessageMixin, UpdateView):
    model = Menu
    template_name = 'menuUpdate.html'
    form_class = MenuForm
    success_url = reverse_lazy("website:menuList")
    success_message = "Menu Successfully Updated"


class MenuDeleteView(LoginMixin, SuccessMessageMixin, DeleteView):
    model = Menu
    template_name = 'delete.html'
    success_url = reverse_lazy("website:menuList")
    success_message = "Menu Successfully Deleted"


class MenuDetailView(LoginMixin, DetailView):
    model = Menu
    template_name = 'menuDetail.html'


class MenuListView(LoginMixin, ListView):
    model = Menu
    template_name = 'menuList.html'
    context_object_name = 'menus'

    def get_queryset(self):
        return Menu.objects.filter(deleted_at=None)


class BookingListView(LoginMixin, ListView):
    model = Booking
    template_name = 'bookingList.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(deleted_at=None)


class BookingDetailView(LoginMixin, DetailView):
    model = Booking
    template_name = 'bookingDetail.html'


class SliderCreateView(LoginMixin, SuccessMessageMixin, CreateView):
    model = Slider
    template_name = 'sliderCreate.html'
    form_class = SliderForm
    success_url = reverse_lazy("website:sliderList")
    success_message = "slider Successfully Added"


class SliderUpdateView(LoginMixin, SuccessMessageMixin, UpdateView):
    model = Slider
    template_name = 'sliderUpdate.html'
    form_class = SliderForm
    success_url = reverse_lazy("website:sliderList")
    success_message = "Slider Successfully Updated"


class SliderDeleteView(LoginMixin, SuccessMessageMixin, DeleteView):
    model = Slider
    template_name = 'delete.html'
    success_url = reverse_lazy("website:sliderList")
    success_message = "Slider Successfully Deleted"


class SliderDetailView(LoginMixin, DetailView):
    model = Slider
    template_name = 'sliderDetail.html'


class SliderListView(LoginMixin, ListView):
    model = Slider
    template_name = 'sliderList.html'
    context_object_name = 'photos'

    def get_queryset(self):
        return Slider.objects.filter(deleted_at=None)


class TrailerCreateView(LoginMixin, SuccessMessageMixin, CreateView):
    model = Trailer
    template_name = 'trailerCreate.html'
    form_class = TrailerForm
    success_url = reverse_lazy("website:trailerList")
    success_message = "Trailer Successfully Added"


class TrailerUpdateView(LoginMixin, SuccessMessageMixin, UpdateView):
    model = Trailer
    template_name = 'trailerUpdate.html'
    form_class = TrailerForm
    success_url = reverse_lazy("website:trailerList")
    success_message = "Trailer Successfully Updated"


class TrailerDeleteView(LoginMixin, SuccessMessageMixin, DeleteView):
    model = Trailer
    template_name = 'delete.html'
    success_url = reverse_lazy("website:trailerList")
    success_message = "Trailer Successfully Deleted"


class TrailerDetailView(LoginMixin, DetailView):
    model = Trailer
    template_name = 'trailerDetail.html'


class TrailerListView(LoginMixin, ListView):
    model = Trailer
    template_name = 'trailerList.html'
    context_object_name = 'trailers'

    def get_queryset(self):
        return Trailer.objects.filter(deleted_at=None)


def getDateTime(datetime):
    date, time, meridiem = datetime.split(" ")
    hour, minute = time.split(":")
    if meridiem == "PM":
        hr = int(hour) + 12
        hr %= 24
        hour = str(hr)
    time = hour + ':' + minute
    datetime = date + ' ' + time
    return datetime


class CouponCreateView(LoginMixin, SuccessMessageMixin, CreateView):
    model = Coupon
    template_name = 'couponCreate.html'
    form_class = CouponForm
    success_url = reverse_lazy("website:couponList")
    success_message = "Coupon Successfully Added"

    def form_valid(self, form, **kwargs):
        couponObjects = Coupon.objects.filter(code=form.instance.code)
        if couponObjects:
            messages.error(self.request, "Coupon Code Already Exist!!!")
            return redirect('website:couponCreate')
        else:
            form.instance.valid_from = getDateTime(
                form.cleaned_data.get('validFrom'))
            form.instance.valid_to = getDateTime(
                form.cleaned_data.get('validTo'))
            form.save()

        return super(CouponCreateView, self).form_valid(form, *kwargs)

    def form_invalid(self, form, **kwargs):
        print(form.errors)

        return super(CouponCreateView, self).form_invalid(form, *kwargs)


class CouponUpdateView(LoginMixin, SuccessMessageMixin, UpdateView):
    model = Coupon
    template_name = 'couponUpdate.html'
    form_class = CouponForm
    success_url = reverse_lazy("website:couponList")
    success_message = "Coupon Successfully Updated"

    def form_valid(self, form, **kwargs):
        couponObjects = Coupon.objects.filter(code=form.instance.code)
        if couponObjects:
            messages.error(self.request, "Coupon Code Already Exist!!!")
            return redirect('website:couponCreate')
        else:
            form.instance.valid_from = getDateTime(
                form.cleaned_data.get('validFrom'))
            form.instance.valid_to = getDateTime(
                form.cleaned_data.get('validTo'))
            form.save()

        return super(AdminCouponCreateView, self).form_valid(form, *kwargs)


class CouponListView(LoginMixin, ListView):
    model = Coupon
    template_name = 'couponList.html'
    context_object_name = 'coupons'

    def get_queryset(self):
        return Coupon.objects.filter(deleted_at=None)


class CouponDeleteView(LoginMixin, SuccessMessageMixin, DeleteView):
    model = Coupon
    template_name = 'delete.html'
    success_url = reverse_lazy("website:couponList")
    success_message = "Coupon Successfully Deleted"


class FrontPackageListView(HomeMixin, ListView):
    model = Package
    template_name = 'frontPackageList.html'
    context_object_name = 'packages'
    paginate_by = 9

    def get_queryset(self):
        packages = Package.objects.filter(deleted_at=None)
        query = self.request.GET.get("q")
        places = self.request.GET.getlist("destination")
        seasons = self.request.GET.getlist("season")
        days = self.request.GET.getlist("day")
        if places:
            for place in places:
                packages = packages.filter(
                    Q(place__id__icontains=place)
                ).distinct()
        if seasons:
            for season in seasons:
                packages = packages.filter(
                    Q(season__id__icontains=season)
                ).distinct()
        if days:
            for day in days:
                packages = packages.filter(
                    Q(place__id__icontains=day)
                ).distinct()
        if query:
            packages = packages.filter(
                Q(title__icontains=query) |
                Q(subTitle__icontains=query)
            ).distinct()
        return packages

    def get_context_data(self, **kwargs):
        context = super(FrontPackageListView,
                        self).get_context_data(**kwargs)
        context['promotional_packages'] = Package.objects.filter(
            deleted_at=None, is_promotional=True)[:3]
        return context


class FrontPackageDetailView(DetailView):
    model = Package
    template_name = 'frontPackageDetail.html'

    def dispatch(self, request, *args, **kwargs):
        self.slug = kwargs['slug']
        self.package = Package.objects.get(slug=self.slug)
        return super(FrontPackageDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(FrontPackageDetailView,
                        self).get_context_data(**kwargs)
        context['package'] = self.package
        context['recent'] = Package.objects.all().order_by('created_at')[:6]
        context['itenaryList'] = Itenary.objects.filter(package=self.package)
        gallery = Gallery.objects.filter(package=self.package)
        context['photos'] = Photo.objects.filter(gallery=gallery)

        return context


class FrontBlogListView(HomeMixin, ListView):
    model = Blog
    template_name = 'frontBlogList.html'
    context_object_name = 'blogs'
    paginate_by = 9

    def get_queryset(self):
        blogs = Blog.objects.filter(deleted_at=None)
        query = self.request.GET.get("q")
        if query:
            blogs = blogs.filter(
                Q(title__icontains=query) |
                Q(subTitle__icontains=query)
            ).distinct()
        return blogs


class FrontBlogDetailView(HomeMixin, FormView):
    form_class = CommentForm
    template_name = 'frontBlogDetail.html'

    def dispatch(self, request, *args, **kwargs):
        self.pk = kwargs['pk']
        self.blog = Blog.objects.get(pk=self.pk)
        return super(FrontBlogDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(FrontBlogDetailView,
                        self).get_context_data(**kwargs)
        context['blog'] = self.blog
        context['latest_blogs'] = Blog.objects.all().order_by('created_at')[:3]
        context['comments'] = Comment.objects.filter(
            blog=self.blog, approved=True)
        context['count'] = len(Comment.objects.filter(
            blog=self.blog, approved=True))
        return context

    def form_valid(self, form):
        comment = Comment()
        comment.name = form.cleaned_data.get('name')
        comment.email = form.cleaned_data.get('email')
        comment.body = form.cleaned_data.get('body')
        comment.blog = self.blog
        comment.save()
        return HttpResponseRedirect(self.blog.get_absolute_url())


class FrontPackageBookingView(View):
    def get(self, request, *args, **kwargs):
        form = BookingForm()
        slug = kwargs["slug"]
        self.package = Package.objects.get(slug=slug)
        menu_root = Menu.get_root()
        context = {
            'package': self.package,
            'menu_root': menu_root,
            'form': form,
        }
        return render(request, 'frontBooking.html', context)

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST or None)
        slug = kwargs["slug"]
        self.package = Package.objects.get(slug=slug)
        if form.is_valid():
            form.instance.package = self.package
            form.save()
            return redirect('website:home')
        else:
            print(form.errors)
        menu_root = Menu.get_root()
        context = {
            'package': self.package,
            'menu_root': menu_root,
            'form': form,
        }
        return render(request, 'frontBooking.html', context)

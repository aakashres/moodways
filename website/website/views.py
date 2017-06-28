from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View, CreateView, ListView, DetailView, FormView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q

from .models import *
from .forms import *


class Test(TemplateView):
    template_name = "test.html"


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
            return redirect('website:test')
        else:
            print(userForm.errors)

        context = {
            'form': form,
        }
        return render(request, 'registration.html', context)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            messages.warning(request, 'You are already registered.')
            return redirect('website:test')
        return super(RegistrationView, self).dispatch(request, *args, **kwargs)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'login.html', context)

    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                messages.success(request, "Logged In Successfully")
                login(request, user)
                return redirect('website:test')
        messages.warning(request, "Log In Failure")
        context = {
            'form': form,
        }
        return render(request, 'login.html', context)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            messages.warning(request, 'You are already logged in.')
            return redirect('form:test')
        return super(LoginView, self).dispatch(request, *args, **kwargs)


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(request)
        messages.success(request, "Logged Out Successfully")
        return redirect('website:login')


class GalleryCreateView(SuccessMessageMixin, CreateView):
    model = Gallery
    template_name = 'galleryCreate.html'
    form_class = GalleryForm
    success_url = reverse_lazy("website:test")
    success_message = "Gallery Successfully Created"


class GalleryUpdateView(SuccessMessageMixin, UpdateView):
    model = Gallery
    template_name = 'galleryUpdate.html'
    form_class = GalleryForm
    success_url = reverse_lazy("website:test")
    success_message = "Gallery Successfully Updated"


class GalleryDetailView(FormView):
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
            gallery=self.gallery)
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.gallery = self.gallery
        instance.save()
        return HttpResponseRedirect(self.gallery.get_absolute_url())


class PhotoUpdateView(SuccessMessageMixin, UpdateView):
    model = Photo
    template_name = 'photoUpdate.html'
    form_class = PhotoForm
    success_url = reverse_lazy("website:test")
    success_message = "Photo Successfully Updated"


class GalleryListView(ListView):
    model = Gallery
    template_name = 'galleryList.html'
    context_object_name = 'galleries'

    def get_queryset(self):
        return Gallery.objects.filter(deleted_at=None)


class GalleryDeleteView(SuccessMessageMixin, DeleteView):
    model = Gallery
    template_name = 'delete.html'
    success_url = reverse_lazy("website:test")
    success_message = "Gallery Successfully Deleted"


class PhotoDeleteView(SuccessMessageMixin, DeleteView):
    model = Photo
    template_name = 'delete.html'
    success_url = reverse_lazy("website:test")
    success_message = "Photo Successfully Deleted"


class PlaceCreateView(SuccessMessageMixin, CreateView):
    model = Place
    template_name = 'placeCreate.html'
    form_class = PlaceForm
    success_url = reverse_lazy("website:test")
    success_message = "Place Successfully Created"


class PlaceUpdateView(SuccessMessageMixin, UpdateView):
    model = Place
    template_name = 'placeUpdate.html'
    form_class = PlaceForm
    success_url = reverse_lazy("website:test")
    success_message = "Place Successfully Updated"


class PlaceListView(ListView):
    model = Place
    template_name = 'placeList.html'
    context_object_name = 'places'

    def get_queryset(self):
        return Place.objects.filter(deleted_at=None)


class PlaceDeleteView(SuccessMessageMixin, DeleteView):
    model = Place
    template_name = 'delete.html'
    success_url = reverse_lazy("website:test")
    success_message = "Place Successfully Deleted"


class DaysCreateView(SuccessMessageMixin, CreateView):
    model = Days
    template_name = 'daysCreate.html'
    form_class = DaysForm
    success_url = reverse_lazy("website:test")
    success_message = "Days Successfully Created"


class DaysUpdateView(SuccessMessageMixin, UpdateView):
    model = Days
    template_name = 'daysUpdate.html'
    form_class = DaysForm
    success_url = reverse_lazy("website:test")
    success_message = "Days Successfully Updated"


class DaysListView(ListView):
    model = Days
    template_name = 'daysList.html'
    context_object_name = 'days'

    def get_queryset(self):
        return Days.objects.filter(deleted_at=None)


class DaysDeleteView(SuccessMessageMixin, DeleteView):
    model = Days
    template_name = 'delete.html'
    success_url = reverse_lazy("website:test")
    success_message = "Days Successfully Deleted"


class SeasonCreateView(SuccessMessageMixin, CreateView):
    model = Season
    template_name = 'seasonCreate.html'
    form_class = SeasonForm
    success_url = reverse_lazy("website:test")
    success_message = "Season Successfully Created"


class SeasonUpdateView(SuccessMessageMixin, UpdateView):
    model = Season
    template_name = 'seasonUpdate.html'
    form_class = SeasonForm
    success_url = reverse_lazy("website:test")
    success_message = "Season Successfully Updated"


class SeasonListView(ListView):
    model = Season
    template_name = 'seasonList.html'
    context_object_name = 'seasons'

    def get_queryset(self):
        return Season.objects.filter(deleted_at=None)


class SeasonDeleteView(SuccessMessageMixin, DeleteView):
    model = Season
    template_name = 'delete.html'
    success_url = reverse_lazy("website:test")
    success_message = "Season Successfully Deleted"


class PackageCreateView(SuccessMessageMixin, CreateView):
    model = Package
    template_name = 'packageCreate.html'
    form_class = PackageForm
    success_url = reverse_lazy("website:test")
    success_message = "Package Successfully Created"


class PackageUpdateView(SuccessMessageMixin, UpdateView):
    model = Package
    template_name = 'packageUpdate.html'
    form_class = PackageForm
    success_url = reverse_lazy("website:test")
    success_message = "Package Successfully Updated"


class PackageDetailView(FormView):
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
            package=self.package)
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.package = self.package
        instance.save()
        return HttpResponseRedirect(self.package.get_absolute_url())


class PackageListView(ListView):
    model = Package
    template_name = 'packageList.html'
    context_object_name = 'packages'

    def get_queryset(self):
        return Package.objects.filter(deleted_at=None)


class ItenaryUpdateView(SuccessMessageMixin, UpdateView):
    model = Itenary
    template_name = 'itenaryUpdate.html'
    form_class = ItenaryForm
    success_url = reverse_lazy("website:test")
    success_message = "Itenary Successfully Updated"


class PackageDeleteView(SuccessMessageMixin, DeleteView):
    model = Package
    template_name = 'delete.html'
    success_url = reverse_lazy("website:test")
    success_message = "Package Successfully Deleted"


class ItenaryDeleteView(SuccessMessageMixin, DeleteView):
    model = Itenary
    template_name = 'delete.html'
    success_url = reverse_lazy("website:test")
    success_message = "Itenary Successfully Deleted"


class PageCreateView(SuccessMessageMixin, CreateView):
    model = Page
    template_name = 'pageCreate.html'
    form_class = PageForm
    success_url = reverse_lazy("website:test")
    success_message = "Page Successfully Created"


class PageUpdateView(SuccessMessageMixin, UpdateView):
    model = Page
    template_name = 'pageUpdate.html'
    form_class = PageForm
    success_url = reverse_lazy("website:test")
    success_message = "Page Successfully Updated"


class PageListView(ListView):
    model = Page
    template_name = 'pageList.html'
    context_object_name = 'pages'

    def get_queryset(self):
        return Page.objects.filter(deleted_at=None)


class PageDetailView(DetailView):
    model = Page
    template_name = 'pageDetail.html'


class PageDeleteView(SuccessMessageMixin, DeleteView):
    model = Page
    template_name = 'delete.html'
    success_url = reverse_lazy("website:test")
    success_message = "Page Successfully Deleted"


class BlogCreateView(SuccessMessageMixin, CreateView):
    model = Blog
    template_name = 'blogCreate.html'
    form_class = BlogForm
    success_url = reverse_lazy("website:test")
    success_message = "Blog Successfully Created"


class BlogUpdateView(SuccessMessageMixin, UpdateView):
    model = Blog
    template_name = 'blogUpdate.html'
    form_class = BlogForm
    success_url = reverse_lazy("website:test")
    success_message = "Blog Successfully Updated"


class BlogListView(ListView):
    model = Blog
    template_name = 'blogList.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(deleted_at=None)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogDetail.html'


class BlogDeleteView(SuccessMessageMixin, DeleteView):
    model = Blog
    template_name = 'delete.html'
    success_url = reverse_lazy("website:test")
    success_message = "Blog Successfully Deleted"


class CommentListView(ListView):
    model = Comment
    template_name = 'commentList.html'
    context_object_name = 'comments'

    def get_queryset(self):
        return Comment.objects.filter(deleted_at=None)


class CommentDetailView(DetailView):
    model = Comment
    template_name = 'commentDetail.html'


class CommentDeleteView(SuccessMessageMixin, DeleteView):
    model = Comment
    template_name = 'delete.html'
    success_url = reverse_lazy("website:test")
    success_message = "Comment Successfully Deleted"

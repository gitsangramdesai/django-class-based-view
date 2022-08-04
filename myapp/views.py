from django.shortcuts import redirect, render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password

from myapp.forms import SiteUserForm
from .models import SiteUser


class IndexView(ListView):
    model = SiteUser
    queryset = SiteUser.objects.filter(status='active').all().order_by('-createdAt')
    template_name = 'myapp/list_view.html'
    context_object_name = 'site_user_list'
    
class DetailedView(DetailView):
    model = SiteUser
    template_name = 'myapp/detail_view.html'
    context_object_name = 'site_user'
    
class AddView(CreateView):
    model = SiteUser
    form_class = SiteUserForm
    template_name = 'myapp/add_view.html'
    success_url = '/'
    
class EditView(UpdateView):
    model = SiteUser
    form_class = SiteUserForm
    pk_url_kwarg = 'pk'
    template_name = 'myapp/edit_view.html'
    success_url = '/'
    
class DeleteView(DeleteView):
    model = SiteUser
    pk_url_kwarg = 'pk'
    template_name = 'myapp/delete_view.html'
    success_url = '/'    
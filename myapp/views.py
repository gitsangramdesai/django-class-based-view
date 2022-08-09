from django.shortcuts import redirect, render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView,View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse,reverse_lazy
import json
from myapp.forms import SiteUserForm,DocumentForm
from .models import SiteUser
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse

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
    success_url = '/myapp/'
    
class EditView(UpdateView):
    model = SiteUser
    form_class = SiteUserForm
    pk_url_kwarg = 'pk'
    template_name = 'myapp/edit_view.html'
    success_url = '/myapp'
    
class DeleteView(DeleteView):
    model = SiteUser
    pk_url_kwarg = 'pk'
    template_name = 'myapp/delete_view.html'
    success_url = '/myapp/'

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'myapp/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'myapp/simple_upload.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('model_form_upload')
    else:
        form = DocumentForm()
    return render(request, 'myapp/form_upload.html', {
        'form': form
    })
    
class FileUploadView(View):
    form_class = DocumentForm
    success_url = reverse_lazy('class_file_upload')
    template_name = 'myapp/class_upload.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})    
        
def siteUserByEmail(request,foo):        
    print("emailId",foo)
    queryset = SiteUser.objects.filter(email=foo).values()
    return JsonResponse({"siteuser": list(queryset)})
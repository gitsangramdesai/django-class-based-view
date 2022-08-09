import email
from operator import itemgetter
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
import json
from myapp.forms import SiteUserForm, DocumentForm
from .models import SiteUser
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class IndexView(ListView):
    model = SiteUser
    queryset = SiteUser.objects.filter(
        status='active').all().order_by('-createdAt')
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


def siteUserByEmail(request, foo):
    print("emailId", foo)
    queryset = SiteUser.objects.filter(email=foo).values()
    return JsonResponse({"siteuser": list(queryset)})


class ExtendedView(DetailView):
    def get(self, request, *args, **kwargs):
        foo = self.kwargs['foo']
        queryset = SiteUser.objects.filter(email=foo).values()
        return JsonResponse({"siteuser": list(queryset)})


@method_decorator(csrf_exempt, name='dispatch')
class SiteUserUpdate(View):
    def patch(self, request, item_id):
            print("item_id", item_id);
            data = json.loads(request.body.decode("utf-8"))
            item = SiteUser.objects.get(id=item_id)
            item.firstName = data['firstName']
            print("data['firstName']", data['firstName']);
            item.save()

            data = {
                'message': f'Item {item_id} has been updated'
            }

            return JsonResponse(data)

    def delete(self, request, item_id):
        item = SiteUser.objects.get(id=item_id)
        item.delete()

        data = {
            'message': f'Item {item_id} has been deleted'
        }
        return JsonResponse(data)

    def get(self, request):
        items_count = SiteUser.objects.count()
        items = SiteUser.objects.all()

        items_data = []
        for item in items:
            items_data.append({
                'firstName': item.firstName,
                'lastName': item.lastName,
                'email': item.email,
            })

        data = {
            'items': items_data,
            'count': items_count,
        }

        return JsonResponse(data)

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        firstName = data.get('firstName')
        lastName = data.get('lastName')
        emailId = data.get('email')
        dob = data.get('dob')
        status = data.get('status')
        city = data.get('city')
        state = data.get('state')
        country = data.get('country')
        pin = data.get('pin')
        addressLine1 = data.get('addressLine1')
        addressLine2 = data.get('addressLine2')

        try:
            isValidEmail = validate_email(emailId)
        except ValidationError:
            print("ValidationError")
            data={
                "status":"failure",
                "message":"Enter Valid Email Address"
            }
            return JsonResponse(data, status=422)     
        
        
        queryset = SiteUser.objects.filter(email=emailId).count()
        if queryset > 0:
            data = {
                "status": "failure",
                "message": "email address already exist"
            }
            return JsonResponse(data, status=422)                  


        
        site_user_data = {
            'firstName': firstName,
            'lastName': lastName,
            'email': emailId,
            "addressLine1":addressLine1,
            "addressLine2":addressLine2,
            "status":status,
            "city":city,
            "state":state,
            "country":country,
            "dob":dob,
            "pin":pin
        }

        item = SiteUser.objects.create(**site_user_data)

        data = {
            "message": f"New item added to Site User with id: {item.id}"
        }
        return JsonResponse(data, status=201)
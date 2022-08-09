from django.urls import include, re_path,path
from myapp import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    re_path(r'^detail/(?P<pk>\d+)/$', views.DetailedView.as_view(), name='site_user_detail_view'),
    path('add', views.AddView.as_view(), name="add_site_user"),
    path('edit/<int:pk>', views.EditView.as_view(), name="edit_site_user"),
    path('delete/<int:pk>', views.DeleteView.as_view(), name="delete_post"),
    path('simpleupload', views.simple_upload, name="simple_upload"),
    path('modelformupload', views.model_form_upload, name="model_form_upload"),
    path('classfileupload', views.FileUploadView.as_view(), name="class_file_upload"),
    path('siteuser/<str:foo>', views.siteUserByEmail, name="site_user_list_email"),
    path('siteusercbv/<str:foo>', views.ExtendedView.as_view(), name="site_user_list_email_cbv"),
    path('updatefirstname/<int:item_id>', views.SiteUserUpdate.as_view(), name="patch_first_name"),
    path('listsiteuser', views.SiteUserUpdate.as_view(), name="list_site_user "),
]
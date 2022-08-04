from django.urls import include, re_path,path
from myapp import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    re_path(r'^detail/(?P<pk>\d+)/$', views.DetailedView.as_view(), name='site_user_detail_view'),
    path('add', views.AddView.as_view(), name="add_site_user"),
    path('edit/<int:pk>', views.EditView.as_view(), name="edit_site_user"),
    path('delete/<int:pk>', views.DeleteView.as_view(), name="delete_post"),
]
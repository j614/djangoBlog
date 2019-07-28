from django.urls import path
from .import views

app_name = 'blog'

urlpatterns = [
    # views post
    path('', views.post_list, name_list='post_list'),
    path('<int:year>/<int:moth>/<int:day>/<slug:post>',views.post_detail,name ='post_detail')
]
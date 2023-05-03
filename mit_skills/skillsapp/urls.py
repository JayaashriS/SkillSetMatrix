from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^login/$', views.login_request,  name='login'),
    re_path(r'^home/$', views.home, name='home'),
    re_path(r'^logout/$', views.logout_request, name='logout'),
    #re_path(r'^main/$', views.main, name='main'),
    re_path(r'^add/$', views.add, name='add'),
    re_path(r'^edit/$', views.edit, name='edit'),
    re_path(r'^update/$', views.update, name='update'),
    re_path(r'^delete/$', views.delete, name='delete'),
    ## SKills List
    #re_path(r'^skillsListCat/$',views.show_skill_Category, name='SkillCategory')
    #re_path(r'^load_skill_names/$',views.load_skill_names, name='load_skill_names')
]
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from.import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "GraphAlgoriThmVisU Admin"
admin.site.site_title = "GraphAlgoriThmVisU Admin Panel"
admin.site.index_title = "Welcome GraphAlgoriThmVisU Admin Panel"

urlpatterns = [
    path('', views.home, name="home"),
    path('GAVModule/', views.GAVModule, name="GAVModule"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('help/', views.help, name="help"),
    path('info/', views.info, name="info"),
    path('login1/', views.login1, name="login1"),
    path('registration/', views.registration, name="registration"),
    path('profile/', views.profile, name="profile"),
    path('edit_profile', views.edit_profile, name="edit_profile"),
    path('logout/', views.handleLogout, name="handleLogout"),
    # path('change_password/<token>/', views.change_password, name="change_password"),
    # path('forgot_password', views.forgot_password, name="forgot_password"),
     
]


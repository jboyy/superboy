"""superboy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from home import views
from user import views as user_views
from django.contrib.auth import views as auth_views
from contact import views as contact_views
from django.contrib import admin


urlpatterns = [
    path('', views.home,name ='home'),
    path('about/', views.about,name ='about'),
    path('search', views.search, name="search"),
    path('login/',auth_views.LoginView.as_view(template_name = 'login.html'),name = 'login'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name = 'password_reset.html'),name = 'password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'),name = 'password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html'),name = 'password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'),name = 'password_reset_complete'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'logout.html'),name = 'logout'),
    path('contact/', contact_views.contact,name ='contact'),
    path('profile/', user_views.profile,name ='profile'),
    path('register/', user_views.register,name ='register'),
    path('blog/',views.bloglistview.as_view(),name ='blog'),
    path('blog/<int:pk>/',views.blogdetailview.as_view(),name ='blog-detail'),
    path('blog/new/',views.blogcreateview.as_view(),name ='blog-create'),
    path('blog/<int:pk>/update/',views.blogupdateview.as_view(),name ='blog-update'),
    path('blog/<int:pk>/delete/',views.blogdeleteview.as_view(),name ='blog-delete'),
    path('user/<str:username>/',views.userbloglistview.as_view(),name ='user-posts'),
    path('blog/<int:pk>/add_comment/',views.AddCommentView.as_view(),name ='add-comment')
   
    ]
   
if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)

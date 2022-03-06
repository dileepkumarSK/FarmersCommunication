from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('login', views.login, name='login'),
   
    path('share', views.share, name='share'),
    path('details', views.detalis, name='details'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'), 
    path('homepagep', views.homepagep, name='homepagep'), 
    path('buyer', views.buyer, name='buyer'),
    path('seller', views.seller, name='seller'),
    path('machineary', views.machineary, name='machineary'),
    path('security', views.security, name='security'),
    path('help', views.help, name='help'),
    path('feed', views.feed, name='feed'),
    path('register', views.register, name='register'),
    path('central', views.central, name='central'),
    path('account', views.account, name='account'),
    path('logout', views.logout, name='logout'),
    path('terms', views.terms, name='terms'), 
    path('cropdet', views.cropdet, name='cropdet'),
    path('editprofile', views.editperinfo, name='editacc'),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),
]+ static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
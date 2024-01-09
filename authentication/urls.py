from django.urls import include, path, reverse_lazy
from authentication import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.home, name = 'home'),
    path('signup', views.signup, name = 'signup'),
    path('logout', include('django.contrib.auth.urls')),
    path('', include('django.contrib.auth.urls')),

     # change password urls
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    #profile
    path('profile', views.profile, name = 'profile'),
    path('profile-Edit', views.profileEdit, name = 'profileEdit'),
]










# urlpatterns = [
#     path('', views.home, name='home'),
#     path('signup/', views.signup, name='signup'),
#     path('logout/', include('django.contrib.auth.urls')),
#     path('', include('django.contrib.auth.urls'), name='login'),

#     path('password_change/', include('django.contrib.auth.urls'), name='change_password'),
#     path('password_change/done', RedirectView.as_view(url='/login/'), name='password_change_done'),
# ]
 
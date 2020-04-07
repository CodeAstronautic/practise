from django.urls import path
from . import views
from django.contrib.auth import views as v

urlpatterns = [
    path('index_page/',views.index_page,name='index_page'),
    path('register/',views.register_user,name='register_user'),
    path('login/',views.login_user,name='login_user'),
    path('logout_user/',views.logout_user,name='logout_user'),

    path('recipes/',views.recipes,name='recipes'),
    path('service/',views.service,name='service'),
    path('about/',views.about,name='about'),
    path('news/',views.news,name='news'),
    path('',views.single,name='single'),
    path('contact/',views.contact,name='contact'),

    path('password-change/',v.PasswordChangeView.as_view(template_name='food/password_change.html'),name='change_password'),
    path('password-change-done/',v.PasswordChangeView.as_view(template_name='food/password_change_done.html'),name='password_change_done'),
    path('password-reset/',v.PasswordResetView.as_view(template_name='food/password_reset.html',email_template_name='food/password_reset_email.html',subject_template_name='food/password_reset_email_subject.txt'),name='password_reset'),
    path('password-reset-done/',v.PasswordResetView.as_view(template_name='food/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',v.PasswordResetConfirmView.as_view(template_name='food/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',v.PasswordResetCompleteView.as_view(template_name='food/password_reset_complete.html'),name='password_reset_complete'),
    
    path('edit_profile/',views.edit_profile,name='edit_profile')
]
    




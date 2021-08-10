from django.urls import path
from django.urls import reverse_lazy
from authentication.views import ( 
    SignUpView, 
    SignInView, 
    SignOutView, 
    PRView, 
    PRDone,
    PRConfirm, 
    PRComplete,
    PWDChangeView,
    PWDChangeDoneView
    )

from django.contrib.auth.views import ( 
    PasswordResetView,
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView,
      )


# SignUpView is class view
# path need second argm as function view
# we convert it using as_view() method

urlpatterns = [
    # path("",home,name="home_view"),
    path('',SignInView.as_view(),name='signin_view'),
    path('signup/',SignUpView.as_view(),name='signup_view'),
    path('signout/',SignOutView.as_view(),name='signout_view'),
    # path('password/reset/',PRView.as_view(),name='password_reset'),
    # path('password/reset/done',PRDone.as_view(),name='password_reset_done'),
    # path('password/reset/confirm/<uidb64>/<token>',PRConfirm.as_view(),name='password_reset_confirm'),
    # path('password/reset/complete',PRComplete.as_view(),name='password_reset_complete'),

    path('password/reset/',PasswordResetView.as_view(email_template_name='authentication/password_reset_email.html',
                                                template_name = "authentication/password_reset.html")
                            ,name='password_reset'),
    path('password/reset/done',PasswordResetDoneView.as_view(template_name = 'authentication/password_reset_done.html'),
                            name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>',PasswordResetConfirmView.as_view( template_name = 'authentication/password_reset_confirm.html'),
                            name='password_reset_confirm'),
    path('password/reset/complete',PasswordResetCompleteView.as_view(template_name = 'authentication/password_reset_complete.html'),
                            name='password_reset_complete'),
    # path('password/change/',PWDChangeView.as_view(),name='password_change_view'),
    # path('password/change/done',PWDChangeDoneView.as_view(),name='password_change_done_view'),
    path('password/change/',PasswordChangeView.as_view(template_name = 'authentication/password_change.html',
                            success_url =reverse_lazy('password_change_done_view')),
                            name='password_change_view'),
    path('password/change/done',PasswordChangeDoneView.as_view(template_name = 'authentication/password_change_done.html'),
                            name='password_change_done_view'),



]


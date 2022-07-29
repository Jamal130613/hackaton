from django.urls import path


from applications.account.views import RegisterView, ActivationView, LoginView, ChangePasswordView, LogOutView, \
    ForgotPasswordView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('active/<uuid:activation_code>/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    path('logout/', LogOutView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view())
]
from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('register', Register.as_view(), name='register'),
    path('passwordRecovery', PasswordRecovery.as_view(), name='password_recovery'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('report/<int:event_id>/', GenerateReportView.as_view(), name='generate_report'),
    path('reportExcel/<int:event_id>/', GenerateReportExcelView.as_view(), name='generate_report'),
]

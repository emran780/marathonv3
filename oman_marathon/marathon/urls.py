from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('past_events/', views.past_events, name='past_events'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('runner_dashboard/', views.runner_dashboard, name='runner_dashboard'),
    path('update_runner/', views.update_runner, name='update_runner'),
    path('delete_runner/<int:runner_id>/', views.delete_runner, name='delete_runner'),
]

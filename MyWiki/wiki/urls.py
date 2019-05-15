from django.urls import path, include
from . import views

app_name = 'wiki'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('upload/', views.upload_file, name='upload_page' ),
    path('accounts/signup', views.signup_page , name='signup_page'),
    path('<str:pk>/edit/save', views.save_page , name='save_page'),
    path('<str:pk>/edit/delete/confirm', views.delete_confirm , name='delete_confirm'),
    path('<str:pk>/edit/delete', views.delete_page , name='delete_page'),
    path('<str:pk>/edit', views.edit_page , name='edit_page'),
    path('<str:pk>/', views.View_Page, name='detail'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
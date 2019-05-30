from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# URL configuratrion for the sites pages.
# This has been done dynamically instead of use of absolute url
app_name = 'wiki'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # Navigation for the index page.
    path('errors/407', views.test_407_error , name='test_407_error'), # Used to ensure the 407 warning doesnt appear in the log.
    path('errors/500', views.test_500_error , name='test_500_error'), # Used to ensure the 407 error appears in the log.
    path('errors/404', views.test_404_error , name='test_404_error'), # Used to ensure the 404 warning appears in the log.
    path('download/upload/<str:path>/', views.download, name='download'),
    path('upload/', views.upload_file, name='upload_page' ), # Navigation for the file upload page.
    path('accounts/signup', views.signup_page , name='signup_page'), # Navigation for the user signup page.
    path('<str:pk>/edit/save', views.save_page , name='save_page'), # calls the save page function in views.
    path('<str:pk>/edit/delete/confirm', views.delete_confirm , name='delete_confirm'), # calls the delete page function in views.
    path('<str:pk>/edit/delete', views.delete_page , name='delete_page'), # Navigation for the confirmation page.
    path('<str:pk>/edit', views.edit_page , name='edit_page'), # Navigation for the page modification.
    path('<str:pk>/', views.View_Page, name='detail'), # Navigation for each page view created.
]
# URL configuratrion for the sites accounts login sections.
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
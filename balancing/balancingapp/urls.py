from django.urls import path
from . import views
from .folder_of_views.admin_views import *
from .services.file_creator import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.cards_update_view, name='update'),
    path("pivot/", views.PivotCardView.as_view(), name='user_pivot'),
    path("admin/", AdminPivotView.as_view(), name='admin_pivot'),
    path("onchecking/", OnCheckinView.as_view(), name='onchecking'),
    path("download/", download_excel_data, name='download_pivot'),
    path("close/", close_edit, name='close'),
    path("open/", open_edit, name='open'),
    path('<int:pk>/accept/', accept_kpi, name='accept'),
    path('<int:pk>/reject/', reject_kpi, name='reject')




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
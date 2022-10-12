from django.urls import path
from . import views
from .services.file_creator import *

urlpatterns = [
    path("", views.cards_update_view, name='update'),
    path("pivot/", views.PivotCardView.as_view(), name='user_pivot'),
    path("admin/", views.admin_cards_update_view, name='admin_pivot'),
    path("download/", download_excel_data, name='download_pivot'),
    path("close/", views.close_edit, name='close'),
    path("open/", views.open_edit, name='open'),



]
import django_tables2 as tables
from .models import *


class OnCheckingTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor="pk", orderable=False)
    accept = tables.TemplateColumn(verbose_name=('Решение'),
                                      template_name='accept_column.html',
                                      orderable=False)

    class Meta:
        model = Card
        template_name = "django_tables2/bootstrap.html"
        fields = ('selection','accept', "organization", 'function', 'type',
                 'role', 'fio',
                  'name', 'method', 'low_level', 'target_level',
                  'high_level', 'weight', 'path_to_doc',
                  'comment', 'comment_CA', 'comment_AES_DO')


class CardTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor="pk", orderable=False)

    class Meta:
        model = Card
        template_name = "django_tables2/bootstrap.html"
        fields = ('selection', "organization", 'function', 'type',
                 'role', 'fio',
                  'name', 'method', 'low_level', 'target_level',
                  'high_level', 'weight', 'path_to_doc',
                  'comment', 'comment_CA', 'comment_AES_DO')
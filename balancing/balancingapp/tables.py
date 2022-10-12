import django_tables2 as tables
from .models import *


class CardTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor="pk", orderable=False)

    class Meta:
        model = Card
        template_name = "django_tables2/bootstrap.html"
        fields = ('selection', 'id', "organization", 'function', 'type',
                 'role', 'fio',
                  'name', 'method', 'low_level', 'target_level',
                  'high_level', 'weight', 'path_to_doc',
                  'comment', 'comment_CA', 'comment_AES_DO')
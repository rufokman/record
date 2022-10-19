from django.shortcuts import get_object_or_404, redirect
from django_filters import rest_framework as filters
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from balancingapp.filters import CardFilter
from balancingapp.models import *
from balancingapp.tables import *


class AdminPivotView(SingleTableMixin, FilterView):
    queryset = Card.objects.filter(status=0)
    table_class = CardTable
    # serializer_class = ServerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CardFilter
    template_name = "user_pivot_tab.html"


class OnCheckinView(SingleTableMixin, FilterView):
    queryset = Card.objects.filter(status=1)
    table_class = OnCheckingTable
    # serializer_class = ServerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CardFilter
    template_name = "user_pivot_tab.html"


def accept_kpi(request, pk):
    card_data = get_object_or_404(Card, pk=pk)
    card_data.status = 0
    card_data.save(update_fields=['status'])
    return redirect('onchecking')


def close_edit(request):
    config_data = get_object_or_404(Config, id=1)
    config_data.allow_edit = False
    config_data.save(update_fields=['allow_edit'])

    return redirect('admin_pivot')


def open_edit(request):
    config_data = get_object_or_404(Config, id=1)
    config_data.allow_edit = True
    config_data.save(update_fields=['allow_edit'])

    return redirect('admin_pivot')



def reject_kpi(request, pk):
    card_data = get_object_or_404(Card, pk=pk)
    card_data.status = 2
    card_data.save(update_fields=['status'])

    return redirect('onchecking')


#
# @login_required()
# def admin_cards_update_view(request):
#     data = Card.objects.all()
#     print(request.user)
#     context = {}
#     formset = CardFormSet(request.POST or None, queryset=data)
#     if formset.is_valid():
#         for form in formset:
#             if form.cleaned_data == {}:
#                 continue
#             # print(form.cleaned_data)
#             qform = form.save(commit=False)
#             if qform.method == 1:
#                 qform.low_level = format(float(qform.low_level.replace(',', '.')), '.3f')
#                 qform.target_level = format(float(qform.target_level.replace(',', '.')), '.3f')
#                 qform.high_level = format(float(qform.high_level.replace(',', '.')), '.3f')
#
#             qform.save()
#
#         return redirect(reverse_lazy("admin_pivot"))
#
#     # Add the formset to context dictionary
#     context['formset'] = formset
#     context['filter'] = CardFilter
#     return render(request, "admin_pivot_tab.html", context)

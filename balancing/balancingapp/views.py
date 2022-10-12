from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django_filters import rest_framework as filters
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from rest_framework import generics
from .filters import CardFilter
from .models import *
from .forms import *
from .tables import CardTable
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required()
def cards_update_view(request):
    data = Card.objects.filter(user=request.user)
    config_data = Config.objects.first()
    print(config_data)
    allow_edit = config_data.allow_edit
    context = {}
    formset = CardFormSet(request.POST or None, queryset=data)

    if formset.is_valid():
        if allow_edit == False:
            return redirect('update')

        for form in formset:
            if form.cleaned_data == {}:
                continue
            # print(form.cleaned_data)
            qform = form.save(commit=False)
            qform.user = request.user
            qform.function = request.user.function
            if qform.method == 1:
                qform.low_level = format(float(qform.low_level.replace(',', '.')), '.3f')
                qform.target_level = format(float(qform.target_level.replace(',', '.')), '.3f')
                qform.high_level = format(float(qform.high_level.replace(',', '.')), '.3f')

            qform.save()

        return redirect(reverse_lazy("update"))

    # Add the formset to context dictionary
    context['formset'] = formset
    return render(request, "home.html", context)


class PivotCardView(SingleTableMixin, FilterView):
    queryset = Card.objects.all()
    table_class = CardTable
    # serializer_class = ServerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CardFilter
    template_name = "user_pivot_tab.html"


@login_required()
def admin_cards_update_view(request):
    data = Card.objects.all()
    print(request.user)
    context = {}
    formset = CardFormSet(request.POST or None, queryset=data)
    if formset.is_valid():
        for form in formset:
            if form.cleaned_data == {}:
                continue
            # print(form.cleaned_data)
            qform = form.save(commit=False)
            if qform.method == 1:
                qform.low_level = format(float(qform.low_level.replace(',', '.')), '.3f')
                qform.target_level = format(float(qform.target_level.replace(',', '.')), '.3f')
                qform.high_level = format(float(qform.high_level.replace(',', '.')), '.3f')

            qform.save()

        return redirect(reverse_lazy("admin_pivot"))

    # Add the formset to context dictionary
    context['formset'] = formset
    context['filter'] = CardFilter
    return render(request, "admin_pivot_tab.html", context)


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

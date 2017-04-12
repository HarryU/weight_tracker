from django.shortcuts import render
from graphos.sources.model import ModelDataSource
from graphos.renderers.morris import LineChart
from graphos.renderers.yui import ComboChart
from .models import Weight
from .forms import WeightEntryForm, UserForm
from django.shortcuts import redirect


def weight_graph(request):
    dropdown = UserForm()
    queryset = Weight.objects.filter()
    data_source = ModelDataSource(queryset, fields=['date', 'weight'])
    chart = LineChart(data_source)


    if request.method == "POST":
        form = WeightEntryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/')
    else:
        form = WeightEntryForm()

    context = {'chart': chart, 'form': form, 'dropdown': dropdown}
    return render(request, 'weight_entry/weight_graph.html', context)

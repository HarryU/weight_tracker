from django.shortcuts import render
from .models import Weight

def weight_graph(request):
    return render(request, 'weight_entry/weight_graph.html', {})


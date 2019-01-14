from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def database_panel(request):
    params = {'section': 'Database Panel'}
    return render(request, 'newsbetter/database_panel.html', params)

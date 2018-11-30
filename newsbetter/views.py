from django.shortcuts import render


def database_panel(request):
    params = {'section': 'Database Panel'}
    return render(request, 'newsbetter/database_panel.html', params)

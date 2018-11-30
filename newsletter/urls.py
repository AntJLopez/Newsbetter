from django.urls import path, register_converter, include  # noqa
from . import views, converters


register_converter(converters.DateConverter, 'date')

urlpatterns = [
    path('', views.newsletter_list, name='newsletter_list'),
    path('mockup/<date:date>/', views.newsletter_mockup,
         name='newsletter_mockup'),
    path('<date:date>/', views.newsletter_view,
         name='newsletter_view'),
    path('send/<date:date>/', views.newsletter_send, name='newsletter_send'),
]

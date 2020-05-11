from django.urls import path
from . import views
from .views import PollView

urlpatterns = [

    path('', views.index, name='polls_list'),
    path('add/', views.PollView.as_view(), name='poll_add'),
    path('<int:id/edit/', views.PollView.as_view(), name='poll_edit'),
    path('<int:id>/delete/', views.PollView.as_view(), name='poll_delete'),
    path('<int:id>/details/', views.details, name='poll_details'),
    path('<int:id>/', views.poll, name='single_poll'),

]
'''urlpatterns = [
    path('add/', PollView.as_view(), name='poll_add'),
    path('<int:id>/edit/', PollView.as_view(), name='poll_edit'),
    path('<int:id>/delete/', PollView.as_view(), name='poll_delete'),
    path('list/', index, name='polls_list'),
    path('<int:id>/details/', details, name="poll_details"),
    path('<int:id>/', vote_poll, name="poll_vote")
]'''

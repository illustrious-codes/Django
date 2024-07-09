from django.urls import path
from . import api

urlpatterns =[
    path("", api.index, name="index"),
    path("<int:question_id>/", api.detail, name="detail"),
    path("<int:question_id>/results/", api.results, name="results"),
    path("<int:question_id>/vote/", api.vote, name="vote")
]
from django.urls import path
from .views import CurrentDateView, RandomNumView, HelloView, IndexView

urlpatterns = [
    path('datetime/', CurrentDateView.as_view()),
    path('randomnum/', RandomNumView.as_view()),
    path('hello/', HelloView.as_view()),
    path('', IndexView.as_view()),
]


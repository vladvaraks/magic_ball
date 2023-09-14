from django.urls import path, include
from magic_app.views import *

app_name = 'magic_app'

urlpatterns = [
    path('', LoginUserView.as_view(), name='login'),
    path('question/', QuestionView.as_view(), name='question'),
]
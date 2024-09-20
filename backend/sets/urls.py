from django.urls import path
from .views import SetList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", SetList.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path
from .views import WordDetails, WordList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", WordList.as_view()),
    path("<int:id>", WordDetails.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)

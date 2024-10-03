from django.urls import path
from .views import SetList, SetDetails, SetWords
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", SetList.as_view(), name="set-list"),
    path("<str:id>", SetDetails.as_view(), name="set-detail"),
    path("<str:id>/words", SetWords.as_view(), name="set-words"),
]


urlpatterns = format_suffix_patterns(urlpatterns)

from .views import ActivityListView, ActivityListByUser
from django.urls import path

urlpatterns = [
    path('listActivities', ActivityListView.as_view()),
    path('listActivitiesByUser/<int:id_user>/', ActivityListByUser.as_view()),
]
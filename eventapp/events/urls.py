from .views import ActivityListView, ActivityListByUser, ActiveActivityListByUser, AssignUserActivity, RemoveUserActivity, ActiveProgramEvent, ActiveSponsorsEvent
from django.urls import path

urlpatterns = [
    path('listActivities', ActivityListView.as_view()),
    path('listActivitiesByUser', ActivityListByUser.as_view()),
    path('listActiveActivitiesByUser', ActiveActivityListByUser.as_view()),
    path('assignUserActivity/<int:id_activity>/', AssignUserActivity.as_view()),
    path('removeUserActivity/<int:id_activity>/', RemoveUserActivity.as_view()),
    path('activeProgramEvent', ActiveProgramEvent.as_view()),
    path('activeSponsorsEvent', ActiveSponsorsEvent.as_view()),
]
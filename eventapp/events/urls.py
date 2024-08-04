from .views import ActivityListView, ActivityListByUser, ActiveActivityListByUser, AssignUserActivity, RemoveUserActivity
from django.urls import path

urlpatterns = [
    path('listActivities', ActivityListView.as_view()),
    path('listActivitiesByUser/<int:id_user>/', ActivityListByUser.as_view()),
    path('listActiveActivitiesByUser/<int:id_user>/', ActiveActivityListByUser.as_view()),
    path('AssignUserActivity/<int:id_user>/<int:id_activity>/', AssignUserActivity.as_view()),
    path('RemoveUserActivity/<int:id_user>/<int:id_activity>/', RemoveUserActivity.as_view()),
]
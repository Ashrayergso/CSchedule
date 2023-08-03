```python
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('crewmembers/', views.CrewMemberListView.as_view(), name='crewmembers'),
    path('crewmembers/<int:pk>/', views.CrewMemberDetailView.as_view(), name='crewmember-detail'),
    path('ships/', views.ShipListView.as_view(), name='ships'),
    path('ships/<int:pk>/', views.ShipDetailView.as_view(), name='ship-detail'),
    path('assignments/', views.AssignmentListView.as_view(), name='assignments'),
    path('assignments/<int:pk>/', views.AssignmentDetailView.as_view(), name='assignment-detail'),
    path('assignments/create/', views.AssignmentCreateView.as_view(), name='assignment-create'),
    path('assignments/<int:pk>/update/', views.AssignmentUpdateView.as_view(), name='assignment-update'),
    path('assignments/<int:pk>/delete/', views.AssignmentDeleteView.as_view(), name='assignment-delete'),
    path('assigncrew/', views.assignCrewToShips, name='assign-crew'),
]
```
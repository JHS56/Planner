from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("view/<int:plan_id>/", views.detail, name="detail"), 
    path("create/", views.create, name="create"),
    path("view/<int:plan_id>/edit/", views.edit, name="edit"),
    path('view/<int:plan_id>/delete/', views.delete, name='delete'),
    path('goal/', views.goal, name='goal'),
    path('goal/edit/<int:object_id>/', views.edit_goal, name='edit_goal'),
]
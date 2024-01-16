from django.urls import path

from .views import (
    APIRootView,
    BoardListView, BoardDetailView, BoardCreateView, BoardUpdateView, BoardDestroyView,
    ToDoListView, ToDoDetailView, ToDoCreateView, ToDoUpdateTitleView, ToDoUpdateStatusView, 
    ToDoDestroyView
)

urlpatterns = [
    path(
        '', 
        APIRootView.as_view(),
        name='api-root'
    ),
    path(
        'boards/',
        BoardListView.as_view(),
        name='board-list'
    ),
    path(
        'board-add/',
        BoardCreateView.as_view(),
        name='board-create'
    ),
    path(
        'boards/<int:pk>/',
        BoardDetailView.as_view(),
        name='board-detail'
    ),
    path(
        'boards/<int:pk>/change/',
        BoardUpdateView.as_view(),
        name='board-update'
    ),
    path(
        'boards/<int:pk>/delete/',
        BoardDestroyView.as_view(),
        name='board-destroy'
    ),
    path(
        'boards/<int:pk>/todos/',
        ToDoListView.as_view(),
        name='todo-list'
    ),
    path(
        'boards/<int:pk>/todo-add/',
        ToDoCreateView.as_view(),
        name='todo-create'
    ),
    path(
        'boards/<int:pk>/todos/<int:todo_pk>/',
        ToDoDetailView.as_view(),
        name='todo-detail'
    ),
    path(
        'boards/<int:pk>/todos/<int:todo_pk>/change/title/',
        ToDoUpdateTitleView.as_view(),
        name='todo-update-title'
    ),
    path(
        'boards/<int:pk>/todos/<int:todo_pk>/change/status/',
        ToDoUpdateStatusView.as_view(),
        name='todo-update-status'
    ),
    path(
        'boards/<int:pk>/todos/<int:todo_pk>/delete/',
        ToDoDestroyView.as_view(),
        name='todo-destroy'
    ),
]

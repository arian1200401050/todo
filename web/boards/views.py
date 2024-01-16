from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse

from .models import Board, ToDo
from .serializers import (
    BoardSerializer, ToDoSerializer,
    BoardListSerializer, ToDoListSerializer,
    BoardDetailSerializer, ToDoDetailSerializer
)


class APIRootView(APIView):
    def get(self, request):
        return Response({
            'list_boards': reverse('board-list', request=request),
            'add_board': reverse('board-create', request=request),
        })


class BoardListView(APIView):
    def get(self, request):
        """
        Retrun a list of all existing `Boards`.
        """
        boards = Board.objects.order_by('id')
        serializer = BoardListSerializer(boards, many=True, context={'request': request})
        return Response(serializer.data)


class BoardCreateView(APIView):
    def post(self, request):
        """
        Create a new `Board`.
        """
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def get_board(pk):
    try:
       return Board.objects.get(id=pk)
    except Board.DoesNotExist:
        return False
    

class BoardDetailView(APIView):
    def get(self, request, pk):
        board = get_board(pk)
        if not board:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BoardDetailSerializer(board, context={'request': request})
        return Response(serializer.data)
        

class BoardUpdateView(APIView):
    def put(self, request, pk):
        """
        Update an existing `Board`.
        """
        board = get_board(pk)
        if not board:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BoardSerializer(board, request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoardDestroyView(APIView):
    def delete(self, request, pk):
        """
        Destroy an existing `Board`.
        """
        board = get_board(pk)
        if not board:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ToDoListView(APIView):
    def get(self, request, pk):
        """
        List all `ToDos`.
        """
        board = get_board(pk)
        if not board:
            return Response(status=status.HTTP_404_NOT_FOUND)
         
        if 'done' in request.query_params:
            todos = board.todos.filter(status=True).order_by('id')
        else:
            todos = board.todos.filter(status=False).order_by('id')
        serializer = ToDoListSerializer(todos, many=True, context={'request': request})
        return Response(serializer.data)


class ToDoCreateView(APIView):
    def post(self, request, pk):
        """
        Create a `ToDo`.
        """
        board = get_board(pk)
        if not board:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(board=board)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def get_todo(pk, todo_pk):
    try:
        return ToDo.objects.get(board=pk, id=todo_pk)
    except ToDo.DoesNotExist:
        return False
    

class ToDoDetailView(APIView):
    def get(self, request, pk, todo_pk):
        todo = get_todo(pk, todo_pk)
        if not todo:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ToDoDetailSerializer(todo, context={'request': request})
        return Response(serializer.data)


class ToDoUpdateTitleView(APIView):
    def put(self, request, pk, todo_pk):
        """
        Update a `ToDo` title.
        """
        todo = get_todo(pk, todo_pk)
        if not todo:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if not 'title' in request.data or request.data['title'] == todo.title:
            return Response(
                {'Error': 'You should enter new `title`!'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = ToDoSerializer(
            todo, 
            data={'title': request.data['title']}, 
            partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToDoUpdateStatusView(APIView):
    def put(self, request, pk, todo_pk):
        """
        Update a `ToDo` status.
        """
        todo = get_todo(pk, todo_pk)
        if not todo:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        todo_status = not todo.status
        
        serializer = ToDoSerializer(todo, data={'status': todo_status}, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToDoDestroyView(APIView):
    def delete(self, request, pk, todo_pk):
        """
        Destroy a `ToDo`.
        """
        todo = get_todo(pk, todo_pk)
        if not todo:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

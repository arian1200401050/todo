from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Board, ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
        extra_kwargs = {
            'board': {'read_only': True}
        }

class ToDoHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        request = self.context.get('request')
        url_kwargs = {
            'pk': obj.board.id,
            'todo_pk': obj.id
        }
        return reverse(view_name, kwargs=url_kwargs,request=request, format=format)


class ToDoListSerializer(serializers.ModelSerializer):
    show = ToDoHyperlinkedIdentityField('todo-detail')

    class Meta:
        model = ToDo
        fields = ['title', 'show']


class ToDoDetailSerializer(serializers.ModelSerializer):
    # Add url's to browsable api.
    change_status = ToDoHyperlinkedIdentityField('todo-update-status')
    change_title = ToDoHyperlinkedIdentityField('todo-update-title')
    delete = ToDoHyperlinkedIdentityField('todo-destroy')

    class Meta:
        model = ToDo
        fields = [
            'title', 'status', 'created_time', 'updated_time', 
            'change_status', 'change_title', 'delete'
        ]


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class BoardListSerializer(serializers.ModelSerializer):
    show = serializers.HyperlinkedIdentityField('board-detail')

    class Meta:
        model = Board
        fields = ['name', 'show']


class BoardDetailSerializer(serializers.ModelSerializer):
    # Add url's to browsable api.
    todos_count = serializers.SerializerMethodField()
    change = serializers.HyperlinkedIdentityField('board-update')
    delete = serializers.HyperlinkedIdentityField('board-destroy')
    list_todos = serializers.HyperlinkedIdentityField('todo-list')
    list_done_todos = serializers.SerializerMethodField()
    add_todo = serializers.HyperlinkedIdentityField('todo-create')

    class Meta:
        model = Board
        fields = [
            'name', 'todos_count', 'change', 'delete', 
            'list_todos', 'list_done_todos', 'add_todo'
        ]

    def get_todos_count(self, obj):
        count = ToDo.objects.filter(board=obj.id).count()
        return count
    
    def get_list_done_todos(self, obj):
        request = self.context.get('request')
        url = reverse('todo-list', kwargs={'pk': obj.id}, request=request)
        url = f"{url}?done"
        return url
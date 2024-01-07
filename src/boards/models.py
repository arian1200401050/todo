from django.db import models

class Board(models.Model):
    # A database table for `Boards`.
    name = models.CharField(max_length=50, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'boards'
        verbose_name = 'Board'
        verbose_name_plural = 'Boards'


class ToDo(models.Model):
    # A database table for `ToDos`.
    board = models.ForeignKey(to=Board, related_name='todos', on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    status = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'todos'
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDos'
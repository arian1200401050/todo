from rest_framework import status
from rest_framework.test import APITestCase


class BoardTestCase(APITestCase):
    api_urls = {}

    def setUp(self):
        # Get root urls.
        request = self.client.get('')
        self.api_urls['root'] = request.json()

    def add_board(self):
        # Create a board.
        add_board_url = self.api_urls['root']['add_board']
        request = self.client.post(add_board_url, {'name': 'first board'})
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def list_boards(self):
        list_boards_url = self.api_urls['root']['list_boards']
        request = self.client.get(list_boards_url)
        data = request.json()

        self.assertEqual(data[0]['name'], 'first board')

        # Get show url of created board.
        show_url = data[0]['show']
        self.api_urls['boards'] = []
        self.api_urls['boards'].append({'show': show_url})

    def board_detail_test(self):
        board_detail_url = self.api_urls['boards'][0]['show']
        request = self.client.get(board_detail_url)
        return request.json()

    def board_detail(self):
        data = self.board_detail_test()
        self.assertEqual(data['name'], 'first board')

        # Get urls of created board.
        self.api_urls['boards'][0]['change'] = data['change']
        self.api_urls['boards'][0]['delete'] = data['delete']
        self.api_urls['boards'][0]['add_todo'] = data['add_todo']
        self.api_urls['boards'][0]['list_todos'] = data['list_todos']
        self.api_urls['boards'][0]['list_done_todos'] = data['list_done_todos']

    def board_change(self):
        board_change_url = self.api_urls['boards'][0]['change']
        self.client.put(
            board_change_url,
            {'name': 'first board changed'},
            format='json'
        )

        # Check that the name of board has changed.
        data = self.board_detail_test()
        self.assertEqual(data['name'], 'first board changed')

    def board_delete(self):
        board_delete_url = self.api_urls['boards'][0]['delete']
        request = self.client.delete(board_delete_url)
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

        # Check that the board has deleted.
        board_detail_url = self.api_urls['boards'][0]['show']
        request = self.client.get(board_detail_url)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

    def add_todo(self):
        # Create a todo.
        add_todo_url = self.api_urls['boards'][0]['add_todo']
        request = self.client.post(add_todo_url, {'title': 'first todo'})
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def list_todos(self):
        list_todos_url = self.api_urls['boards'][0]['list_todos']
        request = self.client.get(list_todos_url)
        data = request.json()

        self.assertEqual(data[0]['title'], 'first todo')

        # Get show url of created todo.
        show_url = data[0]['show']
        self.api_urls['todos'] = []
        self.api_urls['todos'].append({'show': show_url})

    def todo_detail_test(self):
        todo_detail_url = self.api_urls['todos'][0]['show']
        request = self.client.get(todo_detail_url)
        return request.json()

    def todo_detail(self):
        data = self.todo_detail_test()
        self.assertEqual(data['title'], 'first todo')

        # Get urls of created board.
        self.api_urls['todos'][0]['change_status'] = data['change_status']
        self.api_urls['todos'][0]['change_title'] = data['change_title']
        self.api_urls['todos'][0]['delete'] = data['delete']

    def todo_change_status(self):
        todo_change_status_url = self.api_urls['todos'][0]['change_status']
        self.client.put(
            todo_change_status_url,
            format='json'
        )

        # Check that status of the todo has changed.
        data = self.todo_detail_test()
        self.assertEqual(data['status'], True)

    def todo_change_title(self):
        todo_change_title_url = self.api_urls['todos'][0]['change_title']
        self.client.put(
            todo_change_title_url,
            {'title': 'first todo changed'},
            format='json'
        )

        # Check that title of the todo has changed.
        data = self.todo_detail_test()
        self.assertEqual(data['title'], 'first todo changed')

    def todo_delete(self):
        todo_delete_url = self.api_urls['todos'][0]['delete']
        request = self.client.delete(todo_delete_url)
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

        # Check that the todo has deleted.
        todo_detail_url = self.api_urls['todos'][0]['show']
        request = self.client.get(todo_detail_url)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

    def test_all(self):
        self.add_board()
        self.list_boards()
        self.board_detail()
        self.board_change()
        self.add_todo()
        self.list_todos()
        self.todo_detail()
        self.todo_change_status()
        self.todo_change_title()
        self.todo_delete()
        self.board_delete()

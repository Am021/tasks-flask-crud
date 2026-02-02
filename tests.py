import pytest
import requests

#CRUD biblioteca pytest + requests

BASE_URL = 'http://127.0.0.1:5000'
task = []

def test_create_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa"
    }

    response = requests.post(f"{BASE_URL}/tasks", json= new_task_data)
    assert response.status_code == 200
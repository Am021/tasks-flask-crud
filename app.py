from flask import Flask, request, jsonify
from models import task
from models.task import Task
app = Flask(__name__)
# {} = dicionário
# () = tupla
#CRUD
# CREATE, READ, UPDATE AND DELETE
#Tabela: Tarefa

tasks = [] #lista []
task_id_control = 1

@app.route('/tasks', methods=['POST']) #CREATE
def create_task():
    global task_id_control
    data = request.get_json()
    print(data)
    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify ({"message": "nova tarefa criada com sucesso"})  


@app.route('/tasks', methods=['GET']) #READ
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
        
    output = { 
                "tasks": task_list,
                "total_tasks": len(task_list)  # Len para começar a contagens a partir do 1      
            }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])# <> Identificador
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404


@app.route('/tasks/<int:id>', methods=['PUT']) #UPDATE
def update_task(id):
    
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if task == None:
        return jsonify({"message": "não foi possível encontrar a atividade"}), 404 #404 erro de não encontrado
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']

    return jsonify({"message": "tarefa atualizada com sucesso"}) #200 encontrado com sucesso

@app.route('/tasks/<int:id>', methods=['DELETE']) #DELETE
def delete_task(id):
    task = None
    for t in tasks:
        print(t.to_dict())
        if t.id == id:
            task = t
            break
    
    if not task: 
        return jsonify({"message": "não foi possível encontrar a atividade"}), 404
    
    tasks.remove(task)
    return jsonify({"message": "tarefa deletada com sucesso"})


if __name__ == "__main__":
    app.run(debug=True)
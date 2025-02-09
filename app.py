from flask import Flask, request, jsonify, render_template
from pprint import pprint
from clinic_assistant import workflow  # Импортируем workflow из созданного clinic-assistant.py

app = Flask(__name__)

# Компилируем граф, как было описано выше
app_graph = workflow.compile()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    # Получаем вопрос от пользователя
    question = request.form['question']
    
    # Создаем состояние для графа с вопросом
    state = {"question": question}
    output = None
    
    # Выполняем запрос к графу
    for result in app_graph.stream(state):
        output = result.get('generation', {}).get('generation', "No response generated.")
    
    return jsonify({'response': output})

if __name__ == '__main__':
    app.run(debug=True)

#для запуска нажать пуск справа, потом в создавшуюся консоль написать 
#pipx run streamlit run /Users/anazaharova/Desktop/диплом/ТИГР_ФИНАЛ/ТЕСТ.py
import streamlit as st
import pandas as pd
from datetime import datetime
import os
import task_data
os.chdir(os.path.dirname(__file__))  # рабочая директория
person_easy = [
    {
        "prime_text": "Мы косим траву",
        "stimulus_text": "Мы кле_ плитку",
        "answers": ("им", "ишь"),
        "hint": "Что делаем?"
    },
    {
        "prime_text": "Ты ловишь бабочек",
        "stimulus_text": "Ты вар_ кашу",
        "answers": ("ит", "ишь"),
        "hint": "Что делаешь?"
    },
    {
        "prime_text": "Вы строите дом",
        "stimulus_text": "Вы смотр_ сериал",
        "answers": ("ит", "ите"),
        "hint": "Что делаете?"
    }
]

# Инициализация состояния страницы
if "current_step" not in st.session_state:
    st.session_state.current_step = 0  

if "q1_index" not in st.session_state: #added
    st.session_state.q1_index = 0 #added

if "responses" not in st.session_state:
    st.session_state.responses = {}

st.title("ТИГР: тренируемся изучать грамматику")

if st.session_state.current_step == 0:
    st.header("Добро пожаловать в тест!")
    st.write("В этом тесте вам предстоит выполнить ОДНО ТЕСТОВОЕ ЗАДАНИЕ.")
    if st.button("Начать"):
        st.session_state.current_step = 1
        st.rerun()
############################################################################################################################################
# Функция для создания HTML с новым дизайном
def create_task1_html(prime_text, stimulus_text, hint):
    html = f"""
    <style>
        .container {{
            display: flex;
            flex-direction: column;
            align-items: flex-start; /* Выравниваем по левому краю */
            text-align: left; /* Текст по левому краю */
            font-size: 1.2em; /* Увеличиваем шрифт */
        }}
        .example {{
            border: 2px solid #ccc;
            background-color: #f0f0f0;
            padding: 15px;
            margin: 10px 0;
            color: #666; /* Серый цвет текста */
            width: 80%;
        }}
        .task {{
            border: 2px solid orange;
            background-color: #ffebcc;
            padding: 15px;
            margin: 10px 0;
            color: black; /* Черный цвет текста */
            width: 80%;
        }}
        .hint {{
            font-style: italic;
            color: #666; /* Серый цвет текста */
        }}
    </style>
    <div class="container">
        <div class="example">
            <strong>Образец:</strong> {prime_text}
        </div>
        <div class="task">
            {stimulus_text}
            <div class="hint">{hint}</div>
        </div>
    </div>
    """
    return html

# Основной код для задания 1
if st.session_state.current_step == 1:
    st.header("Задание 1")
    st.write("Выберите правильное окончание с опорой на предложение-образец.")
    if st.button("Начать тестовое задание"):
        st.session_state.current_step = 2
        st.rerun()

elif st.session_state.current_step == 2:
    index = len(st.session_state.responses)
    if index < len(person_easy):
        task = person_easy[index]

        # Создаем HTML с новым дизайном
        html = create_task1_html(task["prime_text"], task["stimulus_text"], task["hint"])
        st.components.v1.html(html, height=300)

        # Стилизация кнопок
        st.markdown(
            """
            <style>
                .stButton > button {
                    background-color: #ffebcc;
                    border: 2px solid orange;
                    padding: 10px;
                    border-radius: 5px;
                    width: 80%;
                    text-align: left; /* Текст по левому краю */
                    cursor: pointer;
                    margin: 5px 0;
                    font-size: 1.2em;
                }
                .stButton > button:hover {
                    background-color: #ffd699;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # Варианты ответов в виде кнопок
        choice = None
        for answer in task["answers"]:
            if st.button(answer, key=f"q1_{index}_{answer}"):
                choice = answer

        if choice is not None:
            st.session_state.responses[task['stimulus_text']] = choice
            st.rerun()

        #if st.button("Далее") and choice is not None:
            #st.rerun()
    else:
        st.write("Тестовое задание завершено!")
        if st.button("Сохранить результаты"):
            df = pd.DataFrame(list(st.session_state.responses.items()), columns=["Вопрос", "Ответ"])
            filename = f"responses_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
            df.to_csv(filename, index=False)
            # Кнопка для скачивания
            with open(filename, "rb") as f:
                st.download_button(
                    label="Скачать результаты",
                    data=f,
                    file_name=filename,
                    mime="text/csv"
                )

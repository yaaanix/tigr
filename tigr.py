#для запуска нажать пуск справа, потом в создавшуюся консоль написать 
#pipx run streamlit run /Users/anazaharova/Desktop/диплом/ТИГР_ФИНАЛ/tigr.py
import streamlit as st
import pandas as pd
from datetime import datetime
import os
import task_data
os.chdir(os.path.dirname(__file__))  # рабочая директория


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
    st.write("В этом тесте вам предстоит выполнить несколько заданий.")
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

####DEBUG####
#st.session_state.current_step = 11
#############

# Основной код для задания 1
if st.session_state.current_step == 1:
    st.header("Задание 1")
    st.write("Выберите правильное окончание с опорой на предложение-образец.")
    if st.button("Начать задание 1"):
        st.session_state.current_step = 2
        st.rerun()

elif st.session_state.current_step == 2:
    index = len(st.session_state.responses)
    if index < len(task_data.person_easy):
        task = task_data.person_easy[index]

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
            # st.session_state.responses[task['stimulus_text']] = choice
            st.session_state.responses[f"Задание 1: {task['stimulus_text']}"] = choice
            st.rerun()

        #if st.button("Далее") and choice is not None:
            #st.rerun()
    else:
        st.write("Задание 1 завершено!")
        if st.button("Перейти к следующему заданию"):
            st.session_state.current_step = 3
            st.rerun()
############################################################################################################################################
# Функция для создания HTML с новым дизайном для задания 2
def create_task2_html(stimulus_text, hint_text):
    html = f"""
    <style>
        .container {{
            display: flex;
            flex-direction: column;
            align-items: flex-start; /* Выравниваем по левому краю */
            text-align: left; /* Текст по левому краю */
            font-size: 1.2em; /* Увеличиваем шрифт */
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
            font-style: italic; /* Курсив */
            color: #666; /* Серый цвет текста */
            margin-top: 10px; /* Отступ сверху */
        }}
    </style>
    <div class="container">
        <div class="task">
            {stimulus_text}
            <div class="hint">{hint_text}</div>
        </div>
    </div>
    """
    return html

# Основной код для задания 2
if st.session_state.current_step == 3:  
    st.header("Задание 2")
    st.write("Выберите правильный глагол (слово-действие)")
    if st.button("Начать задание 2"):
        st.session_state.current_step = 4
        st.rerun()

elif st.session_state.current_step == 4:
    index = len([k for k in st.session_state.responses.keys() if k.startswith("Задание 2")])    
    if index < len(task_data.person_middle_minus):
        # Создаем HTML с новым дизайном
        html = create_task2_html(
            task_data.person_middle_minus[index],  # Основной текст
            task_data.person_middle_minus_hint[index]  # Подсказка
        )
        st.components.v1.html(html, height=150)

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
        for answer in task_data.person_middle_minus_opt[index]:
            if st.button(answer, key=f"q2_{index}_{answer}"):
                choice = answer

        if choice is not None:
            st.session_state.responses[f"Задание 2: {task_data.person_middle_minus[index]}"] = choice
            st.rerun()

    else:
        st.write("Задание 2 завершено!")
        if st.button("Перейти к следующему заданию"):
            st.session_state.current_step = 5
            st.rerun()
############################################################################################################################################
# Задание 3
# if st.session_state.current_step == 5:
#     st.header("Задание 3")
#     st.write("Соедините подлежащее с правильной формой глагола")
#     if st.button("Начать задание 3"):
#         st.session_state.current_step = 6
#         st.rerun()

# elif st.session_state.current_step == 6:
#     index = len([k for k in st.session_state.responses.keys() if k.startswith("Задание 3")])

#     if index < len(task_data.person_middle_plus):
#         st.subheader(f"Вопрос {index + 1}")

#         st.header("Задание 3")
#         st.write("Перетащите подлежащее в серую сетку, чтобы соединить его с глаголом.")

#         subjects = task_data.person_middle_plus[index]["subjects"]
#         verbs = task_data.person_middle_plus[index]["verbs"]

#         # HTML с тремя колонками: subjects, сетка, глаголы
#         html_code = f"""
#         <style>
#             .container {{
#                 display: flex;
#                 gap: 20px;
#                 width: 100%;  /* Растягиваем на всю страницу */
#             }}
#             .column {{
#                 display: flex;
#                 flex-direction: column;
#                 gap: 10px;
#                 width: 33%;  /* Равномерное распределение колонок */
#             }}
#             .subject {{
#                 background-color: #ffebcc;
#                 border: 2px solid orange;
#                 padding: 10px;
#                 border-radius: 5px;
#                 width: 120px;  /* Размер рамок */
#                 height: 40px;  /* Размер рамок */
#                 display: flex;
#                 align-items: center;
#                 justify-content: center;
#                 cursor: grab;
#                 font-size: 1.1em;  /* Уменьшенный шрифт */
#             }}
#             .drop-zone {{
#                 width: 150px;  /* Размер сетки равен размеру рамок */
#                 height: 60px;  /* Размер сетки равен размеру рамок */
#                 display: flex;
#                 align-items: center;
#                 justify-content: center;
#                 background-color: #ccc;
#                 border: 2px dashed #999;
#                 border-radius: 5px;
#             }}
#             .drop-zone.hovered {{
#                 border-color: #000;
#             }}
#             .verb {{
#                 background-color: #ffebcc;  /* Оранжевый фон */
#                 border: 2px solid orange;  /* Оранжевая рамка */
#                 padding: 10px;
#                 border-radius: 5px;
#                 width: 120px;  /* Размер рамок */
#                 height: 40px;  /* Размер рамок */
#                 display: flex;
#                 align-items: center;
#                 justify-content: center;
#                 font-size: 1.1em;  /* Уменьшенный шрифт */
#             }}
#         </style>
#         <div class="container">
#             <!-- Левая колонка: Подлежащие -->
#             <div class="column">
#                 <div>Подлежащие:</div>
#                 {"".join([f'<div class="subject" draggable="true" data-subject="{subject}">{subject}</div>' for subject in subjects])}
#             </div>

#             <!-- Средняя колонка: Серая сетка -->
#             <div class="column">
#                 <div>Перетащите сюда:</div>
#                 {"".join([f'<div class="drop-zone" data-target="{i}"></div>' for i in range(len(subjects))])}
#             </div>

#             <!-- Правая колонка: Глаголы -->
#             <div class="column">
#                 <div>Глаголы:</div>
#                 {"".join([f'<div class="verb">{verb}</div>' for verb in verbs])}
#             </div>
#         </div>
#         <script>
#             console.log("Скрипт загружен");  // Отладочное сообщение
#             const subjects = document.querySelectorAll('.subject');
#             const dropZones = document.querySelectorAll('.drop-zone');

#             // Обработка перетаскивания
#             subjects.forEach(subject => {{
#                 subject.addEventListener('dragstart', (e) => {{
#                     e.dataTransfer.setData('text/plain', subject.getAttribute('data-subject')); // Сохраняем подлежащее
#                     subject.classList.add('dragging');
#                 }});

#                 subject.addEventListener('dragend', () => {{
#                     subject.classList.remove('dragging');
#                 }});
#             }});

#             dropZones.forEach(zone => {{
#                 zone.addEventListener('dragover', (e) => {{
#                     e.preventDefault();
#                     zone.classList.add('hovered');
#                 }});

#                 zone.addEventListener('dragleave', () => {{
#                     zone.classList.remove('hovered');
#                 }});

#                 zone.addEventListener('drop', (e) => {{
#                     e.preventDefault();
#                     const subject = e.dataTransfer.getData('text/plain'); // Получаем подлежащее

#                     // Если в зоне уже есть подлежащее, возвращаем его в левую колонку
#                     if (zone.textContent) {{
#                         const returnedSubject = document.createElement('div');
#                         returnedSubject.className = 'subject';
#                         returnedSubject.setAttribute('data-subject', zone.textContent);
#                         returnedSubject.textContent = zone.textContent;
#                         returnedSubject.draggable = true;
#                         document.querySelector('.column').appendChild(returnedSubject);
#                     }}

#                     // Удаляем подлежащее из исходного места
#                     const draggedItem = document.querySelector(`.subject[data-subject="${{subject}}"]`);
#                     if (draggedItem) draggedItem.remove();

#                     // Добавляем подлежащее в зону перетаскивания
#                     zone.textContent = subject;
#                     zone.style.backgroundColor = "#ffebcc"; // Оранжевый фон
#                     zone.style.border = "2px solid orange"; // Оранжевая рамка
#                     zone.classList.remove('hovered');

#                     // Делаем зону перетаскиваемой
#                     zone.draggable = true;
#                     zone.addEventListener('dragstart', (e) => {{
#                         e.dataTransfer.setData('text/plain', zone.textContent);
#                         zone.classList.add('dragging');
#                     }});

#                     zone.addEventListener('dragend', () => {{
#                         zone.classList.remove('dragging');
#                     }});

#                     // Отправляем данные обратно в Streamlit
#                     const response = Array.from(dropZones).map(zone => zone.textContent);
#                     Streamlit.setComponentValue(response);
#                 }});
#             }});
#         </script>
#         """
#         # response = st.components.v1.html(html_code, height=600, key=f"drag_drop_{index}")
#         response = st.components.v1.html(html_code, height=600)


#         if response:
#             st.session_state.responses[f"Задание 3: Вопрос {index + 1}"] = {
#                 "verbs": verbs,
#                 "subjects": response
#             }

#         # Кнопка "Далее"
#         if st.button("Далее"):
#             st.rerun()
#     else:
#         st.write("Задание 3 завершено!")
#         if st.button("Перейти к следующему заданию"):
#             st.session_state.current_step = 7
#             st.rerun()

# # Вывод ответов
# if st.session_state.current_step > 6:
#     st.write("Ответы:")
#     for key, value in st.session_state.responses.items():
#         st.write(f"{key}: {value}")
elif st.session_state.current_step == 5:  
    st.header("Задание 3")
    st.write("Соедините подлежащее с правильной формой глагола")
    if st.button("Начать задание 3"):
        st.session_state.current_step = 6
        st.session_state.task3_index = 0  # Инициализация индекса для задания 3
        st.rerun()

elif st.session_state.current_step == 6:  
    # Используем task3_index для отслеживания текущего вопроса в задании 3
    index = st.session_state.task3_index
    
    if index < len(task_data.person_middle_plus):
        st.header("Задание 3")
        st.write("Соедините подлежащее с правильной формой глагола")

        subjects = task_data.person_middle_plus[index]["subjects"]
        verbs = task_data.person_middle_plus[index]["verbs"]

        selected_verbs = [
            st.selectbox(f"{subject}:", [""] + verbs, key=f"verb_{i}_{index}") 
            for i, subject in enumerate(subjects)
        ]

        if st.button("Далее"):
            # Проверяем, выбраны ли все глаголы
            if all(selected_verbs):
                # Сохраняем ответы в формате "стимул-ответ" с префиксом "Задание 3:"
                for i, subject in enumerate(subjects):
                    st.session_state.responses[f"Задание 3: {subject}"] = selected_verbs[i]
                
                # Увеличиваем индекс для следующего вопроса
                st.session_state.task3_index += 1
                st.rerun()  # Обновляем страницу для следующего вопроса
            else:
                st.warning("Выберите все глаголы перед переходом.")
    else:
        st.write("Задание 3 завершено!")
        if st.button("Перейти к следующему заданию"):
            st.session_state.current_step = 7
            st.rerun()
############################################################################################################################################
# Функция для создания HTML с новым дизайном для задания 4
def create_task4_html(stimulus_text):
    html = f"""
    <style>
        .container {{
            display: flex;
            flex-direction: column;
            align-items: flex-start; /* Выравниваем по левому краю */
            text-align: left; /* Текст по левому краю */
            font-size: 1.2em; /* Увеличиваем шрифт */
        }}
        .task {{
            border: 2px solid orange;
            background-color: #ffebcc;
            padding: 15px;
            margin: 10px 0;
            color: black; /* Черный цвет текста */
            width: 80%;
        }}
    </style>
    <div class="container">
        <div class="task">
            {stimulus_text}
        </div>
    </div>
    """
    return html

# Основной код для задания 4
if st.session_state.current_step == 7:  # Титульный лист задания 4
    st.header("Задание 4")
    st.write("Напечатайте пропущенное слово (в скобках) в подходящей форме настоящего времени")
    if st.button("Начать задание 4"):
        st.session_state.current_step = 8
        st.rerun()

elif st.session_state.current_step == 8:  # Задание 4 (ввод ответа)
    index = len([k for k in st.session_state.responses.keys() if k.startswith("Задание 4")])
    
    if index < len(task_data.person_complex):
        # Создаем HTML с новым дизайном
        html = create_task4_html(task_data.person_complex[index])
        st.components.v1.html(html, height=150)

        # Поле для ввода ответа
        answer = st.text_input(
            "Напечатайте пропущенное слово (в скобках) в подходящей форме настоящего времени",
            key=f"q4_{index}"
        )

        if st.button("Далее") and answer:
            st.session_state.responses[f"Задание 4: {task_data.person_complex[index]}"] = answer
            st.rerun()
    else:
        st.write("Задание 4 завершено!")
        if st.button("Перейти к следующему заданию"):
            st.session_state.current_step = 9
            st.rerun()
############################################################################################################################################
# Функция для создания HTML с новым дизайном для задания 5
def create_task5_html(prime_text, stimulus_text, hint):
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
#################################################################################################
# Основной код для задания 5
if st.session_state.current_step == 9:
    st.header("Задание 5")
    st.write("Выберите правильный глагол с опорой на предложение-образец")
    if st.button("Начать задание 5"):
        st.session_state.current_step = 10
        st.rerun()

elif st.session_state.current_step == 10:
    index = len([k for k in st.session_state.responses.keys() if k.startswith("Задание 5")])
    
    if index < len(task_data.gender_easy):
        task5 = task_data.gender_easy[index]

        # Создаем HTML с новым дизайном
        html = create_task5_html(task5["prime_text"], task5["stimulus_text"], task5["hint"])
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
        for answer in task5["answers"]:
            if st.button(answer, key=f"q5_{index}_{answer}"):
                choice = answer

        if choice is not None:
            st.session_state.responses[f"Задание 5: {task5['stimulus_text']}"] = choice
            st.rerun()

        #if st.button("Далее") and choice is not None:
        #    st.rerun()
    else:
        st.write("Задание 5 завершено!")
        if st.button("Перейти к следующему заданию"):
            st.session_state.current_step = 11
            st.rerun()
############################################################################################################################################
# Основной код для задания 6
if st.session_state.current_step == 11:
    st.header("Задание 6")
    st.write("Соедините картинки с правильной формой глагола")
    if st.button("Начать задание 6"):
        st.session_state.current_step = 12
        st.rerun()

# Задание 6
if st.session_state.current_step == 12:
    # index = len([k for k in st.session_state.responses.keys() if k.startswith("Задание 6")])
    
    # #st.write(f"Текущий индекс: {index}")  # Отладочное сообщение
    # #st.write(f"Длина task_data.gender_middle_minus: {len(task_data.gender_middle_minus)}")  # Отладочное сообщение
    
    # if index < len(task_data.gender_middle_minus):
    #     st.write("Перетащите глаголы в соответствующие серые квадраты.")

    #     # Отображение картинок
    #     st.write("Картинки:")
    #     col1, col2, col3 = st.columns(3)
    #     with col1:
    #         st.image(f"images/{task_data.gender_middle_minus[index][0]}", use_container_width=True, width=150)
    #     with col2:
    #         st.image(f"images/{task_data.gender_middle_minus[index][1]}", use_container_width=True, width=150)
    #     with col3:
    #         st.image(f"images/{task_data.gender_middle_minus[index][2]}", use_container_width=True, width=150)

    #     # Отображение глаголов в оранжевых рамках
    #     st.write("Глаголы:")
    #     html_code = f"""
    #     <style>
    #         .verb-button {{
    #             background-color: #ffebcc;
    #             border: 2px solid orange;
    #             padding: 10px;
    #             border-radius: 5px;
    #             width: 150px;
    #             height: 50px;
    #             display: flex;
    #             align-items: center;
    #             justify-content: center;
    #             cursor: grab;
    #             margin: 0 10px;
    #             font-size: 1.2em;
    #         }}
    #         .verb-button:hover {{
    #             background-color: #ffd699;
    #         }}
    #         .drop-zone {{
    #             width: 170px;
    #             height: 70px;
    #             display: flex;
    #             align-items: center;
    #             justify-content: center;
    #             background-color: #ccc;
    #             border: 2px dashed #999;
    #             border-radius: 5px;
    #             margin: 0 10px;
    #         }}
    #         .drop-zone.hovered {{
    #             border-color: #000;
    #         }}
    #         #drag-items, #drop-zones {{
    #             display: flex;
    #             justify-content: center;
    #             gap: 10px;
    #             margin: 20px 0;
    #         }}
    #     </style>
    #     <div id="drag-container">
    #         <div id="drag-items">
    #             <div class="verb-button" draggable="true" data-verb="{task_data.gender_middle_minus_opt[index][0]}">{task_data.gender_middle_minus_opt[index][0]}</div>
    #             <div class="verb-button" draggable="true" data-verb="{task_data.gender_middle_minus_opt[index][1]}">{task_data.gender_middle_minus_opt[index][1]}</div>
    #             <div class="verb-button" draggable="true" data-verb="{task_data.gender_middle_minus_opt[index][2]}">{task_data.gender_middle_minus_opt[index][2]}</div>
    #         </div>
    #         <div id="drop-zones">
    #             <div class="drop-zone"></div>
    #             <div class="drop-zone"></div>
    #             <div class="drop-zone"></div>
    #         </div>
    #     </div>
    #     <script>
    #         console.log("Скрипт загружен");  // Отладочное сообщение
    #         const dragItems = document.querySelectorAll('.verb-button');
    #         const dropZones = document.querySelectorAll('.drop-zone');

    #         // Обработка перетаскивания
    #         dragItems.forEach(item => {{
    #             item.addEventListener('dragstart', (e) => {{
    #                 e.dataTransfer.setData('text/plain', item.getAttribute('data-verb')); // Сохраняем глагол
    #                 item.classList.add('dragging');
    #             }});

    #             item.addEventListener('dragend', () => {{
    #                 item.classList.remove('dragging');
    #             }});
    #         }});

    #         dropZones.forEach(zone => {{
    #             zone.addEventListener('dragover', (e) => {{
    #                 e.preventDefault();
    #                 zone.classList.add('hovered');
    #             }});

    #             zone.addEventListener('dragleave', () => {{
    #                 zone.classList.remove('hovered');
    #             }});

    #             zone.addEventListener('drop', (e) => {{
    #                 e.preventDefault();
    #                 const verb = e.dataTransfer.getData('text/plain'); // Получаем глагол

    #                 // Удаляем глагол из исходного места
    #                 const draggedItem = document.querySelector(`.verb-button[data-verb="${{verb}}"]`);
    #                 draggedItem.remove();

    #                 // Добавляем глагол в зону перетаскивания
    #                 zone.textContent = verb;
    #                 zone.style.backgroundColor = "#ffebcc"; // Оранжевый фон
    #                 zone.style.border = "2px solid orange"; // Оранжевая рамка
    #                 zone.classList.remove('hovered');
    #             }});
    #         }});
    #     </script>
    #     """
    #     st.components.v1.html(html_code, height=300)

    #     # Кнопка "Далее"
    #     if st.button("Далее"):
    #         # Сохраняем имена файлов картинок
    #         st.session_state.responses[f"Задание 6: Картинки {task_data.gender_middle_minus[index]}"] = f"Глаголы: {task_data.gender_middle_minus_opt[index]}"
    #         st.rerun()
    # else:
    #     st.write("Задание 6 завершено!")
    #     if st.button("Перейти к следующему заданию"):
    #         st.session_state.current_step = 13
    #         st.rerun()

####temp####
    index = int( len([k for k in st.session_state.responses.keys() if k.startswith("Задание 6")]) / 3) #divide in 3 bcause 3 answ

    if index < len(task_data.gender_middle_minus_opt):
        #     st.write("Перетащите глаголы в соответствующие серые квадраты.")
        st.header("Задание 6")
        # Отображение картинок
        image_names = task_data.gender_middle_minus[index]
        verbs = task_data.gender_middle_minus_opt[index]
        index_answrs = [] #answers for current index

        st.write("Картинки:")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(f"images/{image_names[0]}", use_container_width=True, width=150)
            index_answrs.append(st.selectbox("Выберите форму:", verbs, key=f"verb_1_{index}"))
        with col2:
            st.image(f"images/{image_names[1]}", use_container_width=True, width=150)
            index_answrs.append(st.selectbox("Выберите форму:", verbs, key=f"verb_2_{index}"))
        with col3:
            st.image(f"images/{image_names[2]}", use_container_width=True, width=150)
            index_answrs.append(st.selectbox("Выберите форму:", verbs, key=f"verb_3_{index}"))


        if st.button("Далее"):
            # Проверяем, выбраны ли все глаголы
            if len(index_answrs)==3 and not any(item == "" for item in index_answrs):
                # Сохраняем ответы в формате "стимул-ответ" с префиксом "Задание 3:"
                for i, subject in enumerate(index_answrs):
                    st.session_state.responses[f"Задание 6: Картина {image_names[i]}: "] = index_answrs[i]
                st.rerun()  # Обновляем страницу для следующего вопроса
            else:
                st.warning("Выберите все глаголы перед переходом.")
    else:
        st.write("Задание 6 завершено!")
        if st.button("Перейти к следующему заданию"):
            st.session_state.current_step = 13
            st.rerun()
############################################################################################################################################
# Функция для создания HTML с новым дизайном для задания 7
def create_task7_html(stimulus_text):
    html = f"""
    <style>
        .container {{
            display: flex;
            flex-direction: column;
            align-items: flex-start; /* Выравниваем по левому краю */
            text-align: left; /* Текст по левому краю */
            font-size: 1.2em; /* Увеличиваем шрифт */
        }}
        .task {{
            border: 2px solid orange;
            background-color: #ffebcc;
            padding: 15px;
            margin: 10px 0;
            color: black; /* Черный цвет текста */
            width: 80%;
        }}
    </style>
    <div class="container">
        <div class="task">
            {stimulus_text}
        </div>
    </div>
    """
    return html

# Основной код для задания 7
if st.session_state.current_step == 13:  
    st.header("Задание 7")
    st.write("Выберите правильную форму глагола.")
    if st.button("Начать задание 7"):
        st.session_state.current_step = 14
        st.rerun()

elif st.session_state.current_step == 14:
    index = len([k for k in st.session_state.responses.keys() if k.startswith("Задание 7")])
    
    if index < len(task_data.gender_middle_plus):
        # Создаем HTML с новым дизайном
        html = create_task7_html(task_data.gender_middle_plus[index])
        st.components.v1.html(html, height=150)

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
        for answer in task_data.gender_middle_plus_opt[index]:
            if st.button(answer, key=f"q7_{index}_{answer}"):
                choice = answer

        if choice is not None:
            st.session_state.responses[f"Задание 7: {task_data.gender_middle_plus[index]}"] = choice
            st.rerun()

        #if st.button("Далее") and choice is not None:
        #    st.rerun()
    else:
        st.write("Задание 7 завершено!")
        if st.button("Перейти к следующему заданию"):
            st.session_state.current_step = 15
            st.rerun()
############################################################################################################################################
# Функция для создания HTML с новым дизайном для задания 8
def create_task8_html(stimulus_text):
    html = f"""
    <style>
        .container {{
            display: flex;
            flex-direction: column;
            align-items: flex-start; /* Выравниваем по левому краю */
            text-align: left; /* Текст по левому краю */
            font-size: 1.2em; /* Увеличиваем шрифт */
        }}
        .task {{
            border: 2px solid orange;
            background-color: #ffebcc;
            padding: 15px;
            margin: 10px 0;
            color: black; /* Черный цвет текста */
            width: 80%;
        }}
    </style>
    <div class="container">
        <div class="task">
            {stimulus_text}
        </div>
    </div>
    """
    return html

# Основной код для задания 8
if st.session_state.current_step == 15:  # Титульный лист задания 8
    st.header("Задание 8")
    st.write("Напечатайте пропущенное слово (в скобках) в подходящей форме прошедшего времени")
    if st.button("Начать задание 8"):
        st.session_state.current_step = 16
        st.rerun()

elif st.session_state.current_step == 16:  # Задание 8 (ввод ответа)
    index = len([k for k in st.session_state.responses.keys() if k.startswith("Задание 8")])
    
    if index < len(task_data.gender_complex):
        # Создаем HTML с новым дизайном
        html = create_task8_html(task_data.gender_complex[index])
        st.components.v1.html(html, height=150)

        # Поле для ввода ответа
        answer = st.text_input(
            "Напечатайте пропущенное слово (в скобках) в подходящей форме прошедшего времени",
            key=f"q8_{index}"
        )

        if st.button("Далее") and answer:
            st.session_state.responses[f"Задание 8: {task_data.gender_complex[index]}"] = answer
            st.rerun()
    else:
        st.write("Задание 8 завершено!")
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
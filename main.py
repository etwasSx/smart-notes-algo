# подключение требуемых библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QListWidget, QLabel, QPushButton, QLineEdit, QTextEdit, QHBoxLayout, QVBoxLayout,
    QInputDialog
)

import json

# Подключаем библиотеку json

# Тут у нас будет структура для заметок
notes = {}  # Теперь наш словарь будет загружаться из файла и нам не надо будет создавать ручками

# Создадим окно приложения
app = QApplication([])
main_window = QWidget()  # И так же создадим главное окно приложения
main_window.setWindowTitle("Мои Заметки")  # Дадим ему название
main_window.resize(900, 600)  # Дадим размеры окну и сделаем его видимым

# Теперь создадим используемые виджеты приложения
list_notes = QListWidget()
list_notes_label = QLabel("Список заметок")

# Кнопки для нашего списка заметок
btn_note_create = QPushButton("Создать заметку")
btn_note_delete = QPushButton("Удалить заметку")
btn_note_save = QPushButton("Сохранить заметку")

field_tag = QLineEdit("")
field_tag.setPlaceholderText("Введите тег..")  # текст подсказка

# поле для самой заметки. Сюда будем ее вводить
field_text = QTextEdit()

# Список тегов
list_tags = QListWidget()
list_tags_label = QLabel("Список тегов")

# кнопки для списка тегов
button_tag_add = QPushButton("Добавить тег")
button_tag_del = QPushButton("Удалить тег")
button_tag_search = QPushButton("Искать тег")

# пока что у нас ничего не прикреплено по лайаутам и при запуске приложения будет пустота
# теперь чтобы показать нашу красоту пользователю, используем лайауты
layout_notes = QHBoxLayout()  # Вертикальный основной лайаут, прикрепим к окну

column_left = QVBoxLayout()  # Левый столбец
column_left.addWidget(field_text)  # добавим сюда поле ввода

column_right = QVBoxLayout()  # Правый столбец с списками
column_right.addWidget(list_notes_label)
column_right.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(btn_note_create)
row_1.addWidget(btn_note_save)
row_2 = QHBoxLayout()
row_2.addWidget(btn_note_delete)

column_right.addLayout(row_1)
column_right.addLayout(row_2)

# Теперь повторим те же действия, но для списка тегов
column_right.addWidget(list_tags_label)
column_right.addWidget(list_tags)
column_right.addWidget(field_tag)  # поле появилось

# Остались кнопки
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)

# кнопки не появились потому что мы их не прикрепили к столбцу. Делаем
column_right.addLayout(row_3)
column_right.addLayout(row_4)

# Добавили поле для ввода текста и праый столбец
layout_notes.addLayout(column_left, stretch=2)
layout_notes.addLayout(column_right, stretch=1)


def show_note():
    key = list_notes.selectedItems()[0].text()  # Получаем текст нашей заметки. Это нулевой индекс
    field_text.setText(notes[key]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[key]["теги"])


# Функция для создания заметки
def add_note():
    note_name, ok = QInputDialog.getText(main_window, "Добавить", "Название:")
    if ok and note_name != "":  # если не пустой текст заметки и нажат ок
        notes[note_name] = {"текст": "", "теги": []}  # Пока значения пустые
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]["теги"])
        with open("notes.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False)  # последний параметр нужен чтобы файл был виден на русском


# Функция для Сохранения заметки
def save_note():
    if list_notes.selectedItems():  # Если выбран элемент, заметка
        key = list_notes.selectedItems()[0].text()  # Название заметки *
        notes[key]["текст"] = field_text.toPlainText()
        with open("notes.json", "w", encoding="utf-8") as file:  # тут была ошибка. Надо добавить as file
            json.dump(notes, file, ensure_ascii=False)
    else:
        print("Заметка не выбрана. Сохранять нечего")


# Функция для удаления
def delete_note():
    if list_notes.selectedItems():  # если какая то заметка выбрана
        key = list_notes.selectedItems()[0].text()  # Берем название заметки
        del notes[key]  # Удаляем ее по названию
        list_notes.clear()
        list_tags.clear()
        field_text.clear()  # Чистим все окна
        list_notes.addItems(notes)  # обновляем содержимое списка заметок
        with open("notes.json", "w", encoding="utf-8") as file:  # Сохраним изменения в файл
            json.dump(notes, file, ensure_ascii=False)

    else:
        print("Заметка не выбрана. Нечего удалять")


# Функция для добавления тега
def add_tag():
    if list_notes.selectedItems():  # Будем устанавливать тег только тогда, когда выбрана какая то заметка
        key = list_notes.selectedItems()[0].text()  # Берем название заметки
        tag = field_tag.text()  # Сохраняем в переменную тег заметки. Использовал не то поле. Нужно field_tag
        if not tag in notes[key]["теги"]:  # Если такого тега еще нет в списке тегов этой заметки, тогда будем добавляеть
            notes[key]["теги"].append(tag)  # теги - это список, добавляем в конец
            list_tags.addItem(tag)  # Добавляем в список тегов наш только что созданный тег
            field_tag.clear()  # Очищаем поле ввода тега
        with open("notes.json", "w", encoding="utf-8") as file:  # Сохраним изменения в файл
            json.dump(notes, file, ensure_ascii=False)
    else:
        print("Заметка не выбрана")


# Функция для удаления тега
def delete_tag():
    if list_notes.selectedItems():  # Будем устанавливать тег только тогда, когда выбрана какая то заметка
        key = list_notes.selectedItems()[0].text()  # Берем название заметки
        tag = list_tags.selectedItems()[0].text()  # Берем имя тега
        notes[key]["теги"].remove(tag)  # Удаляем заметку из списка заметок
        list_tags.clear()
        list_tags.addItems(notes[key]["теги"]) # Обновляем список тегов

        with open("notes.json", "w", encoding="utf-8") as file:  # Сохраним изменения в файл
            json.dump(notes, file, ensure_ascii=False)
    else:
        print("Заметка для удаления не выбрана")


# Теперь самое сложное в этой части. Поиск ЗАМЕТОК по тегам
def search_tag():
    tag = field_tag.text() # Берем текст тега по которому будем искать заметки
    if button_tag_search.text() == "Искать тег": # Если мы нажимаем кнопку и у нее текст искать - Ищем
        notes_searched = {} # В этом словаре будут храниться найденные заметки
        for note in notes:
            if tag in notes[note]["теги"]:
                notes_searched[note] = notes[note] # Если что то нашли, дублируем в словарь notes_searched. Его потом покажем пользователю

            button_tag_search.setText("Сбросить поиск")
            list_notes.clear()
            list_tags.clear()
            list_notes.addItems(notes_searched) # В списке заметок отобразим только те, что были найдены

    elif button_tag_search.text() == "Сбросить поиск": # Если нажимаем на кнопку с надписью сбросить поиск, то вернем обычный вид
        list_notes.clear()
        list_tags.clear()
        field_tag.clear()
        list_notes.addItems(notes) # Отобразим обычную версию заметок
        button_tag_search.setText("Искать тег") # Поменяем текст кнопки


''' ЗАПУСК ПРИЛОЖЕНИЯ '''

''' функции обработчики'''
# Покажем список заметок пользователю
list_notes.itemClicked.connect(show_note)

# Создадим заметку
btn_note_create.clicked.connect(add_note)
# Сохраним заметку
btn_note_save.clicked.connect(save_note)
# Удалим заметку. Все отлично работает
btn_note_delete.clicked.connect(delete_note)

# Добавим тег к заметке
button_tag_add.clicked.connect(add_tag)
# Удалим тег у заметки
button_tag_del.clicked.connect(delete_tag)
# Поиск по тегам
button_tag_search.clicked.connect(search_tag)
# На этом все.

#
''' ОКНО '''
main_window.setLayout(layout_notes)

main_window.show()

# Теперь добавим считывание из файла и покажем название заметки в списке
with open("notes.json", "r", encoding="utf-8") as file:
    notes = json.load(file)
list_notes.addItems(notes)

# У нас появилась заметка. Но при нажатии на нее ничего не открывается. Исправим.
# Создадим для этого функцию обработчик

app.exec_()

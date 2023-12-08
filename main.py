# подключение требуемых библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QListWidget, QLabel, QPushButton, QLineEdit, QTextEdit, QHBoxLayout, QVBoxLayout
)

# Создадим окно приложения
app = QApplication([])
main_window = QWidget() # И так же создадим главное окно приложения
main_window.setWindowTitle("Мои Заметки") # Дадим ему название
main_window.resize(900, 600) # Дадим размеры окну и сделаем его видимым

# Теперь создадим используемые виджеты приложения
list_notes = QListWidget()
list_notes_label = QLabel("Список заметок")

# Кнопки для нашего списка заметок
btn_note_create = QPushButton("Создать заметку")
btn_note_delete = QPushButton("Удалить заметку")
btn_note_save = QPushButton("Сохранить заметку")

field_tag = QLineEdit("")
field_tag.setPlaceholderText("Введите тег..") # текст подсказка

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
layout_notes = QHBoxLayout() # Вертикальный основной лайаут, прикрепим к окну

column_left = QVBoxLayout() # Левый столбец
column_left.addWidget(field_text) # добавим сюда поле ввода

column_right = QVBoxLayout() # Правый столбец с списками
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
layout_notes.addLayout(column_left)
layout_notes.addLayout(column_right)
main_window.setLayout(layout_notes)

main_window.show()

app.exec_()

# На этом заготовка готова
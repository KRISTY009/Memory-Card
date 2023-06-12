#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *

number = -1

app = QApplication([])
win = QWidget()
win.show()
win.setWindowTitle('Memory Card')
win.resize(450,300)

class Question():
    def __init__(self,question,true_ans0,false_ans1,false_ans2,false_ans3):
        self.question = question
        self.true_ans0 = true_ans0
        self.false_ans1 = false_ans1
        self.false_ans2 = false_ans2
        self.false_ans3 = false_ans3

idi1 = Question('Какой приз вас ждёт за ответ на вопрос?','Больше вопросов','Отдых','1.000.000 рублей','Волшебное предсказание')
idi2 = Question('Джордж Оруэлл, объясняя выбор темы для одного из своих эссе, писал: \n"Это весьма любопытно. И не только потому, что это одна из опор британской цивилизации, но и потому, что лучший способ является предметом ожесточенных споров".\n В эссе приводится 11 способов. Чего??','Заваривания чая','Готовки пельменей','Мест для сна','Вариантов проведения отпуска')
idi3 = Question('Российский мультфильм, удостоенный «Оскара», — это…','Старик и море','Простоквашино','Басни','Колобок')
idi4 = Question('Кто из знаменитых художников за жизнь продал всего одну картину?','Винсент Ван Гог','Пьер Огюст Ренуар','И. К. Айвазовский','Леонардо да Винчи')
idi5 = Question('Что в Российской империи было вещевым эквивалентом денег?','Шкуры пушных зверей','Женские серьги','Соль и сахар','Крупный рогатый скот')
idi6 = Question('Представте: вы падаете в яму, полную змей. Как выжить?','Перестать воображать','Взлететь','Сжаться в клубок','Попытаться упасть там, где их нет')
idi7 = Question('До открытия горы Эверест, какая гора была самой высокой?','Эверест','Уральские горы','Белуха','Монте-Роза')
idi8 = Question('Выберете правильный вариант на вопрос: Если вампир укусит зомби, зомби станет вампиром или вампир станет зомби? ','Правильный вариант на вопрос','Зомби станет вампиром','Вампир станет зомби','Вселенная схлопнется') 
idi9 = Question('Может ли пингвин назвать себя птицей?','Пингвины не имет разговаривать','Да','Нет','42')

questions = [idi1,idi2,idi3,idi4,idi5,idi6,idi7,idi8,idi9]

ans_1 = QRadioButton('.')
ans_2 = QRadioButton('.')
ans_3 = QRadioButton('.')
ans_4 = QRadioButton('.')

text = QLabel('.')
button = QPushButton('Ответить')
is_it_true = QLabel('оно не работает')
fin_true_answer = QLabel('.')

answers = [ans_1,ans_2,ans_3,ans_4]

group = QButtonGroup()
group.addButton(ans_1)
group.addButton(ans_2)
group.addButton(ans_3)
group.addButton(ans_4)

main_line = QVBoxLayout()

line_1 = QHBoxLayout()
line_1.addWidget(text, alignment = Qt.AlignCenter)

group1 = QGroupBox('Варианты ответа:')

line_2_main = QHBoxLayout()
line_2_main.addSpacing(5)
line_2_1 = QVBoxLayout()
line_2_2 = QVBoxLayout()

line_2_1.addWidget(ans_1)
line_2_1.addWidget(ans_2)
line_2_2.addWidget(ans_3)
line_2_2.addWidget(ans_4)

line_2_main.addLayout(line_2_1)
line_2_main.addLayout(line_2_2)
group1.setLayout(line_2_main)
#line_2 = QHBoxLayout()
#line_2.addWidget(group)

line_3 = QHBoxLayout()
line_3.addStretch(1)
line_3.addWidget(button,alignment = Qt.AlignVCenter, stretch = 2)
line_3.addStretch(1)


line_2sek = QVBoxLayout()
line_2sek.addSpacing(5)
line_2sek.addWidget(is_it_true, alignment = Qt.AlignLeft)
line_2sek.addSpacing(15)
line_2sek.addWidget(fin_true_answer, alignment = Qt.AlignCenter)

group2 = QGroupBox('Результат теста:')
group2.setLayout(line_2sek)

group2.hide()
#group1.hide()
def show_result():
    group1.hide()
    group2.show()
    button.setText('Следующий вопрос')
    group.setExclusive(False)
    ans_1.setChecked(False)
    ans_2.setChecked(False)
    ans_3.setChecked(False)
    ans_4.setChecked(False)
    group.setExclusive(True)

def show_question():
    group2.hide()
    group1.show()
    button.setText('Ответить')

def ask(q):
    shuffle(answers)
    answers[0].setText(q.true_ans0)
    answers[1].setText(q.false_ans1)
    answers[2].setText(q.false_ans2)
    answers[3].setText(q.false_ans3)
    text.setText(q.question)
    fin_true_answer.setText(q.true_ans0)
    show_question()

def show_correct(res):
    is_it_true.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно! :)')
    elif  answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неправильно! :(')

def next_question():
    global number, questions
    number += 1
    if number >= len(questions) - 1:
        number = -1
    q = questions[number]
    ask(q)

def start_test():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

next_question()
button.clicked.connect(start_test)

main_line.addLayout(line_1)
main_line.addWidget(group1, alignment = Qt.AlignVCenter)
main_line.addWidget(group2, alignment = Qt.AlignVCenter)
# main_line.addLayout(line_2)
main_line.addLayout(line_3)

win.setLayout(main_line)

app.exec_()

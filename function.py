import file_operation
import Note

min_len = 4  # сколько знаков МИНИМУМ может быть в тексте заметки

def menu():
    print('\nЭто программа Заметки.\n\nВозможны следующие действия:\n[1] - Вывод всех заметок из файла\n[2] - Добавление заметки\n[3] - Удаление заметки\n[4] - Редактирование заметки\n[5] - Выборка заметок по дате\n[6] - Показать заметку по ID\n[7] - Выход\n\nВыберите необходимое действие: ')

def goodbuy():
    print('До свидания!')

def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов.\n')
        text = input('Введите текст: ')
    else:
        return text

def create_note(min_len):
    title = check_len_text_input(
        input('Введите Название заметки: '), min_len)
    body = check_len_text_input(
        input('Введите Описание заметки: '), min_len)
    return Note.Note(title=title, body=body)

def add():
    note = create_note(min_len)
    array = file_operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, 'a')
    print('Заметка добавлена...')

def show(text):
    logic = True
    array = file_operation.read_file()
    for notes in array:
        match text:
            case 'all': 
                logic = False
                print(Note.Note.map_note(notes))
            case 'id': 
                logic = False
                print('ID: ' + Note.Note.get_id(notes))
            case 'date':
                logic = False
                input_date = input('Введите дату в формате dd.mm.yyyy: ')
                if input_date in Note.Note.get_date(notes):
                    print(Note.Note.map_note(notes))
    if logic == True:
        print('Нет ни одной заметки...')

def id_edit_del_show(text):
    id = input('Введите ID необходимой заметки: ')
    array = file_operation.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            match text:
                case 'edit':
                    note = create_note(min_len)
                    Note.Note.set_title(notes, note.get_title())
                    Note.Note.set_body(notes, note.get_body())
                    Note.Note.set_date(notes)
                    print('Заметка изменена...')
                case 'del':
                    array.remove(notes)
                    print('Заметка удалена...')
                case 'show':
                    print(Note.Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный ID.')
    file_operation.write_file(array, 'a')
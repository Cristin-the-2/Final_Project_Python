import function as f

input_from_user = 0
while input_from_user != 7:
    f.menu()
    input_from_user = int(input())
    match input_from_user:
        case 1: f.show('all')
        case 2: f.add()
        case 3: 
            f.show('all')
            f.id_edit_del_show('del')
        case 4:
            f.show('all')
            f.id_edit_del_show('edit')
        case 5: f.show('date')
        case 6:
            f.show('id')
            f.id_edit_del_show('show')
        case 7: 
            f.goodbuy()
            break
        case _: print('Нет такого действия.')
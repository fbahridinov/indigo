from openpyxl import load_workbook


def add_employees():

    db = 'indigo_db.xlsx'
    wb = load_workbook(db)
    ws = wb['employees']
    ws.append(employee)
    wb.save(db)
    wb.close()

    print('\n Сотрудник успешно добавлен...')
    return employee


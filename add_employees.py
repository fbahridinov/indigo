from openpyxl import load_workbook


def add_employees():
    employee = []
    last_name = input('Фамилия: ')
    employee.append(last_name)
    name = input('Имя: ')
    employee.append(name)
    date_birth = input('Дата рождения: ')
    employee.append(date_birth)
    department = input('Отделение: ')
    employee.append(department)
    job_title = input('Должность: ')
    employee.append(job_title)
    status = input('Статус: ')
    employee.append(status)

    db = 'indigo_db.xlsx'
    wb = load_workbook(db)
    ws = wb['employees']
    ws.append(employee)
    wb.save(db)
    wb.close()

    print('\n Сотрудник успешно добавлен...')
    return employee


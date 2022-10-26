import openpyxl


def print_x():
    personal_list = openpyxl.open('indigo_db.XLSX', 'r')

    sheet = personal_list.active

    for colum in range(1, sheet.max_row + 1):
        last_name = sheet[colum][0].value
        name = sheet[colum][1].value
        date_birth = sheet[colum][2].value
        department = sheet[colum][3].value
        job_title = sheet[colum][4].value
        status = sheet[colum][5].value
        print(f"""------------------------------------------------------------------------------------------------------
        {last_name}     | {name}     | {date_birth}     | {department}     | {job_title}     | {status} """)



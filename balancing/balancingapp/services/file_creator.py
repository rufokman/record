from django.http import HttpResponse
from ..models import Card
import xlsxwriter


def download_excel_data1(request):
	# content-type of response
	response = HttpResponse(content_type='application/ms-excel')

	# decide file name
	response['Content-Disposition'] = 'attachment; filename="pivot.xlsx"'

	# creating workbook
	wb = xlsxwriter.Workbook(response, {'in_memory': True})

	# adding sheet
	ws = wb.add_worksheet()

	# Sheet header, first row
	row_num = 0

	font_style = xlwt.XFStyle()
	# headers are bold
	font_style.font.bold = True

	# column header names, you can use your own headers here
	columns = ['Column 1', 'Column 2', 'Column 3', 'Column 4', ]

	# write column headers in sheet
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)

	# Sheet body, remaining rows
	font_style = xlwt.XFStyle()

	# get your data, from database or from a text file...
	data = Card.objects.all()
	for my_row in data:
		row_num = row_num + 1
		ws.write(row_num, 0, my_row.organization, font_style)
		ws.write(row_num, 1, my_row.function, font_style)
		ws.write(row_num, 2, my_row.role, font_style)
		ws.write(row_num, 3, my_row.fio, font_style)

	wb.save(response)
	return response


def download_excel_data(request):
	data = Card.objects.all()
	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename="pivot.xlsx"'
	workbook = xlsxwriter.Workbook(response, {'in_memory': True})
	ws = workbook.add_worksheet('Реестр')
	# wrap_format = ws.for add_format({'border': 1, 'text_wrap': True, 'align': 'left', 'valign': 'vcenter'})
	row_num = 0
	columns = ['№ пп', 'Организация', 'Функция', 'Название должности',
			   'ФИО сотрудника, в чью карту устанавливается КПЭ',
			   'ID КПЭ в ИС РЕКОРД', 'Наименование КПЭ / КлС', 'КПЭ / КлС2',
			   'Тип КПЭ / КлС (Методика расчета)', 'Нижний уровень', "Целевой уровень",
			   "Верхний уровень", "Вес", "Паспорт", "Факт выполнения", "Инициатор / Верификатор",
			   "Комментарий от функции (по необходимости)",
			   "Комментарии по аудиту (заполняется СУП УК)",
			   "Комментарии по аудиту (заполняется сотрудником АЭС/ДО)",
			   ]

	ws.set_column('A:A', 5)
	ws.set_column('B:B', 23)
	ws.set_column('C:C', 23, )
	ws.set_column('D:D', 23, )
	ws.set_column('E:E', 26, )
	ws.set_column('F:F', 11, )
	ws.set_column('G:G', 81, )
	ws.set_column('H:H', 16, )
	ws.set_column('I:I', 20, )
	ws.set_column('J:J', 20, )
	ws.set_column('K:K', 30, )
	ws.set_column('L:L', 20, )
	ws.set_column('M:M', 7, )
	ws.set_column('N:N', 17, )
	ws.set_column('O:O', 17, )
	ws.set_column('P:P', 40, )
	ws.set_column('Q:Q', 24, )
	ws.set_column('R:R', 24, )
	ws.set_column('S:S', 24, )

	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num])

	for my_row in data:
		row_num = row_num + 1
		ws.write(row_num, 0, row_num)
		ws.write(row_num, 1, my_row.organization)
		ws.write(row_num, 2, my_row.function)
		ws.write(row_num, 3, my_row.role)
		ws.write(row_num, 4, my_row.fio)
		ws.write(row_num, 5, "ID КПЭ в ИС РЕКОРД")
		ws.write(row_num, 6, my_row.name)
		ws.write(row_num, 7, "КПЭ / КлС2")
		ws.write(row_num, 8, my_row.method)
		ws.write(row_num, 9, my_row.low_level)
		ws.write(row_num, 10, my_row.target_level)
		ws.write(row_num, 11, my_row.high_level)
		ws.write(row_num, 12, my_row.weight)
		ws.write(row_num, 13, "Паспорт")
		ws.write(row_num, 14, "Факт выполнения")
		ws.write(row_num, 15, "Инициатор / Верификатор")
		ws.write(row_num, 16, "Комментарий от функции (по необходимости)")
		ws.write(row_num, 17, "Комментарии по аудиту (заполняется СУП УК)")
		ws.write(row_num, 18, "Комментарии по аудиту (заполняется сотрудником АЭС/ДО)")






	workbook.close()

	return response

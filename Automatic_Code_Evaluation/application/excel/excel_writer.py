import xlwt
from xlwt import Workbook


def write(filename, records):
    book = Workbook()
    sheet = book.add_sheet("Result")
    write_header(sheet)
    write_records(sheet, records)
    book.save(filename)


def write_records(sheet, records):
    i = 1
    for record in records:
        format = None
        if record[2] == 'Accepted':
            format = "font: color black"
        else:
            format = "font: color red"
        style = xlwt.easyxf(format)
        sheet.write(i, 0, record[1], style)
        sheet.write(i, 1, record[0], style)
        for j in range(2, 6):
            sheet.write(i, j, record[j], style)
        i += 1


def write_header(sheet):
    format = "font: bold 1 , color black ; borders: top_color black," \
             "bottom_color black, right_color black, left_color black, left medium," \
             "right medium, top medium, bottom medium"
    style = xlwt.easyxf(format)
    column_headers = ["ROLL_NUMBER", "NAME", "STATUS", "TIME", "MEMORY", "ERROR"]
    i = 0
    for header in column_headers:
        sheet.write(0, i, header, style)
        i += 1


# write("record.xls",
#       [["Aniket", 10, "Accepted", "27 s", "3485 kb", "NA"], ["Aniket", 11, "Accepted", "27 s", "3485 kb", "NA"],
#        ["Aniket", 13, "Rejected", "NA", "NA", "Compile time error"]])

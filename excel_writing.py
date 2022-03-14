import scraping
import openpyxl
from openpyxl.worksheet import worksheet
from openpyxl.styles import Font


OUT_XLSX_FILENAME = 'kwork_parsing.xlsx'

def dump_to_xlsx():
    book = openpyxl.load_workbook(filename=OUT_XLSX_FILENAME)
    sheet: worksheet = book.worksheets[0]
    num = 1
    names = scraping.scrap_name()
    fprices = scraping.scrap_first_price()
    sprices = scraping.scrap_second_price()
    details = scraping.scrap_detail()
    
    for name, fprice, sprice, detail in names, fprices, sprices, details:
        sheet.cell(row=num, column=1, value='Название')
        sheet.cell(row=num, column=2, value='Желаемая цена')
        sheet.cell(row=num, column=3, value='Допустимая цена')
        sheet.cell(row=num, column=4, value='Описание')
        num += 1
    book.save(OUT_XLSX_FILENAME)

if __name__ == '__main__':
    dump_to_xlsx()


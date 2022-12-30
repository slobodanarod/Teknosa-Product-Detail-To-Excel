import requests
from bs4 import BeautifulSoup as bs
import xlsxwriter

product_url = "https://www.teknosa.com/lenovo-ideapad-3-82h8020btxbt6-i5-1135g7-156-8-gb-ram-256-gb-ssd-fhd-freedos-tasinabilir-bilgisayar-p-786284230"

def get_teknosa_product_data(product_url):
    page = requests.get(product_url)
    soup = bs(page.content, 'html.parser')
    #product brand and name tag
    product_name_brands = soup.find("h1", {"class": "pdp-title"})
    product_name = product_name_brands.text
    product_brand = product_name_brands.b.text
    # product brand and name tag
    price_area = soup.find("span", {"class": "prc-last"}).text
    product_image = soup.find('img', {'class': "entered"})["data-src"]
    breadcrumbs = soup.findChild('ol', {'class': "breadcrumb"}).find_all('li')
    product_category = breadcrumbs[-1].text
    data_to_excel_row(product_name,product_brand,price_area,product_image, product_category,1)

def data_to_excel_row(name,brand,price,image,category,row):
    workbook = xlsxwriter.Workbook('products.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A' + str(row), name)
    worksheet.write('B' + str(row), brand)
    worksheet.write('C' + str(row), price)
    worksheet.write('D' + str(row), category)
    worksheet.write('E' + str(row), image)
    workbook.close()

get_teknosa_product_data(product_url)

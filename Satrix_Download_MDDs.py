import requests
from requests import status_codes
from requests_html import HTML,HTMLSession
url = 'https://satrix.co.za/products'

s = HTMLSession()
r = s.get(url)
r.html.render(sleep = 1)

a = r.html.find('div.panel-group', first = True)
b = r.html.find('div.panel-group')
# for link in list(a.absolute_links):
#     if 'TabSelection=ETF' in link:
#         print(a.find('h2.vertical-center', first = True).text)
#         print(link)
#         r = s.get(link)
#         print(r.html.find('div.col-sm-12.text-center',first = True).text)
#         pdf_link = list(r.html.find('a.btn.transparent-btn-blue-border.col-xs-12.mdd-icon',first=True).absolute_links)[0]
#         pdf_r = requests.get(pdf_link,stream = True)
#         pdf_id = pdf_link.split('/')[-1]
#         pdf_name = "{}.pdf".format(pdf_id)
#         print(pdf_name)
#         with open(pdf_name,'wb') as f:
#             for chunk in pdf_r.iter_content (1024):
#                 f.write(chunk)
for item in b:
    for link in list(item.absolute_links):
        if 'TabSelection=ETF' in link:
            print(item.find('h2.vertical-center',first = True).text)
            r = s.get(link)
            try:
                pdf_link = list(r.html.find('a.btn.transparent-btn-blue-border.col-xs-12.mdd-icon',first = True).absolute_links)[0]
                pdf_r = requests.get(pdf_link, stream = True)
                name = pdf_link.split('/')[-1]
                pdf_name = "{}.pdf".format(name)
                with open (pdf_name, 'wb') as f:
                    for chunk in pdf_r.iter_content(1024):
                        f.write(chunk)
            except:
                pass          

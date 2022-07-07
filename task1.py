import requests
import xml.etree.ElementTree as ET
response= requests.get("https://coding-academy.pl/all_customers")

dane_xml = ET.fromstring(response.text)

do_pliku=""
for customer in dane_xml:
   do_pliku=do_pliku+customer.text+"\n"
file = open(r"task1_solution.txt", "w")
file.write(do_pliku)
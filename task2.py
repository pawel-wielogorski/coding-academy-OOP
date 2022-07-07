import json
import xml.etree.ElementTree as ET
import requests

f = open(r"input_data.txt", "r")
data = f.read()
table = data.split('\n')
print(len(table))

def json_request(cnumber):   # budujemy z numeru klienta request JSON
    cunbr_={"cunbr":cnumber}
    customer_={"customer":cunbr_}
    customer_request_={"customer_request":customer_}
    return customer_request_

def extract_cunbr_from_json(json):   # kontrolnie pobieramy numer klienta z JSONa zeby sprawdzic czy działa
    return str(json["customer_request"]["customer"]["cunbr"])

def create_web_request(cnumber):
    return "https://coding-academy.pl/customer/"+ extract_cunbr_from_json(json_request(cnumber)) # budujemy z jsona zapytanie do serwisu web

def xml2acc_list(cust_request):   # na podstawie odpwiedzi XML tworzymy liste rachunków
    response = requests.get(create_web_request(cnumber))
    dane_xml = ET.fromstring(response.text)
    acc_list=[]
    for customer in dane_xml:
        for accounts in customer:
            acc_list.append(accounts.text)
    return acc_list

def list2json(cust_number,lista_acc):   # na bazie numeru klienta i listy rachunków z XML budujemy odpowiedź JSON
    cunbr_ = {"cunbr":cust_number,"accounts":lista_acc}
    customer_={"customer":cunbr_}
    customer_response_ = {"customer_response":customer_}
    json_string = json.dumps(customer_response_)
    return json_string
f = open("json_requests.txt", "a")
g = open("json_responses.txt", "a")

for cnumber in table:
    f.write(json.dumps(json_request(cnumber))+"\n") # zapis zapytania JSON
    #print(extract_cunbr_from_json(json_request(cnumber))) # wydruk numeru klienta z zapytania JSON
    #print(create_web_request(cnumber))   # wydruk zapytania do serwisu web
    #print(xml2acc_list(create_web_request(cnumber)))   # wydruk listy rachunków otrzymanej w XML z web serwisu
    g.write(list2json(cnumber,xml2acc_list(create_web_request(cnumber)))+"\n") #  zapis JSONa utworzonego z numeru klienta i listy rachunków

f.close()
g.close()

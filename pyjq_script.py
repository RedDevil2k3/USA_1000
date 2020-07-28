import json
import csv
import pyjq
import os


file_name = 'AlexaUSA1C.json'
top_site_data = open(file_name, 'r')
parsed_data = json.loads(top_site_data.read())
data = pyjq.all('.Ats.Results.Result.Alexa.TopSites.Country.Sites.Site[].DataUrl', parsed_data)
print(data)

with open('USA100.csv', 'w') as filehandle:
    for d in data:
        filehandle.write('%s\n' % d)




file_name = 'AlexaUSA2C.json'
top_site_data = open(file_name, 'r')
parsed_data = json.loads(top_site_data.read())
data = pyjq.all('.Ats.Results.Result.Alexa.TopSites.Country.Sites.Site[].DataUrl', parsed_data)
print(data)

with open('USA200.csv', 'w') as filehandle:
    for d in data:
        filehandle.write('%s\n' % d)




file_name = 'AlexaUSA3C.json'
top_site_data = open(file_name, 'r')
parsed_data = json.loads(top_site_data.read())
data = pyjq.all('.Ats.Results.Result.Alexa.TopSites.Country.Sites.Site[].DataUrl', parsed_data)
print(data)

with open('USA300.csv', 'w') as filehandle:
    for d in data:
        filehandle.write('%s\n' % d)




file_name = 'AlexaUSA4C.json'
top_site_data = open(file_name, 'r')
parsed_data = json.loads(top_site_data.read())
data = pyjq.all('.Ats.Results.Result.Alexa.TopSites.Country.Sites.Site[].DataUrl', parsed_data)
print(data)

with open('USA400.csv', 'w') as filehandle:
    for d in data:
        filehandle.write('%s\n' % d)




file_name = 'AlexaUSA5C.json'
top_site_data = open(file_name, 'r')
parsed_data = json.loads(top_site_data.read())
data = pyjq.all('.Ats.Results.Result.Alexa.TopSites.Country.Sites.Site[].DataUrl', parsed_data)
print(data)

with open('USA500.csv', 'w') as filehandle:
    for d in data:
        filehandle.write('%s\n' % d)





file_name = 'AlexaUSA6C.json'
top_site_data = open(file_name, 'r')
parsed_data = json.loads(top_site_data.read())
data = pyjq.all('.Ats.Results.Result.Alexa.TopSites.Country.Sites.Site[].DataUrl', parsed_data)
print(data)

with open('USA600.csv', 'w') as filehandle:
    for d in data:
        filehandle.write('%s\n' % d)




file_name = 'AlexaUSA7C.json'
top_site_data = open(file_name, 'r')
parsed_data = json.loads(top_site_data.read())
data = pyjq.all('.Ats.Results.Result.Alexa.TopSites.Country.Sites.Site[].DataUrl', parsed_data)
print(data)

with open('USA700.csv', 'w') as filehandle:
    for d in data:
        filehandle.write('%s\n' % d)





file_name = 'AlexaUSA8C.json'
top_site_data = open(file_name, 'r')
parsed_data = json.loads(top_site_data.read())
data = pyjq.all('.Ats.Results.Result.Alexa.TopSites.Country.Sites.Site[].DataUrl', parsed_data)
print(data)

with open('USA800.csv', 'w') as filehandle:
    for d in data:
        filehandle.write('%s\n' % d)




file_name = 'AlexaUSA9C.json'
top_site_data = open(file_name, 'r')
parsed_data = json.loads(top_site_data.read())
data = pyjq.all('.Ats.Results.Result.Alexa.TopSites.Country.Sites.Site[].DataUrl', parsed_data)
print(data)

with open('USA900.csv', 'w') as filehandle:
    for d in data:
        filehandle.write('%s\n' % d)





file_name = 'AlexaUSA1M.json'
top_site_data = open(file_name, 'r')
parsed_data = json.loads(top_site_data.read())
data = pyjq.all('.Ats.Results.Result.Alexa.TopSites.Country.Sites.Site[].DataUrl', parsed_data)
print(data)

with open('USA1000.csv', 'w') as filehandle:
    for d in data:
        filehandle.write('%s\n' % d)

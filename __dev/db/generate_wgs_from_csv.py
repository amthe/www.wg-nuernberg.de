import csv
from jinja2 import Template

wgtemplate = Template('---\nlayout: wg\nwgid: {{ wgid }}\nwgparam: {{ wgparam }}\nwgname: {{ wgname }}\nwggeschoss: {{ wggeschoss }}\nwgqm: {{ wgqm }}\nwgzimmer: {{ wgzimmer }}\nwgterrasse: {{ wgterrasse }}\nwgterrasse_qm: {{ wgterrasse_qm }}\nwgbaeder: {{ wgbaeder }}\nwgfahrrad: {{ wgfahrrad }}\nwgwaschen: {{ wgwaschen }}\nobjektid: {{ objektid }}\nobjektparam: {{ objektparam }}\nobjektstrasse: {{ objektstrasse }}\nobjekthausnummer: {{ objekthausnummer }}\nobjektlatitude: {{ objektlatitude }}\nobjektlongitude: {{ objektlongitude }}\npermalink: /{{ wgparam }}/  \n---\n{{ body }}')
with open('wg.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV, None)  # skip the headers
    for row in readCSV:
        content = wgtemplate.render(wgid=row[0],wgparam=row[1],wgname=row[2],wggeschoss=row[3],wgqm=row[4],wgzimmer=row[5],wgterrasse=row[6],wgterrasse_qm=row[7],wgbaeder=row[8],wgfahrrad=row[9],wgwaschen=row[10],objektid=row[11],objektparam=row[12],objektstrasse=row[13],objekthausnummer=row[14],objektlatitude=row[15],objektlongitude=row[16],body=row[17])
        print (content)
        with open(row[1] + '.md', 'w') as file:
            file.write(content)

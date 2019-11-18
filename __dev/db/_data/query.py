import csv
from jinja2 import Template

template = Template('---\nzimmerid: {{ zimmerid }}\nzimmerparam: {{ zimmerparam }}\nzimmerqm: {{ zimmerqm }}\nzimmerabstellraum: {{ zimmerabstellraum }}\nzimmertyp: {{ zimmertyp }}\nzimmerschraege: {{ zimmerschraege }}\nzimmerausrichtung: {{ zimmerausrichtung }}\nzimmerfenster: {{ zimmerfenster }}\nzimmerlautstaerke: {{ zimmerlautstaerke }}\nwgid: {{ wgid }}\nwgparam: {{ wgparam }}\nwgname: {{ wgname }}\nwggeschoss: {{ wggeschoss }}\nwgqm: {{ wgqm }}\nwgzimmer: {{ wgzimmer }}\nwgterrasse: {{ wgterrasse }}\nwgterrasse_qm: {{ wgterrasse_qm }}\nwgbaeder: {{ wgbaeder }}\nwgfahrrad: {{ wgfahrrad }}\nwgwaschen: {{ wgwaschen }}\nobjektid: {{ objektid }}\nobjektparam: {{ objektparam }}\nobjektstrasse: {{ objektstrasse }}\nobjekthausnummer: {{ objekthausnummer }}\nobjektlatitude: {{ objektlatitude }}\nobjektlongitude: {{ objektlongitude }}\npermalink: /{{ wgparam }}/{{ zimmerparam }}  \n---\n{{ body }}')
with open('query.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        content = template.render(zimmerid=row[0],zimmerparam=row[1],zimmerqm=row[2],zimmerabstellraum=row[3],zimmertyp=row[4],zimmerschraege=row[5],zimmerausrichtung=row[6],zimmerfenster=row[7],zimmerlautstaerke=row[8],wgid=row[9],wgparam=row[10],wgname=row[11],wggeschoss=row[12],wgqm=row[13],wgzimmer=row[14],wgterrasse=row[15],wgterrasse_qm=row[16],wgbaeder=row[17],wgfahrrad=row[18],wgwaschen=row[19],objektid=row[20],objektparam=row[21],objektstrasse=row[22],objekthausnummer=row[23],objektlatitude=row[24],objektlongitude=row[25],body=row[26])
        print (content)
        with open(row[1] + '.md', 'w') as file:
            file.write(content)

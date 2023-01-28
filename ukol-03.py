import json

#ukol-03

with open("body.json", encoding="UTF-8") as soubor:
    data = soubor.read()
body = (json.loads(data))

prospech = {}

for student in body:
    if body[student] >= 60:
        prospech[student] = "Pass"
    else:
        prospech[student] = "Fail"

with open("prospech.json", mode="w", encoding="UTF-8") as soubor_prospech:
    #soubor_prospech.write(json.dumps(prospech))
    json.dump(prospech, soubor_prospech)

#bonus

with open("bonusy.json", encoding="UTF-8") as soubor_bonusy:
    data_bonusy = soubor_bonusy.read()
body_bonusy = (json.loads(data_bonusy))

body_celkem = {}

for student in body:
    if student in body_bonusy:
        body_celkem[student] = body[student] + body_bonusy[student]
    else:
        body_celkem[student] = body[student]

znamky = {}

for student in body_celkem:
    if body_celkem[student] >= 90:
        znamky[student] = 1
    elif body_celkem[student] >= 70:
        znamky[student] = 2
    elif body_celkem[student] >= 50:
        znamky[student] = 3
    elif body_celkem[student] >= 30:
        znamky[student] = 4
    else:
        znamky[student] = 5

with open("znamky.json", mode="w", encoding="UTF-8") as soubor_znamky:
    #soubor_znamky.write(json.dumps(znamky))
    json.dump(znamky, soubor_znamky)
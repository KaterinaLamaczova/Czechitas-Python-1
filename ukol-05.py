#ukol-05

#teploty: ráno, poledne, večer, noc

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

# 1. Seznam průměrných teplot pro každý den

prumer_teplot = [sum(teplota)/len(teplota) for teplota in teploty]
print(prumer_teplot)

# 2. Seznam ranních teplot

ranni_teploty = [teplota[0] for teplota in teploty]
print(ranni_teploty)

# 3. Seznam nočních teplot

nocni_teploty = [teplota[3] for teplota in teploty]
print(nocni_teploty)

# 4. Seznam seznamů s polední a noční teplotou

poledne_noc = [[teplota[1], teplota[3]] for teplota in teploty]
print(poledne_noc)

# Bonus

teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]

prumerna_teplota = {teplota[0]: sum(teplota[1:])/(len(teplota)-1) for teplota in teploty}
print(prumerna_teplota)
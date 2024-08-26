# pythonl

Wat als je alleen maar Nederlandse woorden zou gebruiken voor python sleutel woorden?

Hier is mijn idee daar van:

- and: en
- as: als
- assert: eis
- async: async
- await: wachtop
- break: stop
- case: geval
- class: klasse
- continue: opnieuw
- def: def
- del: verwijder
- if: indien
- elif: andien 
- else: anders
- except: behalve
- False: Onwaar 
- finally: uiteindelijk
- for: voor
- from: van
- global: globaal
- import: importeer
- in: in
- is: is
- lambda: lambda
- match: vergelijk
- None: Niets
- nonlocal: nietlokaal
- not: niet
- or: of
- pass: pas
- raise: hef
- return: terug
- True: Waar
- try: probeer
- type: type
- while: zolang
- with: met
- yield: lever

## Voorbeeld

```pythonl
def lees_nummers(bestand_naam):
    nummers = []
    met open(bestand_naam) als bestand:
        voor lijn in bestand:
            probeer:
                nummers.append(int(lijn))
            behalve:
                opnieuw
    terug nummers

nummers = lees_nummers("nummers.txt")
print(nummers)
```

En je kan dit nog echt uitvoeren ook!

```shell
./pythonl voorbeeld.pynl
```


## Afhankelijkheden

Vergeet niet om de afhankelijkheden in `requirements.txt` te installeren. 
Dat is op dit moment alleen maar [token_utils](https://pypi.org/project/token-utils/).

```bash
pip install -r requirements.txt
```

## Interactie met Python code

Pythonl code in .pynl bestanden werkt naadloos samen met Python in .py bestanden. 
Je kan .py bestanden gewoon importeren in je .pynl bestanden. Zie [hoofd.pynl](./hoofd.pynl):

```pythonl
importeer fiben
importeer fibnl

print("Fibonacci(7) uit Engelse module:", fiben.fibonacci(7))
print("Fibonacci(7) uit Nederlandse module:", fibnl.fibonacci(7))

eis fiben.fibonacci(7) == fibnl.fibonacci(7)
```

Als je dit uitvoert met pythonl krijg je:

```shell
$ pythonl ./hoofd.pynl
# Fibonacci(7) uit Engelse module: 13
# Fibonacci(7) uit Nederlandse module: 13
```

# Zelfstart (Boodstrap) Pythonl 🐍

```shell
$ ./pythonl ./pythonl.pynl ./hoofd.pynl
Fibonacci(7) uit Engelse module: 13
Fibonacci(7) uit Nederlandse module: 13
```

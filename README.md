# pythonl

Wat als je alleen maar Nederlandse woorden zou gebruiken voor python sleutel woorden?

Hier is mijn idee daar van:

- and : en
- as : zoals
- assert : eis
- break : stop
- class : klasse
- continue: opnieuw
- def: def
- del: verwijder
- elif: andien 
- else: anders
- except: behalve
- False: Onwaar 
- finally: uiteindelijk
- for: voor
- from: van
- global: globaal
- if: indien
- import: importeer
- in: in
- is: is
- lambda: labda
- None: Niets
- nonlocal: nietlokaal
- not: niet
- or: of
- pass: pas
- raise: verhoog
- return: terug
- True: Waar
- try: probeer
- while: zolang
- with: met
- yield: lever

```python
def(a):
  indien a:
    print(a)
  anders:
    print("Niet a")
```

En je kan dit nog echt uitvoeren ook!

# Afhankelijkheden

Vergeet niet om de afhankelijkheden in `requirements.txt` te installeren. 
Dat is op dit moment alleen maar [token_utils](https://pypi.org/project/token-utils/).

```bash
pip install -r requirements.txt
```

## Uitvoeren

```bash
$ pythonl ./hoofd.pynl
# Fibonacci(7) uit Engelse module: 13
# Fibonacci(7) uit Nederlandse module: 13
```

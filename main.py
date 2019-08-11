import os, sys, json, re, mendeleev as mdv

path = os.path.join(sys.path[0], 'config.json')
config = json.load(open(path, 'r'))

def score(item):
    return config['elements'][str(item[0])] + config['elements'][str(item[1])], item

def arrange(item):
    return (max(item), min(item))

def formatting(e1, e2):
    e1, e2 = mdv.element(e1), mdv.element(e2)
    return '\t[{} {}] + [{} {}]'.format(e1.symbol if not config['fullPrint'] else e1.name,
                                        e1.atomic_number,
                                        e2.symbol if not config['fullPrint'] else e2.name,
                                        e2.atomic_number)

def getElement(element):
    if re.match(r'\d+', element):
        return mdv.element(int(element))
    elif re.match(r'\w{1,2}', element):
        try:
            return mdv.element(element.strip().title())
        except:
            raise ValueError('Unknown Element \'{}\''.format(element))
    else:
        raise ValueError('Unknown Element Format \'{}\''.format(element))

def bestSelection(select):
    select = select.atomic_number
    posi = [(x, select - x) for x in range(1, select)]
    posi = list(map(arrange, posi))
    posi = list(set(posi))
    posi = list(filter(lambda item : score(item)[0] >= config['minimumScore'], posi))
    posi.sort(key=lambda item : score(item), reverse=not config['reverseSorting'])

    string1 = '[Best Elements for Element {}, {}]'.format(select, mdv.element(select).name)
    string2 = '\n'.join([formatting(element1, element2) for element1, element2 in posi])
    return string1, string2 or '\t{No elements matched the configuration specified}'

selection = input("Choose elements, delimited by whitespace and/or punctuation...\n")
selection = [getElement(e) for e in selection.split()]
print('\n\n'.join(
    sorted(['{}\n{}'.format(*bestSelection(E)) for E in selection], key=lambda string : len(string.split('\n')))
))
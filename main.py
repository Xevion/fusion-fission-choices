import os, sys, json, re, mendeleev as mdv

path = os.path.join(sys.path[0], 'config.json')
config = json.load(open(path, 'r'))

def score(element):
    return config['elements'][str(element)]

def scoreSum(item):
    return (score(item[0]) + score(item[1])), item

def formatting(e1, e2):
    e1, e2 = mdv.element(e1), mdv.element(e2)
    return '\t[{} {}] + [{} {}]'.format(e1.symbol if not config['fullPrint'] else e1.name,
                                        e1.atomic_number,
                                        e2.symbol if not config['fullPrint'] else e2.name,
                                        e2.atomic_number)

def hasNegatives(item):
    return score(item[0]) < 0 or score(item[1]) < 0

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
    # Create a set, rearrange by (larger, smaller), then remove duplicates
    posi = [(x, select - x) for x in range(1, select)]
    posi = list(map(lambda item : (max(item), min(item)), posi))
    posi = list(dict.fromkeys(posi))
    # Filter out element tuples that don't have both with scores
    if config['noNegatives']:
        posi = list(filter(lambda item : hasNegatives(item), posi))
    # Filter out elements that do not meet the minimum set
    posi = list(filter(lambda item : scoreSum(item)[0] >= config['minimumScore'], posi))
    # Sort the elements by the sum of their scores
    posi.sort(key=lambda item : scoreSum(item), reverse=not config['reverseSorting'])

    string1 = '[Best Elements for Element {}, {}]'.format(select, mdv.element(select).name)
    string2 = '\n'.join([formatting(element1, element2) for element1, element2 in posi])
    return string1, string2 or '\t{No elements matched the configuration specified}'

selection = input("Choose elements, delimited by whitespace and/or punctuation...\n")
selection = [getElement(e) for e in selection.split()]
print('\n\n'.join(
    sorted(['{}\n{}'.format(*bestSelection(E)) for E in selection], key=lambda string : len(string.split('\n')))
))
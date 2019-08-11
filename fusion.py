import os, sys, json, re, mendeleev as mdv

# Configuration reading
path = os.path.join(sys.path[0], 'config.json')
config = json.load(open(path, 'r'))

# Constants
noElements = '\t{No elements matched the configuration specified}'

# Lambdas
score = lambda element : config['elements'][str(element)]
scoreSum = lambda item : ((score(item[0]) + score(item[1])), item)
hasNegatives = lambda item : score(item[0]) < 0 or score(item[1]) < 0

# Formatting for a single element report line
def formatting(e1, e2):
    e1, e2 = mdv.element(e1), mdv.element(e2)
    return '\t[{} {}] + [{} {}]'.format(e1.symbol if not config['fullPrint'] else e1.name,
                                        e1.atomic_number,
                                        e2.symbol if not config['fullPrint'] else e2.name,
                                        e2.atomic_number)

# get the element based on two letters or a digit and attempt to map it to a number
def getElement(element):
    if re.match(r'\d+', element):
        element = int(element)
        if element >= 1 and element <= 118:
            return mdv.element(element)
        raise ValueError(f'Unknown Element Atomic Number \'{element}\'')
    elif re.match(r'\w{1,2}', element):
        try:
            return mdv.element(element.strip().title())
        except:
            raise ValueError(f'Unknown Element \'{element}\'')
    else:
        raise ValueError(f'Unknown Element Format \'{element}\'')

def bestSelection(select):
    select = select.atomic_number
    # Create a set, rearrange by (larger, smaller), then remove duplicates
    posi = [(x, select - x) for x in range(1, select)]
    posi = list(map(lambda item : (max(item), min(item)), posi))
    posi = list(dict.fromkeys(posi))
    # Filter out element tuples that don't have both with scores
    if config['noNegatives']:
        posi = list(filter(lambda item : hasNegatives(item), posi))
    # Filter out elements that do not meet the minimum/maximum set
    posi = list(filter(lambda item : scoreSum(item)[0] >= config['minimumScore'], posi))
    # Sort the elements by the sum of their scores
    posi.sort(key=lambda item : scoreSum(item), reverse=not config['reverseInnerOrder'])
    # Build the strings
    string1 = '[Best Elements for Element {}, {}]'.format(select, mdv.element(select).name if config['fullPrint'] else mdv.element(select.symbol))
    string2 = '\n'.join([formatting(element1, element2) for element1, element2 in posi])
    return string1, string2 or noElements

# Driver code
def main():
    selection = input("Choose elements, delimited by whitespace and/or punctuation...\n")
    selection = [getElement(e) for e in selection.split()]
    # No one:
    # No one at all:
    # Me:
    print('\n\n'.join(
        map(
            lambda item : '{}\n{}'.format(item[0], item[1]),
            filter(
                lambda item : (item[1] != noElements) if config['eliminateEmpty'] else True,
                sorted([bestSelection(E) for E in selection],
                # hacky solution for reverseOrder config option
                key=lambda item : len(item[1]) if item[1] != noElements else 0,
                reverse=not config['reverseOrder'])
            )
        )
    ))
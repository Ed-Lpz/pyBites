import re

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'aly pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names=NAMES):
    new_names = []
    [new_names.append(name.title()) for name in names if name.title() not in new_names]
    return new_names

def sort_by_surname_desc(names=NAMES):
    """Returns names list sorted desc by surname"""
    pattern = re.compile(r'(^\w+)(\s?)(\w+$)')
    last_first = [pattern.sub(r'\3\2\1', name.title()) for name in dedup_and_title_case_names(names)]
    last_first.sort(reverse=True)
    org_names = [pattern.sub(r'\3\2\1', name.title()) for name in last_first]
    return org_names



def shortest_first_name(names):
    names = dedup_and_title_case_names(names)
    first = [name.split()[0] for name in names]
    first.sort(key=len)
    return first[0]

  
print(sort_by_surname_desc(NAMES))
print(shortest_first_name(NAMES))
NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    temp = set(names)
    return [s.title() for s in temp]


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return sorted(sorted(names), key=lambda s: s.split()[1], reverse=True)


def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    names.sort(key=lambda s: (len(s.split()[0]), s))
    return names[0].split()[0]


print(*dedup_and_title_case_names(NAMES), sep="\n")
print("<------------------------------>")
print(*sort_by_surname_desc(NAMES), sep="\n")
print("<------------------------------>")
print(shortest_first_name(NAMES), sep="\n")

def test_dedup_and_title_case_names():
    names = dedup_and_title_case_names(NAMES)
    assert names.count('Bob Belderbos') == 1
    assert names.count('julian sequeira') == 0
    assert names.count('Brad Pitt') == 1
    assert len(names) == 10
    assert all(n.title() in names for n in NAMES)


def test_sort_by_surname_desc():
    names = sort_by_surname_desc(NAMES)
    assert names[0] == 'Julian Sequeira'
    assert names[-1] == 'Alec Baldwin'


def test_shortest_first_name():
    assert shortest_first_name(NAMES) == 'Al'


test_dedup_and_title_case_names()
test_sort_by_surname_desc()
test_shortest_first_name()
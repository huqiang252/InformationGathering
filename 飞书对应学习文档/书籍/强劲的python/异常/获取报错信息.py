# 稀有气体的原子序数
nobles = {'He': 2, 'Ne': 10, 'Ar': 18, 'Kr': 36, 'Xe': 54}

def show_element_info(elements):
    for element in elements:
        print('Atomic number of {} is {}'.format(
            element, nobles[element]))

try:
    show_element_info(['Ne', 'Ar', 'Br'])
except KeyError as err:
    missing_element = err.args[0]
    print(f"Missing data for element: {missing_element}")




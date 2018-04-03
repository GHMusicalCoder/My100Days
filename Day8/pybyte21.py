cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma separated string of jeep models (original order)"""
    return ', '.join(cars.get('Jeep'))


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    return [values[0] for key, values in cars.items()]


def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    grep = grep.lower()
    match = []
    for key in cars.keys():
        for value in cars[key]:
            if grep in value.lower():
                match.append(value)
    return sorted(match, key=lambda x: x)


def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    for key in cars.keys():
        cars[key] = sorted(cars[key], key=lambda x: x)


print(get_all_jeeps())
print('-' * 60)
print(get_first_model_each_manufacturer())
print('-' * 60)
print(get_all_matching_models())
print(get_all_matching_models('CO'))
print('-' * 60)

sort_car_models()
for key, values in cars.items():
    print('{0}: {1}'.format(key, values))
cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': [ 'Grand Cherokee','Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    print(', '.join(cars['Jeep']))
    return ', '.join(cars['Jeep'])
   

def get_first_model_each_manufacturer(cars=cars):
    results = []
    for man in cars.values():
        results.append(str(man[0]))
    print(results)
    return results


def get_all_matching_models(cars=cars, grep='Trail'):
    trail_list = []
    for values in cars.values():
        for model in values:
            if ( str(grep).lower() in str(model).lower() ):
                trail_list.append(model)
    trail_list.sort()
    print(trail_list)
    return trail_list
          

def sort_car_models(cars=cars):
    for models in cars.values():
        models.sort()
    print(cars)
    return (cars)


get_all_jeeps()
get_first_model_each_manufacturer()
get_all_matching_models( grep='CO')

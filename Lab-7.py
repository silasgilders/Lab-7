#|-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-|
#       				       BEHOLD, THE HEADER.
# Description:
#
# Usage: python Lab-7.py
#
# Parameters: N/A
#
#|-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-|
  
def main():
    
    person_info = {
        'name': 'Silas Gilders',
        'student_id': '1026511',
        'pizza_toppings' : [
            'Pepperoni',
            'Sausage',
            'Onions',],

        'movies' :[ {
        
            'title' : [ "Lord of the Rings", "Pacific Rim", "Pulp Fiction",],
            'genre' : 'Action',
            }
        ]
        

    }
    print_person_info(person_info)


def print_person_info(person_info):
    
    sentence = "Hello, my name is " + person_info['name'] + ", " + "my student number is " + person_info['student_id']
    sentence2 = "My ideal pizza has "

    for topping in person_info['pizza_toppings']:
        sentence2 += str(topping['pizza_toppings'])
    #for i in enumerate(person_info['pizza_toppings']):
        #if i < len(str(person_info['pizza_toppings'])):
            #sentence2 += ', '
        #else:
            #sentence2 += '.'

    print(sentence, "\n", sentence2)






main()
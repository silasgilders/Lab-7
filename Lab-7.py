#|-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-|
#       				       BEHOLD, THE HEADER.
# Description: Prints information from a Data Structure into a preset 
#                  group of sentences
#
#
# Usage: python Lab-7.py
#
#
# Parameters: N/A
#
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
    
    sentence = "Hello, my name is " + person_info['name'] + ", " + "my student number is " + person_info['student_id'] + "."
    sentence2 = "My ideal pizza has "
    sentence3 = "I like to watch "
    sentence4 = "Some of my favourite movies are "



    for topping in person_info['pizza_toppings']:
        sentence2 += topping + ", "
   
    for genre in person_info['movies']:
        sentence3 += genre['genre'] + " movies."
    
    for movie in person_info['movies'][0]['title']:
        sentence4 += movie + ", "
    

    print(sentence, "\n", sentence2, '\n', sentence3, '\n', sentence4)






main()
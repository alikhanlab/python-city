def draw_park(num_trees = 10, num_people = 10):
    """
    The function prints symbolic trees and people.
    It takes as parameters: 'num_trees' - number of trees to print.
                            'num_people' - number of people to print.
    Returns None.
    """
    if num_trees < 0:
        raise ValueError('Number of trees can not be negative')
    for _ in range(num_trees):
        print('~\|/~')
        
    if num_people < 0:
        raise ValueError('Number of people can not be negative')
    for _ in range(num_people):
            print('-_-')
            print('<|>')
            print("/ \ ")        
    return

def create_dictionary(filename):
    """Return a dictionary with the letter of the alphabet as the key and the name of the flower as the value for each row in flower.txt."""
    
    dict_flowers = {}
    
    with open(filename) as flowers:
        for line in flowers:
            letter, flower = line.strip().split(': ')
            dict_flowers[letter] = flower
            
    return dict_flowers

def get_user_identity():
    """Return the full name of the user in the title style."""
    
    full_name = input('Enter your First [space] Last name only: ')
    return full_name.title()

def main():
    dict_flowers = create_dictionary('flowers.txt')
    first_name = get_user_identity().split()[0]

    print('Unique flower name with the first letter: {}'.format(dict_flowers.get(first_name[0])))

if __name__ == '__main__':
    main()

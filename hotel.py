hotel = {
     '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
         }
    },
    '105': {},
}

def is_vacant(hotel,room):
    if 'guest' in hotel[room]:
        print("The room is not vacant.")
        return False
    else:
        print("The room is vacant.")
        return True

is_vacant(hotel, '101')

print('\n')

new_guest = 'Issa Rae'
def check_in(room, guest_dictionary):
    if is_vacant(hotel, room) == True:
        hotel[room] = guest_dictionary
        print(f'{guest_dictionary} is checked into room number {room}.')
    else:
        print('The room is not available.')
        return False
check_in('102', new_guest)

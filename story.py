FIRSTKEY = 'first'
scenes = {FIRSTKEY : ('here is the main story', 
                      'mooky.png',  
                      ('a.', 'b.', 'c.', 'd.') )
         }

def draw_message():

    print('bob')

    story1 = ('elirocks', 'eli is awesome', 'ei is so cool')

    print(story1[0])
    print(story1[1])
    print(story1[2])

    dictionary = {'eli' : 555, 'story' : story1}
    print(dictionary['eli'])
    print(dictionary['story'][1])

def get_first_scene():

    return scenes[FIRSTKEY]

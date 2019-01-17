SCENE1 = 'scene1'
SCENE2 = 'scene2'

scenes = {SCENE1 : ('here is the main story', 
                      'mooky.png',  
                      (('a.', SCENE2), ('b.', SCENE2))), 
          SCENE2 : ('here is the second scene', 
                      'mooky.png',
                      (('a.', SCENE1), ('b.', SCENE1)) )
         }


def get_first_scene():

    return scenes[SCENE1]

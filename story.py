SCENE1 = 'scene1'
SCENE2 = 'scene2'
SCENE3 = 'scene3'

scenes = {SCENE1 : ("Mooky is bored. Then he has an idea! He will go skiing. He grabs his ski stuff and drives to the nearest ski place, Mooker Woods. He starts to put his ski stuff on. He goes to get his skis, But he can't find them. Oh No! Where are his skis? What should he do?",
                      'mooky.png',  
                      (('a. Go search for skis', SCENE2), ('b. Go buy skis', SCENE3))), 
          SCENE2 : ('here is the second scene', 
                      'mooky.png',
                      (('a.', SCENE1), ('b.', SCENE1)) )
         }


def get_first_scene():

    return scenes[SCENE1]

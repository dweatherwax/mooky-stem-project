SCENE1 = 'scene1'
SCENE2 = 'scene2'
SCENE3 = 'scene3'
SCENE4 = 'scene4'
SCENE5 = 'scene5'
SCENE6 = 'scene6'
SCENE7 = 'scene7'
SCENE8 = 'scene8'
SCENE9 = 'scene9'

scenes = {SCENE1 : ("Mooky is bored. Then he has an idea! He will go skiing. He grabs his ski stuff and drives to the nearest ski place, Mooker Woods. He starts to put his ski stuff on. He goes to get his skis, But he can't find them. Oh No! Where are his skis? What should he do?",
                      'images/mooky-stem-2.jpg',  
                      (('a. Go search for skis', SCENE2), ('b. Go buy skis', SCENE3))), 
          SCENE2 : ('Mooky decides to search for his skis. Where should he start searching?', 
                      'images/mooky-stem-1.jpg',
                      (('a. The mountain', SCENE4), ('b. The base lodge', SCENE5)) ), 
          SCENE3 : (' Mooky walks into the ski and snowboard shop. He looks around. He sees the ski section. Oh No! The skis have sold out! Mooky decides to search for his skis. Where should he start searching?', 
                      'images/sad-mookey-stem.jpg',
                      (('a. The mountain', SCENE4), ('b. The base lodge', SCENE5)) ), 
          SCENE4 : (' Mooky looked down the slope. Skiers and snow boarders rushed past him. Suddenly he spotted a pair of skis just like his! " Hey!" he shouted. The skier turned his head. When he noticed Mooky he froze, then took off. " Hey" shouted Mooky again as he chased the skier down a side trail. The skier disappeared as he turned a corner. Mooky skidded around the corner and came to a halt. The trail split into two paths. Which should he take?', 
                      'images/mooky-stem-5.jpg',
                      (('a. The left path', SCENE6), ('b. The right path', SCENE7)) ), 
          SCENE5 : ('Mooky entered the base lodge and looked around. It was crowded. Mooky started checking under tables and peeking in cubbies. He asked a passing mooky. " Have you seen a pair of red skis?" " No, sorry." he replied. Mooky sat down frustrated. He sighed. Where should he search next?', 
                      'images/mooky-stem-4.jpg',
                      (('a. The mountain', SCENE4), ('b. The forest', SCENE8)) ), 
          SCENE6 : (' Mooky runs down the left path. He feels like he ran a mile before reaching a dead end. Exhausted from his run, Mooky collapses into the snow. What should he do now?', 
                      'images/mooky-stem-7.jpg',
                      (('a. Give up', SCENE9), ('b. Go back', SCENE4)) ), 
          SCENE7 : (' Mooky barrels down the right path. As he turns a corner the skier with his skis comes into view. Mooky takes a flying leap and tackles him to the ground. He accidently knocks off the skiers helmet revealing his face. " Ducky!?" cries Mooky. Ducky smiles guiltily. " Do not dare smile!" shouts Mooky angrily. " spent a lot of time looking for those skis!" Ducky looks scared. Mooky tries to control his anger. " Why did you steal my skis?" Mooky asks. " Well," says Ducky." My mother saw on TV a horrific accident that happened to a skier, So she does not let me ski now. But I like skiing, So I stole your skis so I could ski." " Okay." said Mooky as he clambered off Ducky. " But I need my skis back. Maybe you could talk to your mom about it. She might understand." " Okay," answered Ducky as he hande Mooky his skis. " Thank You!" Mooky called as he skied away, excited for a fun day of skiing. The End.', 
                      'images/mooky-stem-6.jpg',
                      (('a. Play Again', SCENE1), ) ), 
          SCENE8 : (' The snow crunched under Mookys feet as he trudged through the forest looking left and right. As far as he could tell, no one was there but him. He had only one more place to look, the mountain.', 
                      'images/mooky-stem-3.jpg',
                      (('a. The mountain', SCENE4), ) ), 
          SCENE9 : (' Mooky dragged his feet as he trudged into the base lodge. He sighed, gathered up his stuff, and drove home. He would never see those red skis again.', 
                      'images/sad-mookey-stem.jpg',
                      (('a. Restart', SCENE1), ) )
         }


def get_first_scene():

    return scenes[SCENE1]

def get_scene(scene):

    return scenes[scene]

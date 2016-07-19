# coding: utf-8
# 导入必要的模块

from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)
        
# 第一个场景 Death
class Death(Scene):

    quips = [
        "you died. You kinda suck at this.",
        "Your mom would be pround...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
	]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)
        
# 剩下的游戏场景
class CentralCorridor(Scene):

    def enter(self):
        print """
The Gothons of Planet Percal #25 have invaded your ship and destroyed\nyour entire crew. You are the last surviving member and your last\nmission is to get the neutron destruct bomb from the Weapon Armory,\nput it in the bridge, and blow the ship up after getting into an\nescape pod.\n\nYou're runing down the cnetral corridor to the Weapon Armory when\na Gothon jumps out, red scaly skin , dark grimy teeth, and evil clown costume\nArmory and about to pull a weapon to blast you.
        """     
        action = raw_input("> ")
        if action == 'shoot!':
            print """Quick on the draw you yank out your blaster and fire it at the Gothon\nHis clown costume is flowing and moving around his body, which throws\noff your aim. Yout laser hits his costume but misses him entirely.\nThis completely ruins his brand new costume his mother bought him whihc\nmakes him fly into an insane rage and blast you repeatedly in the face until\nyou are deat. Then he eats you.
            """
            return 'death'

        elif action == "dodge!":
            print """Like a world class boxer you dodge, weave, slip and slide right\nas the Gothon's blaster cranks a laser past yout head.\nIn the middle of your artful dodge your foot slips and you\nbang your head on the metal wall and pass out.\nYou wake up shourly after only to die as the Gothon stomps on\nyour head and eats you.
            """
            return 'death'

        elif action == "tell a joke":
            print """Lucky for you they made you learn Gothon insults in the academy.\nYou tell the one Gothon joke you know:\nLbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.\nWhile he's laughing you run up and shoot him square in the head\nputting him down, then jump though the Weapon Armory door.
            """
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'
            
class LaserWeaponArmory(Scene):

    def enter(self):
        print """You do a dive roll into the Weapon Armory, crouch and scan the room\nfor more Gothons that might be hiding. It's dead quite, too quiet.\nYou stand up and run to the far side of the room and find the\nneutron bomb in its container. There's a keypad lock on the bpx\nand you need the code to get the bomb out. If you get the code\nwrong 10 times then the lock closes forever and you can't\nget the bomb. The code is 3 digits.
        """
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        print "The time of three numbers is: %d" % (int(code[0]) * int(code[1]) * int(code[2]))
        print "The sum of three numbers is %d" % (int(code[0]) + int(code[1]) + int(code[2]))
        	
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
        	print "BZZZZEDDD!"
        	guesses += 1
        	guess = raw_input("[keybad]> ")

        if guess == code:
            print """The container clicks open and the seal breaks, letting gas out.\nYou grab the neutron bomb and run as fast as you can to the\nbridge where you must place it in the right spot.
            """
            return 'the_bridge'
        else: 
            print """The lock buzzes one last time and then you hear a sickening\nmelting sound as the mechanism is fused together.\nYou decide to sit there, and finally the Gothons blow up the\nship from their ship and you die.
            """
            return 'death'
            
class TheBridge(Scene):

    def enter(Self):
        print """You burst onto the Bridge with the netron destruct bomb\nunder your arm and surprise 5 Gothons who are trying to\ntake control of the ship. Each of them has an even uglier\nclown costume than the last. They haven't pulled their\nweapons out yet, as they see the active bomb under your\n"arm and don't want to set it off.
        """

        action = raw_input("> ")

        if action == "throw the bomb":
            print """In a panic you throw the bomb at the group of Gothons\nand make a leap for the door. Right as you drop it a\nGothon shoots you right in the back killing you.\nAs you died you see another Gothon frantically try to disarm\nthe bomb. You die knowing they will probably blow up when\nit goes off.
            """
            return 'death'

        elif action == "slowly place the bomb":
            print """You point your blaster at the bomb under your arm\nand the Gothons put their hands up and start to sweat.\nYou inch backward to the door, open it, and then carefully\nplace the bomb on the floor, pointing your blaster at it.\nYou then jump back through the door, punch the close button\nand blast the lock so the Gothons can't get out.\nNow that the bomb is placed you run to the escape pod to\nget off this tin can.
            """
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"
            
class EscapePod(Scene):

    def enter(self):
        print """You rush through the ship desperately trying to make it to\nthe escape pod before the whole ship explodes. It seems like\nhardly any Gothons are on the ship, so your run is clear of\ninterference. You get to the chamber with the escape pod, and\nnow need to pick one to take. Some of them could be damaged\nbut you don't have time to look. There's 5 pods, which one\ndo you take?
        """

        good_pod = randint(1,5)
        print "the squire the of number is: %d" % (int(good_pod)**2)
        guess = raw_input("[pod #]>")

        if int(guess) != good_pod:
            print """You jump into pod %s and hit the eject button.\nThe pod escapes out into the void of space, then\nimplodes as the hull reptures, crushing your body\ninto jam jelly.
            """ % guess
            return 'death'

        else:
            print """Your jump into pod %s and hit the eject button.\nThe pod easily slides out into space heading to\nthe planet below. As it flies to the planet, you look\nback and see your ship implode then explode like a\nbright star, taking out the Gothon ship at the same\ntime. You WON!
            """ % guess

        return 'finished'
        
class Finished(Scene):

    def enter(self):
        print "You Won! Good Job."
        return 'finished'
        
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()        
        
# map 类，把所有场景存在字典中。这个字典叫做 Map.scene。这个字典包含所有需要的场景
class Map(object):

    scene = {'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scene.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
# 调用 play，把 Map 交给 Engine，运行游戏
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
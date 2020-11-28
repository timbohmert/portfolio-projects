#import the tree class

from tree import TreeNode

#mission provided by Codecademy







######
# VARIABLES FOR WILDERNESS ESCAPE STORY
######


#Wilderness story_root that describes the start of the story
story_root = TreeNode("""
Once upon a time...

You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you:
1) Roar back!
2) Run to the left...
""")


#choice_a for the story_root
choice_a = TreeNode("""
The bear is startled and runs away.
Do you:
1) Shout 'Sorry bear!'
2) Yell 'Hooray!'
""")


#choice_b for story_root
choice_b = TreeNode("""
You come across a clearing full of flowers.
The bear follows you and asks 'what gives?'
Do you:
1) Gasp 'A talking bear!'
2) Explain that the bear scared you.
""")


#adding choice_a and choice_b to story_root
story_root.add_child(choice_a)

story_root.add_child(choice_b)


#choice_a_1 for choice_a
choice_a_1 = TreeNode("""
The bear returns and tells you it's been a rough week. 
After making peace with a talking bear he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS!!!
""")


#choice_a_2 for choice_a
choice_a_2 = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone in the wilderness.

YOU REMAIN LOST IN THE WILDERNESS!!!
""")


#adding choice_a_1 and choice_a_2 to choice_a
choice_a.add_child(choice_a_1)

choice_a.add_child(choice_a_2)


#choice_b_1 for choice_b
choice_b_1 = TreeNode("""
The bear is unamused.
After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST IN THE WILDERNSS!!!
""")


#choice_b_2 for choice_b
choice_b_2 = TreeNode("""
The bear understands and apologizes for startling you.
Your new friend shows you a path leafing out of the forest.

YOU HAVE ESCAPED THE WILDERNESS!!!
""")


#adding choice_b_1 and choice_b_2 to choice_b
choice_b.add_child(choice_b_1)

choice_b.add_child(choice_b_2)


######
# TESTING AREA
######

#story_root.traverse()



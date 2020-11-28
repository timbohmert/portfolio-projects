######
# TREENODE CLASS
######


#treenode class that will keep track of portion of the story and choices user can make to progress story
class TreeNode:

    #constructor for declaring story_piece that will be placed into each node and empty list of choices
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []


    #method to add additional nodes to the story
    def add_child(self, node):
        self.choices.append(node)


    #method for traversing the tree
    def traverse(self):
        story_node = self
        print(story_node.story_piece)

        #while loop that ensures node has choices in the list and has user chose the path
        while len(story_node.choices) > 0:
            choice = input('What do you do? Enter 1 or 2 to continue the story: ')
            
            #conditional that ensures they are chosing 1 or 2
            if choice not in ['1', '2']:
                print('Please choose 1 or 2 to continue the story: ')

            #condition that allows the user to progress through the story
            else:
                chosen_index = int(choice)
                chosen_index -= 1
                chosen_child = story_node.choices[chosen_index]
                print(chosen_child.story_piece)
                story_node = chosen_child

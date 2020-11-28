# Project Goal: Welcome Ancient Ruins Explorer!

# We’ve identified a mysterious chamber deep underground our excavation site. The artifacts held within this chamber would be a considerable addition to the local museum…

# Unfortunately, the chamber lies at the heart of a twisted maze. We’re using a graph data structure to model the ruins. We’ll need your expertise to map out the chambers as we move through them.

# With your help, we’ll find the optimal path to the chamber before our torch burns out.

#imported files
from graph import Graph, build_easy_map, build_medium_map
from vertex import Vertex

map_lst = [['Willimington Estate - Easy Map', build_easy_map], ['Guthery Manor - Medium Map', build_medium_map], ['Difficult Map (under construction - coming soon)','Map is currently unavailable']]

def print_map_idx(map_lst):
    map_str = ''
    count = 0
    for i, map in enumerate(map_lst, 1):
        count = i
        map_str += '{0}: {1}\n'.format(count, map[0])
    map_str += str(count + 1) + ': make your own map (tools under construction - coming soon)\n'
    map_str += str(count + 2) + ': exit\n'
    return map_str

def play_map(map):
    map_created = map()
    map_created.explore()

#map selection
def map_selection():
    #user selction for one of the preloaded maps
    while True:
        map_idx = int(input('Select the Mansion you want to enter for your next heist mission or make your own map.\n{0}'.format(print_map_idx(map_lst)))) - 1
        if map_idx < len(map_lst) and map_idx >= 0:
            play_map(map_lst[map_idx][1])
            map_selection()
            
        
        #user selection if they want to build their own map
        elif map_idx == len(map_lst):
            print('Currently unavailable. Please come back later for this feature.')
        
        #user selection if they want to exit game
        elif map_idx == len(map_lst) + 1:
            return False
        
        #Incorrect selection
        else:
            print('Invalid selection.')
            map_selection()
    

#intro to mansion heist
print('Welcome to Mansion Heist! Let\'s prepare to find some treasure.\n')

map_selection()

print('Thanks for playing! Keep it quiet and sneaky!')

#excavation_site = build_graph()

#excavation_site.explore()
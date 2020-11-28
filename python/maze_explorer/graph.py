#code created by Codecademy

#imported files
from vertex import Vertex

class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, node):
        self.graph_dict[node.value] = node
    
    def add_edge(self, from_node, to_node, weight = 0):
        self.graph_dict[from_node.value].add_edge(to_node.value, weight)
        self.graph_dict[to_node.value].add_edge(from_node.value, weight)

    def explore(self):
        print('Exploring the graph...\n')
        #FILL IN EXPLORE METHOD BELOW
        current_room = 'Entrance'
        path_total = 0
        print('\nStarting off at the {0}\n'.format(current_room))
        
        #while loop that determines if the current room is treasure room, if not it continues to search
        while current_room != 'Treasure room':
            node = self.graph_dict[current_room]
            for connected_room, weight in node.edges.items():
                key = connected_room[0]
                print('enter {0} for {1}: {2} cost'.format(key, connected_room, weight))
            valid_choices = [name[0] for name in node.edges.keys()]
            print('\nYou have accumulated: {0} cost'.format(path_total))
            choice = input('\nWhich room do you move to? ').upper()
            choice.lower()
            if choice not in valid_choices:
                print('please select from these letters: {0}'.format(valid_choices))
            else:
                for room in node.edges.keys():
                    if room.startswith(choice):
                        current_room = room
                        path_total += node.edges[room]
                print('\n*** You have chosen: {0} ***\n'.format(current_room))
        
        print('Made it to the treasure room with {0} cost'.format(path_total))
                


    def print_map(self):
        print('\nMAZE LAYOUT\n')
        for node_key in self.graph_dict:
            print('{0} connected to...'.format(node_key))
            node = self.graph_dict[node_key]
            for adjacent_node, weight in node.edges.items():
                print('=> {0}: cost is {1}'.format(adjacent_node, weight))
                print('')
            print('')

def build_easy_map():
    easy_map = Graph()

    #ROOMS INTO VERTICES
    entrance = Vertex('Entrance')
    ante_chamber = Vertex('Ante-chamber')
    kings_room = Vertex('King\'s room')
    grand_gallery = Vertex('Grand gallery')
    treasure_room = Vertex('Treasure room')

    #ROOMS TO GRAPH
    easy_map.add_vertex(entrance)
    easy_map.add_vertex(ante_chamber)
    easy_map.add_vertex(kings_room)
    easy_map.add_vertex(grand_gallery)
    easy_map.add_vertex(treasure_room)

    
    #EDGES BETWEEN ROOMS
    easy_map.add_edge(entrance, ante_chamber, 7)
    easy_map.add_edge(entrance, kings_room, 3)
    easy_map.add_edge(ante_chamber, kings_room, 1)
    easy_map.add_edge(grand_gallery, ante_chamber, 2)
    easy_map.add_edge(grand_gallery, kings_room, 2)
    easy_map.add_edge(grand_gallery, treasure_room, 4)
    easy_map.add_edge(ante_chamber, treasure_room, 6)

    #CODECADEMY PROVIDED CODE
    easy_map.print_map()
    return easy_map


def build_medium_map():
    medium_map = Graph()

    #ROOMS INTO VERTICES
    entrance = Vertex('Entrance')
    ante_chamber = Vertex('Ante Chamber')
    library = Vertex('Library')
    dining_room = Vertex('Dining Room')
    billiards_room = Vertex('Billiards Rooms')
    sun_room = Vertex('Sun Room')
    cigar_room = Vertex('Cigar Room')
    wine_cellar = Vertex('Wine Cellar')
    patio = Vertex('Patio')
    green_house = Vertex('Green House')
    treasure_room = Vertex('Treasure Room')

    #ROOMS TO GRAPH
    medium_map.add_vertex(ante_chamber)
    medium_map.add_vertex(entrance)
    medium_map.add_vertex(library)
    medium_map.add_vertex(dining_room)
    medium_map.add_vertex(billiards_room)
    medium_map.add_vertex(sun_room)
    medium_map.add_vertex(cigar_room)
    medium_map.add_vertex(patio)
    medium_map.add_vertex(green_house)
    medium_map.add_vertex(wine_cellar)
    medium_map.add_vertex(treasure_room)

    #EDGES BETWEEN ROOMS
    medium_map.add_edge(entrance, ante_chamber, 2)
    medium_map.add_edge(entrance, library, 6)
    medium_map.add_edge(ante_chamber, dining_room, 5)
    medium_map.add_edge(ante_chamber, cigar_room, 8)
    medium_map.add_edge(library, dining_room, 2)
    medium_map.add_edge(library, billiards_room, 3)
    medium_map.add_edge(cigar_room, wine_cellar, 4)
    medium_map.add_edge(billiards_room, sun_room, 2)
    medium_map.add_edge(billiards_room, patio, 4)
    medium_map.add_edge(sun_room, patio, 1)
    medium_map.add_edge(wine_cellar, patio, 5)
    medium_map.add_edge(patio, green_house, 5)
    medium_map.add_edge(green_house, treasure_room, 3)

    #print and return map object 
    medium_map.print_map()
    return medium_map
class Node:
    def __init__(self, id, name):
        # id is the number of the node as an integer (the priority)
        self.id = id
        # name is the name of the node as a Character (can be self chosen)
        self.name = name
        self.list_of_links = []
        self.costs_to_root = 0
        self.root_node = self
        self.next_node_to_root = self

    def printout_object(self):
        return self.id + ' ' + self.name

    def send_message(self):
        for k in self.list_of_links:
            k.get_partner(self).receive_message(self.root_node, self.costs_to_root, k.costs, self)

    def receive_message(self, foreign_root_node, costs_to_root, costs_of_route, sender):
        costs_of_new_route = costs_to_root + costs_of_route
        if foreign_root_node.id < self.root_node.id:
            self.root_node = foreign_root_node
            self.costs_to_root = costs_of_new_route
            self.next_node_to_root = sender
        elif foreign_root_node.id == self.root_node.id and costs_of_new_route < self.costs_to_root:
            self.root_node = foreign_root_node
            self.costs_to_root = costs_of_new_route
            self.next_node_to_root = sender

class Link:
    def __init__(self, start, end, costs):
        self.start = start
        self.end = end
        self.costs = costs

    def printout_object(self):
        return self.start.name + ' ' + self.end.name + ' ' + str(self.costs)

    # if a node1 has a link saved, this method gets node2
    def get_partner(self, recipient):
        if recipient == self.end:
            return self.start
        elif recipient == self.start:
            return self.end

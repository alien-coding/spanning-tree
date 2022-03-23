# main.py
import sys
import re
from Link import Link
from Node import Node


def check_input():
    if len(sys.argv) <= 2:
        print("Error: Arguments missing. Usage: [filename].py [importfile].txt [Number for cycles]")
        sys.exit()
    elif not sys.argv[1].endswith('.txt'):
        print("Error: wrong file format of input file. Usage: [filename].py [importfile].txt [Number for cycles]")
        sys.exit()


def read_import_file():
    list_of_nodes = []
    list_of_links = []
    with open(sys.argv[1], 'r') as f:
        first_line = f.readline()
        if re.search("Graph [a-z|A-Z]*{\n", first_line):
            title_of_graph = first_line[5:len(first_line)-2]
        else:
            print("Error: file format of input file wrong")
            sys.exit()
        for line in f:
            # to find Node in import file
            if re.search("[a-z|A-Z] = [0-9];", line):
                list_of_nodes.append(Node(line[8], line[4]))
            # to find links in import file
            elif re.search("[a-z|A-Z] - [a-z|A-Z] : [0-9]{1,3};", line):
                number = int(line[12:len(line)-2])
                start = ([i for i in list_of_nodes if i.name == line[4]][0])
                end = ([i for i in list_of_nodes if i.name == line[8]][0])
                list_of_links.append(Link(start, end, number))
#        print([k.printout_object() for k in list_of_links])
#        print([k.printout_object() for k in list_of_nodes])
        for node in list_of_nodes:
            for link in list_of_links:
                if node == link.start or node == link.end:
                    node.list_of_links.append(link)
#        print([k.printout_object() for k in list_of_nodes[2].list_of_links])
    return list_of_nodes, title_of_graph


def output(list_of_nodes, title_of_graph):
    output_string = "Results for Graph: " + title_of_graph + "\n\n// NodeX: Use NodeY as Next Hop to Root \n\n"
    for k in list_of_nodes:
        if k.root_node == k:
            output_string += k.name + ' -> Root (' + str(k.costs_to_root) + ')' + '\n'
        else:
            output_string += k.name + ' -> ' + k.next_node_to_root.name + ' (' + str(k.costs_to_root) + ')' + '\n'
    print(output_string)


def main():
    check_input()
    list_of_nodes, title_of_graph = read_import_file()
    for i in range(int(sys.argv[2])):
        for k in list_of_nodes:
            k.send_message()
    output(list_of_nodes, title_of_graph)


if __name__ == "__main__":
    main()

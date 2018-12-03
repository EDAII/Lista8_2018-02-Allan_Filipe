from django.shortcuts import render
import time
import networkx as nx


def home(request):
    if request.method == 'POST' and request.FILES['myfile'] and request.POST['selectedOption']:
        myfile = request.FILES['myfile']
        byte_str = myfile.file.read()

        # Convert to a "unicode" object
        text_obj = byte_str.decode('UTF-8')

        # Choosing algorithm options
        if request.POST['selectedOption'] == "Gerar Métricas":
            columns_descriptions, all_data = read_csv(text_obj.splitlines())

            time_initial_create = time.time()
            classes_graph = create_graph(all_data)
            time_final_create = time.time() - time_initial_create

            time_initial_nodes = time.time()
            classes_nodes = classes_graph.nodes
            time_final_nodes = time.time() - time_initial_nodes

            nodes_number = []
            for i in range(1, len(classes_nodes) + 1):
                nodes_number.append(i)

            time_initial_edges = time.time()
            classes_edges_tuple = classes_graph.edges
            time_final_edges = time.time() - time_initial_edges

            edges_number = []
            classes_edges = []
            i = 0
            for edge in classes_edges_tuple:
                i = i + 1
                edges_number.append(i)
                classes_edges.append(list(edge))

            time_initial_degrees = time.time()
            nodes_degrees_table = create_nodes_degree_table(classes_graph)
            time_final_degrees = time.time() - time_initial_degrees

            max_in_degree = max(classes_graph.in_degree, key=getKey)
            max_out_degree = max(classes_graph.out_degree, key=getKey)
            max_degree = max(classes_graph.degree, key=getKey)

            min_in_degree = min(classes_graph.in_degree, key=getKey)
            min_out_degree = min(classes_graph.out_degree, key=getKey)
            min_degree = min(classes_graph.degree, key=getKey)

            return render(request, 'result.html', {'algorithm': request.POST['selectedOption'],
                                                   'time_final_create': time_final_create,
                                                   'time_final_nodes': time_final_nodes,
                                                   'time_final_edges': time_final_edges,
                                                   'time_final_degrees': time_final_degrees,
                                                   'nodes_degrees_table': nodes_degrees_table,
                                                   'max_in_degree': max_in_degree,
                                                   'max_out_degree': max_out_degree,
                                                   'max_degree': max_degree,
                                                   'min_in_degree': min_in_degree,
                                                   'min_out_degree': min_out_degree,
                                                   'min_degree': min_degree,
                                                   'classes_edges': classes_edges,
                                                   'nodes_number': nodes_number,
                                                   'edges_number': edges_number,
                                                   'classes_nodes': classes_nodes})
        else:
            # Nothing to do
            pass

    else:
        # Nothing to do
        pass

    return render(request, 'home.html')


def getKey(item):
    return item[1]


def create_nodes_degree_table(classes_graph):
    nodes_degrees_table = []

    for (in_degree, out_degree, degree) in zip(classes_graph.in_degree, classes_graph.out_degree, classes_graph.degree):
        nodes_degrees_table.append([in_degree[0], in_degree[1], out_degree[1], degree[1]])

    return nodes_degrees_table


def create_graph(dataset):
    classes_graph = nx.DiGraph()

    for line in dataset:
        if len(line) == 1:
            classes_graph.add_node(line[0])
        else:
            for i in range(1, len(line)):
                classes_graph.add_edge(line[0], line[i])

    return classes_graph


def read_csv(file):
    all_data = []
    columns_descriptions = []

    # Save all csv data in a list of lists, removing '\n' at the last line element.
    for line in file:
        if not columns_descriptions:
            columns_descriptions = line.split(",")
            columns_descriptions[-1] = columns_descriptions[-1].strip("\n")
        else:
            line_splitted = line.split(",")
            line_splitted[-1] = line_splitted[-1].strip("\n")
            all_data.append(line_splitted)

    return columns_descriptions, all_data

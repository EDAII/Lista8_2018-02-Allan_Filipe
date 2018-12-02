from django.shortcuts import render
import time


def home(request):
    if request.method == 'POST' and request.FILES['myfile'] and request.POST['selectedOption']:
        myfile = request.FILES['myfile']
        byte_str = myfile.file.read()

        # Convert to a "unicode" object
        text_obj = byte_str.decode('UTF-8')

        # Choosing algorithm options
        if request.POST['selectedOption'] == "Knapsack Iterativo":
            columns_descriptions, values, weights, limit = read_csv_knapsack(text_obj.splitlines())

            item_weight_table = create_item_weight_table(values, weights)

            weights_list = create_weight_list(limit)

            time_initial = time.time()
            result, table = knapSack(limit, weights, values, len(values))
            time_final = time.time() - time_initial

            items = getItems(table, limit, len(values), weights, values)

            table = put_itens_on_table(table)

            return render(request, 'result.html', {'algorithm': request.POST['selectedOption'],
                                                   'weights_list': weights_list,
                                                   'limit': limit,
                                                   'result': result,
                                                   'table': table,
                                                   'items': items,
                                                   'time_final': time_final,
                                                   'item_weight_table': item_weight_table})

        elif request.POST['selectedOption'] == "Maior Subsequência Crescente":
            columns_descriptions, all_data = read_csv(text_obj.splitlines())

            time_initial = time.time()
            longest_value, resolution_list = longest_increasing_subsequence(all_data)
            time_final = time.time() - time_initial

            dataset_with_list, id_list = put_resolution_list_on_dataset(all_data, resolution_list)

            return render(request, 'result.html', {'algorithm': request.POST['selectedOption'],
                                                   'columns_descriptions': columns_descriptions,
                                                   'longest_value': longest_value,
                                                   'time_final': time_final,
                                                   'id_list': id_list,
                                                   'resolution_list': resolution_list,
                                                   'dataset_with_list': dataset_with_list,
                                                   'all_data': all_data})

        else:
            # Nothing to do
            pass

    else:
        # Nothing to do
        pass

    return render(request, 'home.html')


def put_itens_on_table(table):
    new_table = list(table)
    current_string = "{} {}"

    for i in range(0, len(table)):
        new_table[i].insert(0, current_string.format("{", "}"))
        if i == 0:
            current_string = "{}" + current_string.format("", "") + str(i + 1) + " " + "{}"
        else:
            current_string = "{}" + current_string.format("", "") + "; " + str(i + 1) + " " + "{}"

    return new_table


def create_weight_list(limit):
    weights_list = []

    for weight in range(0, limit + 1):
        weights_list.append(weight)

    return weights_list


def create_item_weight_table(values, weights):
    values_quantit = len(values)

    data = []
    for number in range(0, values_quantit):
        data.append([number + 1, values[number], weights[number]])

    return data


def read_csv_knapsack(file):
    values = []
    weights = []
    limit = []
    columns_descriptions = []

    # Save all csv data in a list of lists, removing '\n' at the last line element.
    for line in file:
        if not columns_descriptions:
            columns_descriptions = line.split(",")
            columns_descriptions[-1] = columns_descriptions[-1].strip("\n")
        else:
            data = line.split(",")
            values.append(int(data[0]))
            weights.append(int(data[1]))
            limit.append(int(data[2]))

    return columns_descriptions, values, weights, limit[0]


def getItems(values_table, weight_limit, values_quantit, weights, values):
    result = values_table[values_quantit][weight_limit]
    items = []

    for number in range(values_quantit, 0, -1):
        if result <= 0:
            break
        if result == values_table[number - 1][weight_limit]:
            continue
        else:
            items.append(weights[number - 1])

            result = result - values[number - 1]
            weight_limit = weight_limit - weights[number - 1]

    return items


def knapSack(weight_limit, weights, values, values_quantit):
    values_table = [[0 for x in range(weight_limit + 1)] for x in range(values_quantit + 1)]

    for item in range(values_quantit + 1):
        for weight in range(weight_limit + 1):
            if item == 0 or weight == 0:
                values_table[item][weight] = 0
            elif weights[item - 1] <= weight:
                values_table[item][weight] = max(values[item - 1] + values_table[item - 1][weight - weights[item - 1]], values_table[item - 1][weight])
            else:
                values_table[item][weight] = values_table[item - 1][weight]

    return values_table[values_quantit][weight_limit], values_table


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


def longest_increasing_subsequence(receive_data):
    dataset = list(receive_data)
    resolution_list = [1 for _ in range(len(dataset))]

    for i in range(len(dataset)):
        for j in range(i):
            if int(dataset[j][0]) <= int(dataset[i][0]):
                resolution_list[i] = max(resolution_list[i], resolution_list[j] + 1)

    return max(resolution_list), resolution_list


def put_resolution_list_on_dataset(dataset, resolution_list):
    new_dataset = [[], []]
    id_list = []

    for i in range(0, len(dataset)):
        id_list.append(dataset[i][0])
        new_dataset[0].append(dataset[i][0])

    for i in range(0, len(resolution_list)):
        new_dataset[1].append(resolution_list[i])

    return new_dataset, id_list

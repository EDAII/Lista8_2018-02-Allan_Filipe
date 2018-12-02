# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W


def knapSack(weight_limit, weights, values, values_quantit):
	values_table = [[0 for x in range(weight_limit + 1)] for x in range(values_quantit + 1)]

	# Build table values_table[][] in bottom up manner
	for item in range(values_quantit + 1):
		for weight in range(weight_limit + 1):
			if item == 0 or weight == 0:
				values_table[item][weight] = 0
			elif weights[item - 1] <= weight:
				values_table[item][weight] = max(values[item - 1] + values_table[item - 1][weight - weights[item - 1]], values_table[item - 1][weight])
			else:
				values_table[item][weight] = values_table[item - 1][weight]

	return values_table[values_quantit][weight_limit], values_table


# Driver program to test above function
values = [1, 6, 18, 22, 28]
weights = [1, 2, 5, 6, 7]
weight_limit = 11
values_quantit = len(values)
best, table = knapSack(weight_limit, weights, values, values_quantit)
print(best)
print(table)

# This code is contributed by Bhavya Jain

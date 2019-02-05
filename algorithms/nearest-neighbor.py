''' a program by nate weeks to solve travelling salesman problem with the
nearest neighbor hueristic - January 2019'''

def nearest_neighbor_algorithm(input, starting_point):
    '''takes an array of points and a starting point not included in the array
    and returns the total distance spent visiting each point once and returning
    to the starting point as well as the order of points visited'''
    distance = 0
    order_of_points = []
    finishing_point = starting_point[:]
    while input != []:
        nearest_neighbor = find_nearest_neighbor(input, starting_point)
        order_of_points.append(nearest_neighbor[1])
        distance += nearest_neighbor[0]
        starting_point = nearest_neighbor[1]
        if len(input) == 1:
            nearest_neighbor = find_nearest_neighbor([finishing_point], input[0])
            order_of_points.append(nearest_neighbor[1])
            distance += nearest_neighbor[0]
        input.remove(starting_point)
    return [distance, order_of_points]


def find_nearest_neighbor(input, starting_point):
    '''takes an input of an array and a starting point not included in the array
    and returns the closest point to the starting point in the array and the amount
    of units it takes to move there'''
    least_distance = 0
    for point in input:
        distance = 0
        measuring_point = starting_point[:]
        while measuring_point != point:
            if measuring_point[0] < point[0]:
                measuring_point[0] += 1
            if measuring_point[0] > point[0]:
                measuring_point[0] -= 1
            if measuring_point[1] < point[1]:
                measuring_point[1] += 1
            if measuring_point[1] > point[1]:
                measuring_point[1] -= 1
            distance += 1
        if least_distance == 0 or distance < least_distance:
            least_distance = distance
            closest_point = point
    return [least_distance, closest_point]

print(nearest_neighbor_algorithm([[2,2],[2,8], [23, 12]], [1,1]))

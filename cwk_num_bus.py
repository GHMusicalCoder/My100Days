# my answer
def number(bus_stops):
    count = 0
    for stop in bus_stops:
        count += stop[0]
        count -= stop[1]
    return count


print(number([[10,0],[3,5],[5,8]]))
print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
print(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]))


# others results
def number2(num_set):
    return sum(stop[0] - stop[1] for stop in num_set)

# my favorite
def number(bus_stops):
    return sum(on - off for on, off in bus_stops)
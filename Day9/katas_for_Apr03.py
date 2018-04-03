# kata to convert boolean to Yes or No
def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'

# mine was best practice!


# kata : Determine offspring sex based on genes XX and XY chromosomes
def chromosome_check(sperm):
    return 'Congratulations! You\'re going to have a {0}.'.format('son' if sperm[-1] == 'Y' else 'daughter')


print('-' * 60)
print(chromosome_check('XX'))
print(chromosome_check('XY'))


# mine was similar to best practice
def bp_chromosome_check(sperm):
    return 'Congratulations! You\'re going to have a {}.'.format('son' if 'Y' in sperm else 'daughter')


# kata : will you make it
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if (mpg * fuel_left) >= distance_to_pump else False


print('-' * 60)
print(zero_fuel(50, 25, 2))
print(zero_fuel(100, 50, 1))


# mine was close to bp - but not bp
def bp_zero_fuel(distance_to_pump, mpg, fuel_left):
    return (mpg * fuel_left) >= distance_to_pump


print('-' * 60)
# kata : SortNumbers


def solution(nums):
    return [] if nums is None else sorted(nums, key=lambda i: i)


print(solution([1, 2, 10, 5]))
print(solution([1, 5, 8, 6, 3, 4, 7, 2, 10, 9]))
print(solution(None))


# best practice
def bp_solution(nums):
    return sorted(nums) if nums else []

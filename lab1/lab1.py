# TDDA69
# Lab 1: Intro concepts and functional programming


# Task 1a: Implement sum() as a tail recursive function
def sum_iter(term, lower, successor, upper):
    def iter(lower, result):
        if lower > upper:
            return result
        else:
            return iter(successor(lower), result + term(lower))
    return iter(lower, 0)

print("Testing sum_iter with input 2 and 5, result should be 14.")
print("Result: ", sum_iter(lambda x:x, 2, lambda x:x+1, 5), "\n")

# Task 1b: A tail recursive function is a recursive function where the calculation is performed before
# you make the recursive call (in which you also pass the current result). This means that you don't
# have to push anything to the stack, thus enabling you to keep on making recursive calls
# until you're done/the end of time regardless of stack size.

# Task 2a: Implement prod (usual recursion) and prod_iter (tail).
def prod(term, lower, successor, upper):
    if lower > upper:
        return 1
    else:
        return term(lower) * prod(term, successor(lower), successor, upper)

def prod_iter(term, lower, successor, upper):
    def iter(lower, result):
        if lower > upper:
            return result
        else:
            return iter(successor(lower), result * term(lower))
    return iter(lower, 1)

print("Testing prod_iter with input 1 and 4, result should be 24.")
print("Result: ", prod_iter(lambda x:x, 1, lambda x:x+1, 4), "\n")

# Task 2b: Implement factorial using prod_iter.
def factorial(int):
    return prod_iter(lambda x:x, 1, lambda x:x+1, int)

print("Testing factorial with input 6, expecting result 720")
print("Result: ", factorial(6), "\n")

# Task 3a: Implement functions accumulate and accumulate-iter according to pattern from course page.
def accumulate(combiner, null, term, lower, successor, upper):
    if lower > upper:
        return null
    else:
        return combiner(term(lower), accumulate(combiner, null, term, successor(lower), successor, upper))

def accumulate_iter(combiner, null, term, lower, successor, upper):
    def iter(lower, result):
        if lower > upper:
            return result
        else:
            return iter(successor(lower), combiner(result, term(lower)))
    return iter(lower, null)

# Task 3b: Define product and sum as calls to accumulate and accumulate_iter.
def acc_sum(first, second):
    return accumulate(lambda x,y:x+y, 0, lambda x:x, first, lambda x:x+1, second)

print("Testing accumulate calculating sum with input 2, 5. Expected result is 14")
print("Result: ", acc_sum(2, 5))

def acc_iter_sum(first, second):
    return accumulate_iter(lambda x,y:x+y, 0, lambda x:x, first, lambda x:x+1, second)

print("Testing accumulate_iter calculating sum with input 2, 5. Expected result is 14")
print("Result: ", acc_iter_sum(2, 5))

def acc_prod(first, second):
    return accumulate(lambda x,y:x*y, 1, lambda x:x, first, lambda x:x+1, second)

print("Testing accumulate calculating prod with input 1, 4. Expected result is 24")
print("Result: ", acc_prod(1, 4))

def acc_iter_prod(first, second):
    return accumulate_iter(lambda x,y:x*y, 1, lambda x:x, first, lambda x:x+1, second)

print("Testing accumulate_iter calculating prod with input 1, 4. Expected result is 24")
print("Result: ", acc_iter_prod(1, 4))

# Task 3c: Find what mathematical property the combiner must have for accumulate and accumulate_iter to behave identically.
print("Testing accumulate calculating using subtraction with input 1, 4. Expected result is -10")
print("Result: ", accumulate(lambda x,y:x-y, 0, lambda x:x, 1, lambda x:x+1, 4))

print("Testing accumulate_iter calculating using subtraction with input 1, 4. Expected result is -10")
print("Result: ", accumulate_iter(lambda x,y:x-y, 0, lambda x:x, 1, lambda x:x+1, 4))

# Task 4a: Create a left fold fold1 that works on indexable sequences.
# z is "starting value"
def foldl(function, z ,sequence):
    if len(sequence) == 1:
        return function(z, sequence[0])
    else:
        return foldl(function, function(z, sequence[0]), sequence[1:])

print("Testing left folding with subtraction using the input [1, 2, 3]. Expected result is -6")
print("Result: ", foldl(lambda x,y:x-y, 0, [1,2,3]))

# Task 4b: Same as a but a right fold
def foldr(function, z, sequence):
    if len(sequence) == 1:
        return function(sequence[0], z)
    else:
        return foldr(function, function(sequence[-1], z), sequence[:-1])

print("Testing left folding with subtraction using the input [1, 2, 3]. Expected result is 2")
print("Result: ", foldr(lambda x,y:x-y, 0, [1,2,3]))

# Task 4c: Define the functions map, reverse_r and reverse_l using fold.
def my_map(f, sequence):
    return foldl(lambda x,y:x+[f(y)], [], sequence)

print("Testing map using the sequence [1, 2, 3] and the function element - 1. Expected result is [0, 1, 2]")
print("Result: ", my_map(lambda x:x-1, [1, 2, 3]))

def reverse_r(sequence):
    return foldr(lambda x,y:y+[x], [], sequence)

print("Testing reverse_r using the sequence [1, 2]. Expected result is [2, 1]")
print("Result :", reverse_r([1, 2]))

def reverse_l(sequence):
    return foldl(lambda x,y:[y]+x, [], sequence)

print("Testing reverse_l using the sequence [1, 2]. Expected result is [2, 1]")
print("Result :", reverse_l([1, 2]))

# Task 5a: Define repeat that takes a function and an integer and return f^n. That is, repeat(f,2) = f(f(2)).
def repeat(func, n):
    if n > 0:
        return lambda x:func(repeat(func, n-1)(x))
    else:
        return lambda x:x

print("Testing repeat with the input func = x*x, n = 2 and x = 5. Expected result is 625")
print("Result: ", repeat(lambda x:x*x, 2)(5))

# Task 5b: f must be able to take the result of f, otherwise we could not reapply it multiple times.

# Task 5c: Define compose that takes two functions f, g and return the function f(g(x)).
def compose(f, g):
    return lambda x:f(g(x))

print("Testing compose with the input functions f=x*x, g=x+x and input 5. Expected result is 100.")
print("Result: ", compose(lambda x:x*x, lambda x:x+x)(5))

# Task 5d: Recreate repeat using accumulate and compose.
def repeated_application(func, n):
    return accumulate(compose, lambda x:x, lambda x:func, 1, lambda x:x+1, n)

print("Testing repeated_application with the input func = x*x, n = 2 and x = 5. Expected result is 625")
print("Result: ", repeated_application(lambda x:x*x, 2)(5))

# Task 6a: Write a function that takes f and return the smoothed version with dx=0.01.
def smooth(func):
    dx = 0.01
    return lambda x:(func(x-dx) + func(x) + func(x+dx))/3

print("Testing smooth with input function x*x and input to result = 4. Expected result = 16.000066...65.")
print("Result: ", smooth(lambda x:x*x)(4))

# Task 6b: Write an function calling smooth n times using repeat
def n_fold_smooth(func, n):
    return repeat(smooth, n)(func)

print("Testing n_fold_smooth, smoothing 5 times with the same input as last test. Expected result = 16.00033...34.")
print("Result: ", n_fold_smooth(lambda x:x*x, 5)(4))

def find_max(numbers):  
    maxs=0
    for num in numbers:
        if num > maxs:
            maxs=num

    print(maxs)
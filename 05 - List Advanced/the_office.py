# def multiply_factor(n)


workers_happiness = list(map(int, input().split()))
happiness_factor = int(input())

multiply_by_factor = list(map(lambda n: n * happiness_factor, workers_happiness))

filtered = list(filter(lambda x: x >= sum(multiply_by_factor) / len(multiply_by_factor), multiply_by_factor))

if len(filtered) > len(workers_happiness) / 2:
    print(f"Score: {len(filtered)}/{len(workers_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(workers_happiness)}. Employees are not happy!")
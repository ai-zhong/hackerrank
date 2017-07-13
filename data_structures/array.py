# Given an array, A, of N integers,
# print each element in reverse order as
# a single line of space-separated integers.

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr_rev = ""

# method 2: use 'reverse(range(0, n)', followed by 'arr[i]';
# method 3: use 'range(0, n)' followed by 'arr[n-1-i]';
for i in range(n, 0, -1):
    arr_rev = arr_rev + " " + str(arr[i-1])

print(arr_rev.strip())

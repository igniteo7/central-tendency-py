import math
def arithmetic_mean():
    n = int(input("Enter no of elements"))
    arr = []
    print("Enter elements")
    for i in range(n):
        arr.append(int(input()))
    return sum(arr) / n    
    
def median():
    n = int(input("Enter no of elements"))
    arr = []
    print("Enter elements")
    for i in range(n):
        arr.append(int(input()))
    arr.sort()
    if n % 2 != 0:
        return arr[n // 2]
    else:
        return (arr[(n - 1) // 2] + arr[n // 2]) / 2
    

def mode():
    n = int(input("Enter no of elements"))
    arr = []
    print("Enter elements")
    for i in range(n):
        arr.append(int(input()))
    max_count = 0
    mode = arr[0]
    for i in arr:
        count = arr.count(i)
        if count > max_count:
            max_count = count
            mode = i
    return mode
    

def geometric_mean():
    n = int(input("Enter number of elements: "))
    arr = []
    print("Enter elements:")
    for _ in range(n):
        arr.append(int(input()))
    product = 1.0
    for i in arr:
        product *= i
    return round(product ** (1.0 / n), 4)
    
def harmonic_mean():
    n = int(input("Enter number of elements: "))
    arr = []
    print("Enter elements:")
    for _ in range(n):
        arr.append(int(input()))
    reciprocal = 0
    for i in arr:
        reciprocal += 1.0 / i
    return round(n / reciprocal, 4)

def main():
    
    print("A. Arithmetic_Mean")
    print("B. Median")
    print("C. Mode")
    print("D. Geometric_Mean")
    print("E. Harmonic_Mean")

    value = input("Enter your option (A, B, C, D, E): ")
    if value == "A":
        result = arithmetic_mean()
        print("Arithmetic_Mean = " + str(result))
    elif value == "B":
        result = median()
        print("Median = " + str(result))
    elif value == "C":
        result = mode()
        print("Mode = " + str(result))
    elif value == "D":
        result = geometric_mean()
        print("Geometric_mean = " + str(result))
    elif value == "E":
        result = harmonic_mean()
        print("Harmonic_mean = " + str(result))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

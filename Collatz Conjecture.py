# Start with a number n > 1. Find the number of steps it takes to reach one using the following process: 
# If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1
import matplotlib.pyplot as plt
from art import text2art

def collatz(n):
    sequence = [n]
    while n > 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    length = len(sequence) - 1
    return sequence, length

def lists(vals):
    x = [i for i in range(vals[0], vals[1] + 1) if i > 1]
    y = [collatz(i)[1] for i in x]
    return x, y, max(y)

def plot(x, y):
    plt.figure(figsize=(12, 6))  # Adjust the figure size (wider)
    plt.scatter(x, y, s=10, marker='o')  # Create a scatter plot with small dots
    plt.xlabel('Input Values')
    plt.ylabel('Collatz Sequence Length')
    plt.title('Collatz Sequence Length vs. Input Values')
    plt.grid(True)
    plt.show()

def run_plot():
    nums = input("Enter a range of numbers to check (x y) put space in between numbers: ").split()
    vals = list(map(int, nums))
    x, y, max_y = lists(vals)
    print(f'Longest sequence number: {x[y.index(max_y)]}', '\nLongest sequence length:', max_y)
    plot(x, y)

def check_num_true(n):
    sequence = [n]
    while n > 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    length = len(sequence) - 1
    print(f'Number of steps: {length}')


def main():
    print(text2art('Collatz  Conjecture'))
    
    option = input("Enter '1' to check a number or '2' to plot a range: ")
    if option == '1':
        n = int(input('Enter a number: '))
        check_num_true(n)
    elif option == '2':
        run_plot()
    else:
        print('Invalid option. Please try again.')
    


if __name__ == '__main__':
    main()
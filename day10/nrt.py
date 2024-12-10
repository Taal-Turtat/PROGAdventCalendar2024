import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'square root')
    parser.add_argument('--n_times', '-n', required=False, type=int,default=2, help='n-th root')
    parser.add_argument('--value', '-v', required=True, type=float, help='input value (>=0)')
    parser.add_argument('--initial_value','-i',required=True, type=float, help='input initial value (>=0)')
    args = parser.parse_args()

    n = args.n_times
    a = args.value
    initial_value = args.initial_value

    if a < 0 or initial_value < 0 or n <= 0:
        print('error : input the value which is larger than zero')
        exit()
    
    epsilon = 10
    x = initial_value
    while epsilon > 0.0001:
        x_old = x
        x = x - (x**n - a)/(n * x**(n-1))
        epsilon = abs(x - x_old)
    
    print(x)
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'square root')
    parser.add_argument('--value', '-v', required=True, type=float, help='input value (>=0)')
    parser.add_argument('--initial_value','-i',required=True, type=float, help='input initial value (>=0)')
    args = parser.parse_args()

    a = args.value
    initial_value = args.initial_value

    if a < 0 or initial_value < 0:
        print('error : input value which is larger than zero')
        exit()
    
    epsilon = 10
    x = initial_value
    while epsilon > 0.0001:
        x_old = x
        x = x - (x**2 - a)/(2 * x)
        epsilon = abs(x - x_old)
    
    print(x)

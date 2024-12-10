import argparse
from logarithm_e import logarithm_e

e = 2.7182818

def logarithm_10(a,initial_value):
    epsilon = 10
    x = initial_value
    log10 = logarithm_e(10,initial_value)
    while epsilon > 0.0001:
        x_old = x
        x = x - (10**x-a)/(10**x*log10)
        epsilon = abs(x - x_old)
    
    return x

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'square root')
    parser.add_argument('--value', '-v', required=True, type=float, help='input value (>=0)')
    parser.add_argument('--initial_value','-i',required=True, type=float, help='input initial value (>=0)')
    args = parser.parse_args()

    a = args.value
    initial_value = args.initial_value

    # 真数条件
    if a <= 0 or initial_value <= 0:
        print('error : input the value which is larger than zero')
        exit()
    
    x = logarithm_10(a,initial_value)
    
    print(x)
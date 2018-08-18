import sys

def output_string(n):
    s = ''
    for i in range(1, n+1):
        s += '#'
        print(f'{s:>{n}}')

if __name__ == "__main__":
    n = int(sys.argv[1])
    output_string(n)
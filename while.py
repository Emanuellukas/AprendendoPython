def main():
    x = 0
    while x < 51:
        print(x, end=' ')
        x += 1

    fibonacci(100)

def fibonacci(n):
    y, z = 0, 1
    while z < n:
        print(z)
        y, z = z, (y+z)

if __name__ == '__main__': main()

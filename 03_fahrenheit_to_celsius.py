def main():
    a=float(input('Enter temperature in Farenhiet'))
    c=a-32*(5.0/9.0)
    print(f'Temperature {a}F = {c}C'')


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
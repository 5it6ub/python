def div(x,y):
    return x/y

def main():
    x = 6
    for i in [3,2,1,0]:
        x = div(x,i)
    return x

if __name__ == '__main__':
    main()

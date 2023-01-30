from multiprocessing import Process
def fun(name):
    print(f'Hello {name}')
def main():
    p = Process(target=fun, args=('Peter',))
    p.start()

if __name__ == '__main__':
    main()
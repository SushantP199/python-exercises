import string
import collections

def main():
    myd = collections.deque(string.ascii_lowercase)
    print(len(myd))
    # for i in myd:
    #     print(i+'\n',end=" ")
    # myd.pop()
    # myd.append('z_0')
    # print(myd)
    myd.rotate()
    print(myd)

if __name__ == '__main__':
    main()


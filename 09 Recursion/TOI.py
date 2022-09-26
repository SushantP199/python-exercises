def toh(n, from_bar, to_bar, aux_bar):
    if n == 1:
        print(f"Move disk 1 from {from_bar} to {to_bar}")
        return
    toh(n-1, from_bar, aux_bar, to_bar)
    print(f"Move disk {n} from {from_bar} to {to_bar}")
    toh(n-1, aux_bar, to_bar, from_bar)


n = int(input("Enter number of disc : "))
from_bar = input("Enter starting bar : ")
to_bar = input("Enter end bar : ")
aux_bar = input("Enter auxiliary bar : ")

print()
toh(n, from_bar, to_bar, aux_bar)
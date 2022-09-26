print("Floppy Disk Promblem:\n")
f = int(input("Enter no of free bytes = "))
u = int(input("Enter no of used bytes = "))
o = int(input("Enter size of bytes of deleted file = "))
n = int(input("Enter size of bytes of new created file = "))

f = f - n + o

print(f"Floppy disk will have {f} bytes",u)

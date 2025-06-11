from modules.fibb.core import create_seq, locate

command = input()
seq = None

while command != "Stop":
    num = int(command.split()[-1])
    if command.startswith("Locate"):
        if not seq:
            print("please first create a sequence")
            command = input()
            continue
        print(locate(seq, num))
    elif command.startswith("Create"):
        seq = create_seq(num)
        print(*seq)
    command = input()
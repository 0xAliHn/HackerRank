if __name__ == '__main__':
    N = int(input())

def execute(lst, cmd, *instruct): 
    if cmd == 'insert':
        lst.insert(int(instruct[0]), int(instruct[1]))
    elif cmd == 'print':
        print(lst)
    elif cmd == 'remove':
        lst.remove(int(instruct[0]))
    elif cmd == 'append':
        lst.append(int(instruct[0]))
    elif cmd == 'sort':
        lst.sort()
    elif cmd == 'reverse':
        lst.reverse()
    elif cmd == 'pop':
        lst.pop()
    else: 
        print("Command not recognized!")

lst = []
for _ in range(0,N):
    execute(lst, *input().split())  # The *args will give you all function parameters as a tuple.

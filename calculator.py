

active = 1
step = 0

A = 0
a = A
OP = ""
op = OP
B = 0
b = B
R = 0
r = R

while active:
    A=A
    OP=OP
    B=B
    if step == 0:
        a = input("type 'quit' to quit\n\nfirst number\n")
        if a != A:
            if a.lower() == "quit":
                step = 10
            else:
                A=float(a)
                step+=1
    elif step == 1:
        op = input("type 'quit' to quit\n\noperation type\n")
        if op != OP:
            if op.lower() == "quit":
                step = 10
            else:
                OP=op
                step+=1
    elif step == 2:
        b = input("type 'quit' to quit\n\nsecond number\n")
        if b != B:
            if b.lower() == "quit":
                step = 10
            else:
                B=float(b)
                step+=1
    elif step == 3:
        if (OP.lower() == "add") | (OP == "+"):
            r = A + B
            OP="+"
            print(f"{A} {OP} {B} = {r}")
            step+=1
        elif (OP.lower() == "subtract") | (OP == "-"):
            r = A - B
            OP="-"
            print(f"{A} {OP} {B} = {r}")
            step+=1
        elif (OP.lower() == "multiply") | (OP == "*"):
            r = A * B
            OP="*"
            print(f"{A} {OP} {B} = {r}")
            step+=1
        elif (OP.lower() == "divide") | (OP == "/"):
            r = A / B
            OP="/"
            print(f"{A} {OP} {B} = {r}")
            step+=1
        else:
            step = 9
    elif step == 4:
        step+=1
    elif step == 5:
        q = input("quit now? (Y/n)\n")
        if q.lower() == "y":
            step = 10
        elif q.lower() == "n":
            step = 0
        else:
            print("invalid option")
            step = 4
    elif step == 9:
        print("invalid command")
        step = 0
    elif step == 10:
        print("goodbye")
        active = 0
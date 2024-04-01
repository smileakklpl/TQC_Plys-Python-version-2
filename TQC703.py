TUPLE = ()
string = input()
while string != "end":
    TUPLE +=(string,)
    string = input()
print(TUPLE)
print(TUPLE[0:3])
print(TUPLE[-3:])
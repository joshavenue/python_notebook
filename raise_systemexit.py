x = input('type a or b')

if x.lower() == 'a':
    print('A')
elif x.lower() == 'b':
    y = input('more?')
    if y.lower() == 'n':
        print('ok no more')
    elif y.lower() == 'y':
        print('what more?')
else:
    raise SystemExit

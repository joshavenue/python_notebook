a = [10,20,30,20,10,50,60,40,80,50,40,'a','b','a']

dup_items = set(a)
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)

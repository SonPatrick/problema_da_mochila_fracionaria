from bag_frac import make_bag_frag
w = 16

with open('100_item.txt','r') as f:
    items = [i.replace('\n','').replace('(','').replace(')','') for i in f.readlines()]
    pv = [tuple(map(float, i.split(','))) for i in items]

    make_bag_frag(pv, w)
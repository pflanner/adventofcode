from util import get_lines_for_day
from functools import reduce
from operator import mul
from itertools import product

def dfs(v,g,x,y):
    v.add((x,y))
    return sum([1+dfs(v,g,nx,ny)for nx,ny in[(x+dx,y+dy)for dx,dy in product(*[[1,0,-1]]*2)if abs(dx)!=abs(dy)]if(nx,ny)not in v and g.get((nx,ny),9)!=9])

if __name__ == '__main__':
    i=get_lines_for_day(2021,9)
    g={(gx,gy):int(val)for gy,l in enumerate(i)for gx,val in enumerate(l)}
    print(sum(1+g[(x,y)]for x,y in[(lx, ly)for lx,ly in g if all(g.get((nx,ny),10)>g[(lx,ly)]for nx,ny in[(lx+dx,ly+dy)for dx,dy in product(*[[1,0,-1]]*2)if abs(dx)!=abs(dy)])])) # part 1
    v=set()
    print(reduce(mul,sorted([1+dfs(v,g,*loc)for loc in[(lx,ly)for lx,ly in g if all(g.get((nx,ny),10)>g[(lx,ly)]for nx,ny in[(lx+dx,ly+dy)for dx,dy in product(*[[1,0,-1]]*2)if abs(dx)!=abs(dy)])]])[-3:])) # part 2

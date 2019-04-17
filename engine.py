#!/usr/bin/python3.6

import os

class Universe:
    DEAD = 0
    ALIVE = 1
    def __init__(self, n=10, m=10):
        self.n = n
        self.m = m
        self.map = list()
        for i in range(n):
            temp = [0] * m
            self.map.append(temp)

    def get_map(self):
        return self.map

    def console_output(self):
        for this_list in self.map:
            for elem in this_list:
                if elem == Universe.DEAD:
                    print('o', end=' ')
                else:
                    print('*', end=' ')
            print()

    def file_input(self, this_file):
        self.map = list()
        for line in this_file:
            temp = list()
            for val in line.split():
                temp.append(int(val))
            self.map.append(temp)

    def _count_neighbors(self, this_map, x, y): #TODO more optimized/pythonic way
        alive = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                
                if i == 0 and j == 0:
                    continue

                ind_x = (x + i + self.n) % self.n
                ind_y = (y + j + self.m) % self.m

                if this_map[ind_x][ind_y] == Universe.ALIVE:
                    alive += 1
        return alive

    def step(self): #TODO without copy
        copy = [row[:] for row in self.map]
        for i, this_list in enumerate(self.map):
            for j, elem in enumerate(this_list):
                alive = self._count_neighbors(copy, i, j)
                if alive == 3:
                    self.map[i][j] = Universe.ALIVE
                if self.map[i][j] == Universe.ALIVE and (alive != 3 and alive !=2):
                    self.map[i][j] = Universe.DEAD
    



def main():
    universe = Universe()
    f = open('init', 'r')
    universe.file_input(f)
    
    universe.console_output()
    print()
    while True:
        input()

        os.system('clear')
        universe.step()
        universe.console_output()
    

if __name__ == '__main__':
    main()

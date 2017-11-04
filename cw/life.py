#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

'''
Input is matrix of cells.
Output is matrix of cells after n generations, cropped around all living cells.

how do we want to organize the storage of cell data?
The fact that the final necessary dimensions of the matrix are unknown makes things difficult.

We can:
    1: start with a universe twice the size of the current one
        Whenever a cell comes into contact with the edge of the universe,
            double the size of the universe and map the cells over
        Store cells as 1s and 0s in the matrix
        We can easily check neighboring cells


'''



class Universe:
    def __init__(self, cells):
        #square initial universe
        self.cell_arr = np.array(cells)
        (rows, cols) = self.cell_arr.shape
        self.n = max(self.cell_arr.shape)
        square_arr = np.zeros(self.n*self.n).reshape(self.n,self.n)
        square_arr[0:rows, 0:cols] += self.cell_arr
        self.cell_arr = square_arr

    def pad_uni(self):
        n = self.n
        m = n*3
        new_uni = np.zeros(m*m).reshape(m,m)
        new_uni[n:2*n, n:2*n] += self.cell_arr
        self.cell_arr = new_uni
        self.n = m

    def check_edges(self):
        top = any(self.cell_arr[0,:])
        bottom = any(self.cell_arr[self.n-1,:])
        left = any(self.cell_arr[:,0])
        right = any(self.cell_arr[:,self.n-1])
        return any([top, bottom, left, right])

    def is_edge(self, index):
        top = index[0] == 0
        bottom = index[0] == self.n-1
        left = index[1] == 0
        right = index[1] == self.n-1
        return any([top, bottom, left, right])

    def get_neighbor_count(self, index):
        row, col = index[0], index[1]
        u = max(0,row-1)
        b = min(self.n , row+2)
        l = max(0, col-1)
        r = min(self.n, col+2)


        hood = self.cell_arr[u:b, l:r]
        #print hood
        #print np.sum(hood)-self.cell_arr[row,col]
        return np.sum(hood)-self.cell_arr[row,col]

    def is_alive_next_round(self, neighbor_count, currently_alive):
        if currently_alive:
            if neighbor_count == 2 or neighbor_count == 3:
                return 1
            else:
                return 0
        else:
            if neighbor_count == 3:
                return 1
            else:
                return 0

    def live_generation(self):
        if self.check_edges():
            self.pad_uni()
        n = self.n

        counts = np.zeros(n*n).reshape(n,n)

        for index, x in np.ndenumerate(self.cell_arr):
            count = self.get_neighbor_count(index)
            counts[index] = count
        #self.print_array()
        #print self.cell_arr
        #print self.n
        #print counts

        new_cell_arr = np.zeros(n*n).reshape(n,n)

        for index, x in np.ndenumerate(self.cell_arr):
            new_cell_arr[index] = self.is_alive_next_round(counts[index], x)

        self.cell_arr = new_cell_arr


    def print_array(self):
        s = []
        for row in self.cell_arr:
            for cell in row:
                s.append('▓▓' if cell else '░░')
            s.append('\n')
        print ''.join(s)


    def crop_array(self):
        row_populated = np.any(self.cell_arr, axis=1)
        col_populated = np.any(self.cell_arr, axis=0)

        populated_rows = np.where(row_populated == 1)
        populated_cols = np.where(col_populated == 1)

        first_row = populated_rows[0][0]
        last_row = populated_rows[0][-1]

        first_col = populated_cols[0][0]
        last_col = populated_cols[0][-1]

        #print(first_row, last_row, first_col, last_col)

        new_cell_arr=self.cell_arr[first_row:last_row+1, first_col:last_col+1]
        self.cell_arr = new_cell_arr

def get_generation(cells, generations):
    uni = Universe(cells)
    for g in range(generations):
        uni.live_generation()

    uni.crop_array()
    arr = uni.cell_arr.tolist()
    return arr

def htmlize(array):
    s = []
    for row in array:
        for cell in row:
            s.append('▓▓' if cell else '░░')
        s.append('<br />')
    return ''.join(s)

def print_array(array):
    s = []
    for row in array:
        for cell in row:
            s.append('▓▓' if cell else '░░')
        s.append('\n')
    print ''.join(s)

start = [[1,0,0],
         [0,1,1],
         [1,1,0]]
end   = [[0,1,0],
         [0,0,1],
         [1,1,1]]

# test.describe('Glider<:LF:>' + htmlize(start))
# test.it('Glider 1')
#
# resp = get_generation(start, 1)
# test.expect(resp == end, 'Got<:LF:>' + htmlize(resp) + '<:LF:>instead of<:LF:>' + htmlize(end))



if __name__ == "__main__":

    # f = open('life_file.html', 'w')
    # f.write(htmlize(start))
    # f.close()
    uni = Universe(start)
    uni.print_array()
    #uni.live_generation()
    #uni.print_array()


    for i in range(20):
        uni.live_generation()
        uni.print_array()

    uni.crop_array()
    uni.print_array()

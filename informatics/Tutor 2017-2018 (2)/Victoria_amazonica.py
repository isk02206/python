'''
Example answer
'''


class Leaf():
    
    def __init__(self, file_location):
        
        self.bitmap = []
        self.width = 0
        self.height = 0
        self.reader = open(file_location, 'r')
        
        # Open the file and read the data. The leaf bitmap is represented as a
        # 2-D matrix (i.e., as a list of lists), as this simplifies indexing.
        
        for row in open(file_location, 'r'):
            row = list(row)
            if row[-1] == '\n':
                del row[-1]
            
            self.bitmap += [row]
            self.height += 1
            
        self.width = len(self.bitmap[0])
        
    def __str__(self):
        
        string_representation_leaf = ''
        
        for row in self.bitmap:
            string_representation_leaf += ''.join(row) + '\n'
            
        # Remove the last End Of Line character from the string representation
        
        return string_representation_leaf
    
    def fill(self, row_index, column_index):
        
        assert self.bitmap[row_index][column_index] == ' ', 'bit must be empty'
        
        bit_counter = 0
        
        # Given an empty bit, filling is done by visiting the left, right, top and bottom
        # neighbor of that bit. We do not visit neighbors that contain the symbols # or .,
        # nor do we visit neighbors that do not belong to the bitmap.
        
        # Neighbors is a set that keeps track of the empty neighbors to visit.
        
        neighbors = {(row_index, column_index)}
        
        while neighbors:
            
            # Randomly select an empty neighbor to visit.
            
            i, j = neighbors.pop()
            
            # Fill the empty neighbor.
            
            self.bitmap[i][j] = '.'
            
            # Count the number of empty neighbors filled.
            
            bit_counter += 1
            
            # Add further empty neighbors to the set of neighbors (on the condition that
            # these neighbors belong to the rectangular grid).
            
            for di, dj in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                if 0 <= i + di < self.height and 0 <= j+ dj < self.width:
                    if self.bitmap[i + di][j + dj] == ' ':
                        neighbors.add((i + di, j + dj))
                        
            return bit_counter
        
        def clear(self):
            
            for row_index, row in enumerate(self.bitmap):
                for column_index, column in enumerate(row):
                    if self.bitmap[row_index][column_index] == '.':
                        self.bitmap[row_index][column_index] = ' '
                        
        def cellsizes(self):
            
            cell_sizes = []
            
            # Scan the edges of the bitmap for invalid empty cells (i.e., regions of
            # contiguous empty bits that contain empty bits on the outer border), and
            # mark these cells as filled.
            
            for column_index in range(self.width):
                if self.bitmap[0][column_index] == ' ':     # scan top row
                    self.fill(0, column_index)
                if self.bitmap[-1][column_index] == ' ':    # scan bottom row
                    self.fill(self.height - 1, column_index)
                    
            for row_index in range(self.width):
                if self.bitmap[row_index][0] == ' ':           # scan left column
                    self.fill(row_index, 0)
                if self.bitmap[row_index][-1] == ' ':       # scan right column
                    self.fill(row_index, self.width - 1)
                    
            # Scan the entire bitmap for valid empty cells, and mark these cells as filled.
            # We keep track of the size of these valid empty cells.
            
            for row_index, row in enumerate(self.bitmap):
                for column_index, column in enumerate(row):
                    if self.bitmap[row_index][column_index] == ' ':
                        cell_sizes.append(self.fill(row_index, column_index))
                        
            # Clear the entire leaf
            
            self.clear()
            
            # Return the list with cell sizes
            
            return cell_sizes
        
        def cells(self, minimum = 1):
            
            return len([cell_size for cell_size in self.cellsizes() if cell_size >= minimum])
        
        def cellsize(self, minimum = 1):
            
            average_cell_size = 0
            
            filtered_cell_sizes = [cell_size for cell_size in self.cellsizes() if cell_size >= minimum]
            
            if len(filtered_cell_sizes):
                for cell_size in filtered_cell_sizes:
                    average_cell_size += cell_size
                average_cell_size /= len(filtered_cell_sizes)
                return average_cell_size
            
            else:
                return 0
            
leaf = Leaf('leaf.txt')
print(leaf)
print(leaf.fill(5, 30))
print(leaf)
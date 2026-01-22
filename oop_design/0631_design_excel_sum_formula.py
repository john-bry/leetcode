"""
Design the basic function of Excel and implement the function of the sum formula.

Implement the Excel class:

Excel(int height, char width) Initializes the object with the height and the width of the sheet. The sheet is an integer matrix mat of size height x width with the row index in the range [1, height] and the column index in the range ['A', width]. All the values should be zero initially.

void set(int row, char column, int val) Changes the value at mat[row][column] to be val.

int get(int row, char column) Returns the value at mat[row][column].

int sum(int row, char column, List<String> numbers) Sets the value at mat[row][column] to be the sum of cells represented by numbers and returns the value at mat[row][column]. This sum formula should exist until this cell is overlapped by another value or another sum formula. numbers[i] could be on the format:
"ColRow" that represents a single cell.

For example, "F7" represents the cell mat[7]['F'].
"ColRow1:ColRow2" that represents a range of cells. The range will always be a rectangle where "ColRow1" represent the position of the top-left cell, and "ColRow2" represents the position of the bottom-right cell.

For example, "B3:F7" represents the cells mat[i][j] for 3 <= i <= 7 and 'B' <= j <= 'F'.

Note: You could assume that there will not be any circular sum reference.

For example, mat[1]['A'] == sum(1, "B") and mat[1]['B'] == sum(1, "A").
"""


class Excel:

    def __init__(self, height: int, width: str):
        self.height = height
        self.width = ord(width) - ord('A') + 1
        self.cells = {}
        self.formulae = {}

    def set(self, row: int, column: str, val: int) -> None:
       cell = (row, column)
       self.cells[cell] = val

       if cell in self.formulae:
           del self.formulae[cell]

       self._recalculate_dependents(cell)

    def get(self, row: int, column: str) -> int:
       cell = (row, column)

       if cell in self.formulae:
           return self._calculate_sum(cell)

       return self.cells.get(cell, 0)

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        cell = (row, column)
        referenced_cells = self._parse_formula(numbers)
        self.formulae[cell] = referenced_cells

        total = self._calculate_sum(cell)
        self.cells[cell] = total

        return total

    def _parse_formula(self, numbers: List[str]) -> List[Tuple[int, int]]:
        cells = []
        for item in numbers:
            if ':' in item:
                start, end = item.split(':')
                cells.extend(self._extend_range(start, end))
            else:
                cells.append(item)

        return cells

    def _extend_range(self, start: str, end: str) -> List[Tuple[int, int]]:
        start_col = start[0]
        start_row = int(start[1:])
        end_col = end[0]
        end_row = int(end[1:])

        cells = []

        for col_ord in range(ord(start_col), ord(end_col) + 1):
            col = chr(col_ord)
            for row in range(start_row, end_row + 1):
                cells.append(f"{col}{row}")
        
        return cells
    
    def _calculate_sum(self, cell: tuple) -> int:
        """Calculate sum for a cell with a formula"""
        if cell not in self.formulas:
            return self.cells.get(cell, 0)
        
        total = 0
        for cell_ref in self.formulas[cell]:
            # Parse cell reference like "A1"
            col = cell_ref[0]
            row = int(cell_ref[1:])
            
            # Recursively get value (handles nested formulas)
            total += self.get(row, col)
        
        return total
    
    def _recalculate_dependents(self, changed_cell: tuple) -> None:
        """
        When a cell changes, recalculate all cells that depend on it
        This is the KEY to automatic updates!
        """
        row, col = changed_cell
        changed_cell_ref = f"{col}{row}"
        
        # Find all cells that reference this cell in their formula
        for formula_cell, referenced_cells in self.formulas.items():
            if changed_cell_ref in referenced_cells:
                # This cell depends on the changed cell, recalculate it
                new_value = self._calculate_sum(formula_cell)
                self.cells[formula_cell] = new_value
                
                # Recursively update cells that depend on THIS cell
                self._recalculate_dependents(formula_cell)
        


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
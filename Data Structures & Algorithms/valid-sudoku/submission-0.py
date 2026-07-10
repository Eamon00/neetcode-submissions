import numpy as np

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check there are no dupes in rows
        for row in board:
            count = {}
            for number in row:
                if number == '.':
                    continue
                else:
                    count[number] = 1 + count.get(number, 0)
            for value in count.values():
                if value > 1:
                    return(False)

        #first_col = [x[0] for x in board])
        # check there are no dupes in columns
        for i in range(len(board)):
            col = [x[i] for x in board]
            seen = set()
            for numbers in col:
                if numbers == '.':
                    continue
                if numbers in seen:
                    return False
                seen.add(numbers)
                
        # check there are no dupes in 3x3
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                seen = set()
                for row in board[start_row:start_row + 3]:
                    for col in range(start_col, start_col + 3):
                        number = row[col]
                        
                        if number == '.':
                            continue
                        if number in seen:
                            return False
                        seen.add(number)
                        
        return(True)
        
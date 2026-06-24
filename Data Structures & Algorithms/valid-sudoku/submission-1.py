class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # to track numbers in each square
        squares = []
        # to track numbers in columns
        cols = []

        for _ in range(9):
            squares.append({})
            cols.append({})

        def determine_square(row_num, col_num) -> int:
            """Determines which square by row and column."""
            if row_num <=2:
                match col_num:
                    case c if c <= 2:
                        return 0
                    case c if c <= 5:
                        return 1
                    case _:
                        return 2

            elif row_num <= 5:
                match col_num:
                    case c if c <= 2:
                        return 3
                    case c if c <= 5:
                        return 4
                    case _:
                        return 5

            else:
                match col_num:
                    case c if c <= 2:
                        return 6
                    case c if c <= 5:
                        return 7
                    case _:
                        return 8

        for row_num, row in enumerate(board):
            row_boxes = {}

            for col_num, box in enumerate(row):
                if box == ".":
                    continue

                if box in cols[col_num]:
                    return False

                column = cols[col_num]
                column[box] = True

                square_number = determine_square(row_num, col_num)
                if box in squares[square_number]:
                    return False
                
                squares[square_number][box] = True

                if box in row_boxes:
                    return False
                
                row_boxes[box] = True

        return True


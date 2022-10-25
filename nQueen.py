import sys
import time

QUEEN_BOX: str = "👑"
WHITE_BOX: str = "⬜"
BLACK_BOX: str = "⬛"


class NQueen:
    def __init__(self, N: int) -> None:
        self.N = N
        self.board = self.genChessBoard()
        self.main()

    def getBoxColor(self, row: int, col: int) -> str:
        return BLACK_BOX if (row + col) % 2 == 0 else WHITE_BOX

    def genChessBoard(self) -> list:
        return [[self.getBoxColor(i, j) for j in range(self.N)] for i in range(self.N)]

    def printSolution(self) -> None:
        for i in range(self.N):
            print("".join(self.board[i]))

    def isQueenByPosition(self, row: int, col: int) -> bool:
        return self.board[row][col] == QUEEN_BOX

    def isSafe(self, row: int, col: int) -> bool:
        for i in range(col):
            if self.isQueenByPosition(row=row,col=i):
                return False

        for i, j in zip(range(row, -1, -1),
                        range(col, -1, -1)):
            if self.isQueenByPosition(row=i,col=j):
                return False

        for i, j in zip(range(row, self.N, 1),
                        range(col, -1, -1)):
            if self.isQueenByPosition(row=i,col=j):
                return False

        return True

    def solveNQUtil(self, col: int = 0) -> bool:
        if col >= self.N:
            return True

        for row in range(self.N):
            if not self.isSafe(row, col):
                continue

            self.board[row][col] = QUEEN_BOX
            if self.solveNQUtil(col + 1):
                return True

            self.board[row][col] = self.getBoxColor(row, col)

        return False

    def main(self) -> None:
        startTime = time.time()
        if self.solveNQUtil():
            self.printSolution()
            print("Total Taken Time:{:.6f}".format(time.time()-startTime))
            return

        print("Solution does not exist")


if __name__ == "__main__":
    N = 8
    if (len(sys.argv) > 1):
        N = int(sys.argv[1])
    NQueen(N)

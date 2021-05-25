public class BadExample {
    int getLiveNeighborCount(boolean[][] landscape, int row, int column) {
        if (row < 0 || row > landscape.length - 1 || column < 0 || column > landscape.length - 1)
            throw IndexOutOfBoundsException();

        int count = 0;
        for (int i = row - 1; i <= row + 1; i++) {
            for (int j = column - 1; j <= column + 1; j++) {
                if ((i > -1 && j > -1 && i < landscape.length && j < landscape[0].length && landscape[i][j]))
                    count++;
            }
        }
        return landscape[row][column] ? count - 1 : count;
    }
}

public class GoodExample {
    int getLiveNeighborCount(boolean[][] landscape, int row, int column) {
        assertBounds(landscape, row, column);

        int count = 0;
        // for (int i = row - 1; i <= row + 1; i++) {
        //     for (int j = column - 1; j <= column + 1; j++) {
        //         if (isThereALiveCellAt(landscape, i, j))
        //             count++;
        //     }
        // }
        if (isThereALiveCellAt(landscape,row -1, column)) count++;
        if (isThereALiveCellAt(landscape,row -1, column -1)) count++;
        if (isThereALiveCellAt(landscape,row -1, column +1)) count++;
        if (isThereALiveCellAt(landscape,row, column -1)) count++;
        if (isThereALiveCellAt(landscape,row, column +1)) count++;
        if (isThereALiveCellAt(landscape,row +1, column)) count++;
        if (isThereALiveCellAt(landscape,row +1, column -1)) count++;
        if (isThereALiveCellAt(landscape,row +1, column +1)) count++;

        return isThereALiveCellAt(landscape, row, column) ? count - 1 : count;
    }

    private boolean isThereALiveCellAt(boolean[][] landscape, int row, int column) {
        return row > -1 && column > -1 && row < landscape.length && column < landscape[0].length
                && landscape[row][column];
    }

    private void assertBounds(boolean[][] landscape, int row, int column) {
        if (row < 0 || row > landscape.length - 1 || column < 0 || column > landscape.length - 1)
            throw IndexOutOfBoundsException();
    }
}
# 数独是一个非常有名的游戏。整个是一个9X9的大宫格，其中又被划分成9个3X3的小宫格。要求在每个小格中放入1-9中的某个数字。要求是：每行、每列、每个小宫格中数字不能重复。 现要求用计算机求解数独


def get_sudoku_answer(existing_sudoku, unfilled_regions=None):
    # get indexs for cur region
    if unfilled_regions is None:
        unfilled_regions = []
        for i in range(len(existing_sudoku)):
            for j in range(len(existing_sudoku[0])):
                if existing_sudoku[i][j] == 0:
                    unfilled_regions.append((i,j))
    elif len(unfilled_regions) <= 0:
        return True
    cur_region = unfilled_regions[0]

    # get value candidates for cur region
    value_candidates = set([_ for _ in range(1,10)])
    for i in range(len(existing_sudoku)):
        if existing_sudoku[i][cur_region[1]] in value_candidates:
            value_candidates.remove(existing_sudoku[i][cur_region[1]])
    for j in range(len(existing_sudoku[cur_region[0]])):
        if existing_sudoku[cur_region[0]][j] in value_candidates:
            value_candidates.remove(existing_sudoku[cur_region[0]][j])
    index_for_small_sudoku = cur_region[0]-cur_region[0]%3,cur_region[1]-cur_region[1]%3
    for i in range(index_for_small_sudoku[0],index_for_small_sudoku[0]+3):
        for j in range(index_for_small_sudoku[1],index_for_small_sudoku[1]+3):
            if existing_sudoku[i][j] in value_candidates:
                value_candidates.remove(existing_sudoku[i][j])

    # choose one value for cur region, and search next unfilled region
    for single_value in value_candidates:
        existing_sudoku[cur_region[0]][cur_region[1]] = single_value
        if get_sudoku_answer(existing_sudoku,unfilled_regions[1:]) is True:
            return True
        existing_sudoku[cur_region[0]][cur_region[1]] = 0
    return False

if __name__ == "__main__":
    sudoku = [
            [0,9,0,0,0,0,0,6,0],
            [8,0,1,0,0,0,5,0,9],
            [0,5,0,3,0,4,0,7,0],
            [0,0,8,0,7,0,9,0,0],
            [0,0,0,9,0,8,0,0,0],
            [0,0,6,0,2,0,7,0,0],
            [0,8,0,7,0,5,0,4,0],
            [2,0,5,0,0,0,8,0,7],
            [0,6,0,0,0,0,0,9,0],
            ]

    get_sudoku_answer(sudoku)
    for i in range(9):
        print(" ".join( [str(one) for one in sudoku[i]] ))

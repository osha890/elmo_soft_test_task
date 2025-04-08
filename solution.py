from typing import List


def is_last_element_reachable(nums: List[int]) -> bool:
    goal_index = len(nums) - 1
    for i in range(goal_index - 1, -1, -1):
        if nums[i] >= goal_index - i:
            goal_index = i

    if goal_index == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    lsts = [
        [2, 3, 1, 1, 4],  # True
        [1, 1, 2, 0, 3, 0, 0, 1],  # True
        [2, 0, 2, 0, 10, 0, 0, 0],  # True
        [3, 2, 1, 0, 4],  # False
        [1, 1, 2, 0, 2, 0, 0, 1],  # False
        [0, 1, 2, 0, 3, 0, 0, 1],  # False
        [1],  # True
        [],  # False
    ]

    for lst in lsts:
        print(f"{lst} {is_last_element_reachable(lst)}")

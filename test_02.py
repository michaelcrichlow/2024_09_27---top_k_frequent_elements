def top_k_frequent_elements(nums: list[int], k: int) -> list[int]:
    local_dict: dict[int, int] = dict()
    local_array: list[int] = []

    for val in nums:
        if val in local_dict:
            local_dict[val] += 1
        else:
            local_dict[val] = 1
    sorted_list = sorted(local_dict.items(),
                         key=lambda item: item[1], reverse=True)

    for i in range(k):
        local_array.append(sorted_list[i][0])
    return local_array


def main() -> None:
    val = top_k_frequent_elements([1, 1, 1, 2, 2, 3], 2)
    print(val)


if __name__ == '__main__':
    main()

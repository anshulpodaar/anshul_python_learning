"""
Hash Table
"""

import typing

class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
        print("\n")

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            # for entry in self.data_map[index]:
            #     if entry[0] == key:
            #         return entry[1]
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


def _main():
    my_hash_table = HashTable()

    my_hash_table.set_item('bolts', 1400)
    my_hash_table.set_item('washers', 50)
    my_hash_table.set_item('lumber', 70)

    my_hash_table.print_table()

    print(my_hash_table.get_item('lumber'))
    print(my_hash_table.get_item('lumbers'))
    print(my_hash_table.get_item('bolts'))
    print(my_hash_table.get_item('bolt'))
    print(my_hash_table.get_item('washers'))
    print(my_hash_table.get_item('washer'))

    print("\n")

    print(my_hash_table.keys())

    print("-------------------------\n")


# 1 - Item in common (Find if two lists have any items in common)
def item_in_common(list1: list, list2: list):
    # # inefficient
    # for i in list1:
    #     for j in list2:
    #         if i == j:
    #             return True
    # return False
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return True
    return False


# 2 - Find Duplicates
def find_duplicates(nums: list[int]) -> list[int]:
    # duplicates = set()
    # my_dict = {}
    # for i in nums:
    #     if i in my_dict:
    #         duplicates.add(i)
    #     else:
    #         my_dict[i] = True
    # return list(duplicates)
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1
    duplicates = [num for num, count in num_counts.items() if count > 1]
    return duplicates



# 3 - First Non-Repeating Character
def first_non_repeating_char(string: str):
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char in string:
        if char_counts[char] == 1:
            return char
    return None


# 4 - Group Anagrams
def group_anagrams(strings: list[str]):

    # My approach
    anagram_groups = {}
    for s in strings:
        my_hash = 0
        for letter in s:
            my_hash = (my_hash + ord(letter) * 23)
        if my_hash not in anagram_groups.keys():
            anagram_groups[my_hash] = [s]
        else:
            anagram_groups[my_hash].append(s)
    # print(list(anagram_groups.values()))

    # # Suggested solution
    # anagram_groups = {}
    # for string in strings:
    #     canonical = ''.join(sorted(string))
    #     if canonical in anagram_groups:
    #         anagram_groups[canonical].append(string)
    #     else:
    #         anagram_groups[canonical] = [string]
    # return list(anagram_groups.values())

    return list(anagram_groups.values())


# 5 - Two Sum
def two_sum(nums: int, target: int):
    # # My solution
    # output = []
    # for i, num in enumerate(nums):
    #     if (target-num) in nums[i+1:]:
    #         output = [i, (nums[i+1:].index(target-num) + i+1)]
    # return output

    # Suggested solution
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []


# 6 - Subarray Sum
def subarray_sum(nums: int, target: int):
    # # My solution (does not use dictionaries
    # for i in range(len(nums)):
    #     temp = nums[i]
    #     if temp == target:
    #         return [i, i]
    #     j = i+1
    #     while j < len(nums):
    #         temp = temp + nums[j]
    #         if temp == target:
    #             return [i, j]
    #         else:
    #             j += 1
    # return []

    # Suggested solution
    sum_index = {0: -1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum - target in sum_index:
            return [sum_index[current_sum - target] + 1, i]
        sum_index[current_sum] = i
    return []


# 7 - Set: Remove Duplicates
def remove_duplicates(my_list: list):
    return list(set(my_list))


# 8 - Set: Has Unique Chars
def has_unique_chars(s: str) -> bool:
    length_all_char = len(s)
    length_unique_char = len(set(s))
    if length_all_char == length_unique_char:
        return True
    return False

    # # Suggested solution
    # char_set = set()
    # for char in string:
    #     if char in char_set:
    #         return False
    #     char_set.add(char)
    # return True


# 9 - Set: Find Pairs
def find_pairs(arr1: list[int], arr2: list[int], target: int):
    pairs = []
    for num in set(arr2):
        if (target - num) in set(arr1):
            pairs.append(((target - num), num))
    return pairs

    # # Suggested solution
    # # Convert arr1 to a set for O(1) lookup
    # set1 = set(arr1)
    # # Initialize an empty list to store the pairs
    # pairs = []
    # # Loop through each number in arr2
    # for num in arr2:
    #     # Calculate the complement of the current number
    #     complement = target - num
    #     # Check if the complement is in set1
    #     if complement in set1:
    #         # If it is, add the pair to the pairs list
    #         pairs.append((complement, num))
    # # Return the list of pairs that add up to the target value
    # return pairs


# 10 - Set: Longest Consecutive Sequence
def longest_consecutive_sequence(nums: list[int]) -> int:
    longest_sequence = 0
    num_set = set(nums)

    for num in num_set:
        if (num-1) not in num_set:
            current_num = num
            current_sequence = 1

            while (current_num + 1) in num_set:
                current_num += 1
                current_sequence += 1

            longest_sequence = max(longest_sequence, current_sequence)

    return longest_sequence


def _exercises():
    # 1 - Item in common (Find if two lists have any items in common)
    print("# 1 - Item in common (Find if two lists have any items in common)")
    list1 = [1,3,5]
    list2 = [2,4,5]
    print(item_in_common(list1, list2))
    list1 = [1,3,5]
    list2 = [2,4,6]
    print(item_in_common(list1, list2))
    print("-------------------------\n")

    # 2 - Find Duplicates
    print("# 2 - Find Duplicates")
    print(find_duplicates([1, 2, 3, 4, 5]))
    print(find_duplicates([1, 1, 2, 2, 3]))
    print(find_duplicates([1, 1, 1, 1, 1]))
    print(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))
    print(find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))
    print(find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))
    print(find_duplicates([]))
    print("-------------------------\n")

    # 3 - First Non-Repeating Character
    print("# 3 - First Non-Repeating Character")
    print(first_non_repeating_char('leetcode'))
    print(first_non_repeating_char('hello'))
    print(first_non_repeating_char('aabbcc'))
    print("-------------------------\n")


    # 4 - Group Anagrams
    print("# 4 - Group Anagrams")
    print("1st set:")
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

    print("\n2nd set:")
    print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))

    print("\n3rd set:")
    print(group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]))
    print("-------------------------\n")


    # 5 - Two Sum
    print("# 5 - Two Sum")
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([3, 3], 6))
    print(two_sum([1, 2, 3, 4, 5], 10))
    print(two_sum([1, 2, 3, 4, 5], 7))
    print(two_sum([1, 2, 3, 4, 5], 3))
    print(two_sum([], 0))
    print("-------------------------\n")


    # 6 - Subarray Sum
    print("# 6 - Subarray Sum")
    nums = [1, 2, 3, 4, 5]
    target = 9
    print(subarray_sum(nums, target))

    nums = [-1, 2, 3, -4, 5]
    target = 0
    print(subarray_sum(nums, target))

    nums = [2, 3, 4, 5, 6]
    target = 3
    print(subarray_sum(nums, target))

    nums = []
    target = 0
    print(subarray_sum(nums, target))

    nums = [1, 2, 3, 4, 5, 6]
    target = 0
    print(subarray_sum(nums, target))

    print("-------------------------\n")


    # 7 - Set: Remove Duplicates
    print("# 7 - Set: Remove Duplicates")
    my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
    new_list = remove_duplicates(my_list)
    print(new_list)
    print("-------------------------\n")


    # 8 - Set: Has Unique Chars
    print("# 8 - Set: Has Unique Chars")
    print(has_unique_chars('abcdefg'))  # should return True
    print(has_unique_chars('hello'))  # should return False
    print(has_unique_chars(''))  # should return True
    print(has_unique_chars('0123456789'))  # should return True
    print(has_unique_chars('abacadaeaf'))  # should return False
    print("-------------------------\n")


    # 9 - Set: Find Pairs
    print("# 9 - Set: Find Pairs")
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 4, 6, 8, 10]
    target = 7

    pairs = find_pairs(arr1, arr2, target)
    print(pairs)
    print("-------------------------\n")


    # 10 - Set: Longest Consecutive Sequence
    print("# 10 - Set: Longest Consecutive Sequence")
    print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))
    print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2, 6, 7, 8, 9, 10]))
    print("-------------------------\n")



if __name__ == "__main__":
    _main()
    _exercises()

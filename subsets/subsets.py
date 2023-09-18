'''
Given a set with distinct elements, find all of its distinct subsets.

Input: [1, 3]
Output: [], [1], [3], [1,3]
'''


def find_subsets(arr):
    res = [[]]
    for i in range(len(arr)):
        new_ls = []
        for j in range(len(res)):
            x= list(res[j])
            x.append(arr[i])
            new_ls.append(x)
        res+= new_ls
    return res


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()


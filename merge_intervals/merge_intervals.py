'''
Given a list of intervals, merge all the overlapping intervals to produce a
list that has only mutually exclusive intervals.
'''

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print(self.start, self.end)

def merge(intervals):
    intervals.sort(key=lambda x : x.start )
    prev_start = intervals[0].start
    prev_end = intervals[0].end
    res = [Interval(prev_start, prev_end)]
    for i in range(1, len(intervals)):
        curr_interval = intervals[i]
        curr_start = curr_interval.start
        curr_end = curr_interval.end
        if curr_start<=prev_end:
            if res:
                res.pop()
            prev_end = max(curr_end, prev_end)
            res.append(Interval(prev_start, prev_end))
        else:
            res.append(Interval(curr_start, curr_end))
            prev_end = curr_end
            prev_start = curr_start
    return res


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()

main()




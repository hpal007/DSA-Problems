"""
Given a list of intervals, merge all overlapping intervals.
*Input*: [[1,3],[2,6],[8,10],[15,18]]
*output* : [[1,6], [8,10], [15,18]]
"""

def merge_intervals(intervals):

    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <=last[1]:
            last[1] = current[1]
        else:
            merged.append(current)

    return merged


print(merge_intervals([[1,3],[2,6],[8,10],[15,18],[16,20]]))
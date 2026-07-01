def largest_rectangle_area(heights):
    heights.append(0)
    stack = [-1]
    max_area = 0

    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    heights.pop()
    return max_area


print("Bài 12:", largest_rectangle_area([2, 1, 5, 6, 2, 3]))
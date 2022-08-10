def max_area(height):
    max_size = 0
    left = 0
    right = len(height) - 1

    while left < right:
        y_axis = min(height[left], height[right])
        x_axis = right - left
        area = y_axis * x_axis

        if area > max_size:
            max_size = area

        if height[left] < height[right]:
            left += 1
        elif height[right] < height[left]:
            right -= 1
        else:
            left += 1
            right -= 1

    return max_size

max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
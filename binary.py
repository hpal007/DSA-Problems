def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target element.

    Args:
        arr (list): A sorted list of elements.
        target: The element to search for.

    Returns:
        int: The index of the target if found, else -1.
    """
    left, right = 0, len(arr) - 1  # Initialize pointers to the start and end of the array

    while left <= right:
        mid = (left + right) // 2  # Find the middle index

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid  # Target found, return its index

        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1

        # If target is smaller, ignore right half
        else:
            right = mid - 1

    return -1  # Target not found

# Example usage:
# The array must be sorted for binary search to work.
# binary_search([1, 2, 3, 4, 5], 3) returns 2 because 3 is at index 2.

print(binary_search([1, 2, 3, 4, 5], 3))
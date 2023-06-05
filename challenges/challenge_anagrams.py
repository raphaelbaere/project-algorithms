def is_anagram(first_string, second_string):
    if not first_string and not second_string:
      return (first_string, second_string, False)
    def partition(arr, low, high):
      i = low - 1
      pivot = arr[high]

      for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

      arr[i + 1], arr[high] = arr[high], arr[i + 1]
      return i + 1

    def quicksort_string(arr, low, high):
      if low < high:
        pivot_index = partition(arr, low, high)

        quicksort_string(arr, low, pivot_index - 1)
        quicksort_string(arr, pivot_index + 1, high)

    def quicksort_string_wrapper(string):
       arr = list(string.lower())
       quicksort_string(arr, 0, len(arr) - 1)
       return ''.join(arr)
    first_string_ordered = quicksort_string_wrapper(first_string)
    second_string_ordered = quicksort_string_wrapper(second_string)
    is_it_anagram = first_string_ordered == second_string_ordered
    return (first_string_ordered, second_string_ordered, is_it_anagram)
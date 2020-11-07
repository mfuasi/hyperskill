def list_sum(some_list):
    return 0 if not some_list else some_list[0] + list_sum(some_list[1:])  # recursive case

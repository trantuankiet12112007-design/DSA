def get_front_and_rear(queue_list):
    if not queue_list:
        return None, None
    return queue_list[0], queue_list[-1]

print("Bài 5:", get_front_and_rear([4, 5, 6]))
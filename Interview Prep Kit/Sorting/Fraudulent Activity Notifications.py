import time
import os

def timed_func(fn, n=10000):
    def do_n_times(*args, **kwargs):
        time_start = time.perf_counter()
        for _ in range(n):
            result = fn(*args, **kwargs)
        time_elapsed = time.perf_counter() - time_start
        print(f'{fn.__name__}: {time_elapsed:0.2f} s')
        return result
    return do_n_times


def counting_sort(arr, a_min=0, a_max=200):
    '''
    An implementation of counting sort.
    '''
    freq = (a_max - a_min) * [0]
    sorted_arr = len(arr) * [0]

    for val in arr:
        freq[val - a_min] += 1
    
    for i in range(1, len(freq)):
        freq[i] = freq[i-1] + freq[i]
    freq = [0] + freq[:-1]

    for val in arr:
        i = freq[val - a_min]
        sorted_arr[i] = val
        freq[val - a_min] += 1
    
    return sorted_arr

# @timed_func
def activityNotifications(expenditure, d):
    '''
    Given a list of daily expenditure, determine the number of time a 
    notification is send for potentially fraudulent activity. A potentially
    fraudulent activity is defined as spending exceed twice the median
    spending over the past days, where the number of days in the window is
    defined by d.

    arguments:
    expenditure     list containing the daily expenditure
    d               the number of trailing days to consider in the window

    constraints:
    1 <= |expenditure| <= 10e5
    1 <= d <= n
    0 <= expenditure[i] <= 200

    output:
    returns the number of notifications sent for potentially fraudulent
    activities.
    '''
    num_notifications = 0
    for i in range(len(expenditure) - d):
        exp_window = counting_sort(expenditure[i:i+d])
        cur_value = expenditure[i+d]
        if len(exp_window) % 2 == 1:
            window_median = exp_window[len(exp_window) // 2]
        else:
            window_median = (exp_window[len(exp_window) // 2 - 1]  +
                            exp_window[len(exp_window) // 2]) / 2
        if cur_value >= 2 * window_median:
            num_notifications += 1
    return num_notifications

# @timed_func
def activityNotifications2(expenditure, d):
    '''
    A modified version of the above code. This is the code that was submitted
    to Hacker Rank. The above code becomes very slow with large window sizes.
    '''
    def get_median(freqs, location):
        cumul_freq = 0
        for i, freq in enumerate(running_freqs):
            cumul_freq += freq
            if cumul_freq >= location:
                return i
            
    notifications = 0
    # Take the initial window of expenditure with a width of d and calculate 
    # the frequency of each number in the window. This is the initial
    # step of counting sort.
    running_window = expenditure[:d]
    running_freqs = 201 * [0]
    for val in running_window:
        running_freqs[val] += 1

    is_even = d % 2 == 0
    median_location = d // 2 + d % 2
    
    for current_value in expenditure[d:]:
        window_median = get_median(running_freqs, median_location)
        if is_even:
            # For a window width of even length, the median is the average
            # of the middle two values
            window_median = (window_median + 
                            get_median(running_freqs, median_location + 1)
                            ) / 2
            
        if current_value >= 2 * window_median:
            notifications += 1
        # Shifts the window one position to the right for the next value.
        # Only two values are updated in the frequency array, avoiding
        # having to resort from scratch.
        running_freqs[running_window.pop(0)] -= 1
        running_freqs[current_value] += 1
        running_window.append(current_value)
    return notifications


if __name__ == '__main__':
    windows = [5, 4, 3]
    tests = [[2, 3, 4, 2, 3, 6, 8, 4, 5]
            ,[1, 2, 3, 4, 4]
            ,[10, 20, 30, 40, 50]
    ]
    answers = [2, 0, 1]

    for test, window, answer in zip(tests, windows, answers):
        print(test)
        result = activityNotifications(test, window)
        print(f'{activityNotifications.__name__}: {result == answer}')
        result = activityNotifications2(test, window)
        print(f'{activityNotifications2.__name__}: {result == answer}')

# 633
    fname = os.path.join(os.getcwd(), 'Interview Prep Kit', 'Sorting', 'Fraudulent-1.txt')
    with open(fname, 'r') as f:
        _, d = map(int, f.readline().strip().split())
        exp = list(map(int, f.readline().strip().split()))
    
    print(d)
    print(activityNotifications(exp, d))
# https://stackoverflow.com/questions/11886862/calculating-computational-time-and-memory-for-a-code-in-python/57887141#57887141
# https://en.wikipedia.org/wiki/Counting_sort
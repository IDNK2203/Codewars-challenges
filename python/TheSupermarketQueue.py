# Pseudocode
# create an array with on length n and fill it with zero's (co tiils)
# loop through the customer arrays
# check the co tiils array for the index(till) with the smallest value
# increment that index value with value of i
# after the loop has ran get the height value in the co tills array


def queue_time(customers, no_co_tills):
    co_tills = [0] * no_co_tills
    for i in customers:
        nextEmptyTill = co_tills.index(min(co_tills))
        co_tills[nextEmptyTill] = co_tills[nextEmptyTill] + i
    print(max(co_tills))


queue_time([5, 3, 4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10, 2, 3, 3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the
# queue finish before the 1st person has finished.

queue_time([2, 3, 10], 2)
# should return 12

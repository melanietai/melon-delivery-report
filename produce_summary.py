# # day 1 produce summary
# print("Day 1")
# # open file that stores information for day 1 deliveries
# the_file = open("um-deliveries-day-1.txt")
# # get each line from the file
# for line in the_file:
#     # take away whitespace at the right of the line
#     line = line.rstrip()
#     # create a token of 'words' split from '|' in the str
#     words = line.split('|')

#     # 0 index contains the information of type of melon
#     melon = words[0]
#     # change from index 0 to index 1 to access info for count
#     count = words[1]
#     # change from index 0 to index 2 to access info for amount
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()

# # day 2 produce summary
# print("Day 2")
# the_file = open("um-deliveries-day-2.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()

# # day 3 produce summary
# print("Day 3")
# the_file = open("um-deliveries-day-3.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()

# create a function to generate summary reports for melon deliveries in any day
def generate_summary_report(day, txt_file):
    print("Day", day)
    the_file = open(txt_file)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()

    return True

generate_summary_report("1", "um-deliveries-day-1.txt")
#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:

def process_numbers(file_path):
        with open("numbers.txt", "r") as file:
            numbers = [float(line.strip()) for line in file if line.strip()]

        count = len(numbers)
        total = sum(numbers)
        average = total / count if count > 0 else 0
        highest = max(numbers)
        lowest = min(numbers)

        print(f"Number of values: {count}")
        print(f"total sum: {total}")
        print(f"Average: {average}")
        print(f"Highest number: {highest}")
        print(f"Lowest number: {lowest}")

process_numbers("numbers.txt")
#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 

def count_palindromes(file_path):
    with open(file_path, "r") as file:
        words = [line.strip() for line in file if line.strip()]

    palcount = sum(1 for word in words if word == word[::-1])

    print(f"Total palindromes: {palcount}")

count_palindromes("words.txt")
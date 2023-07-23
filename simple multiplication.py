import random

num_of_ques = int(input("Number of questions to ask? : "))
bigset = []
score = 0
first = second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in first:
    for j in second:
        # populate all possible questions in a list for random selection
        bigset.append([i, j])
while num_of_ques > len(bigset):
    num_of_ques = int(input(f"Kindly consider minimizing the questions to less than {len(bigset)}: "))

# selects random questions from all available options
ques = random.sample(bigset, num_of_ques)

len_questions = len(ques)
print("\nAnswer the following:\n")
for qloop in range(0, len_questions):
    firstnum = ques[qloop][0]
    secondnum = ques[qloop][1]
    ans = input(f"{str(qloop + 1)}) {str(firstnum)} x {str(secondnum)} = ")
    if ans == str(firstnum * secondnum):
        score = score + 1

print(f"\nScore = {str(score)}/{str(num_of_ques)} ")

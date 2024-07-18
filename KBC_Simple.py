#Create a program capable of displaying questions to the user like KBC.

#Use List data type to store the questions and their correct answers.

#Display the final amount the person is taking home after playing the game.

question_list= ["What is the capital of India?","Who is the current Prime Minister of India?", "What is the capital of Australia", "Who is the prime mister of france", "Who is the father of Science?", "What is the name of the fifth planet in our solar system?"]
question_answer = ["New Dehli", "Narendra Modi", "Canberra", "Emmanuel Macron","Albert Einstein", "Jupiter"]

question_option = {1: ["New Dehli","Mumbai","Canberra", "New York"], 2:["Narendra Modi", "Rahul Gandhi", "Amit Shah","Keji Rewal"], 3:["Canberra", "Sydney", "Melbourne", "Perth"], 4:["Emmanuel Macron", "Rishi Sunak", "Emmanuel Gandhi","Borisson Jones"], 5:["Albert Einstein", "Isaac Newton", "Stephen Hawking", "Albert Sabin"], 6:["Jupiter", "Saturn", "Mars", "Venus"]}

print("Welcome to Kaun Banega Crorepati")
print("--------------------------------")
name = input("Enter your name: ")
print("--------------------------------")
user_balance = 0 

for i in range(len(question_list)):
  print(question_list[i])
  print(question_option[i+1])
  selection = input("Enter your answer: ")
  if selection == question_answer[i]:
    print("Correct Answer, you won 500$")
    user_balance += 500
    print(f"your new balance is {user_balance}$")
  else:
    print(f"Wrong Answer, you got {user_balance} $")
    break
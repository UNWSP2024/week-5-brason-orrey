import random

def math_quiz():
    num1 = random.randint(0, 1000)
    num2 = random.randint(0, 1000)
    
    print(f"\n{num1}\n+ {num2}\n------")
    
    user_answer = int(input("Enter your answer: "))
    
    correct_answer = num1 + num2
    
    if user_answer == correct_answer:
        print("Congratulations! Your answer is correct.")
    else:
        print(f"Sorry, that's incorrect. The correct answer is {correct_answer}.")

def main():
    print("Welcome to the Math Quiz!")
    
    while True:
        math_quiz()  # Call the math quiz function
        
        continue_quiz = input("Do you want to answer another question? (yes/no): ")
        
        if continue_quiz != 'yes':
            print("Thank you for playing the Math Quiz! Goodbye!")
            break

main()

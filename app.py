
questions = ["what does CPU stands for", "What does GPU stands for?", "What does RAM stands for?"]
answers = ["central processing unit", "graphical processing unit", "random access memmory"]
score = 0
for x in range(0, len(questions)):
          
          answer = ""

          while True:
               answer = input(questions[x] + " ") 
               to_lower = answer.lower()
               if to_lower ==answers[x]: 
                    print("correct!!")
                    score +=1;
                    print("score", score)
                    break

            
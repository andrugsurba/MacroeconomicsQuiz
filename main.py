import random
import sys
from quizdict import quizdict

print ("Macroeconomics CLEP Preparation Quiz \n")

def main(): 

    wrong_answers=[]
    #The wrong answers get appended here for later review and score calculation
    right_answers=[]
    #Similar to above for the purpose of review and calculation

    missed_questions = False
    scored_points = False
    #Nothing has started yet, so the default for these will be 'False'

    def exit_program():
        print "Goodbye!"
        sys.exit()
        #Exits program

    try:
        num_questions=int(raw_input("Choose a number of questions to display between 1 and 100. To exit, press 0. \n"))
        if num_questions == 0:
            exit_program()
    except ValueError:
        print "Please enter a valid number."
        num_questions=int(raw_input("Choose a number of questions to display between 1 and 100. To exit, press 0. \n"))
    
    count = 0
    #Default number of questions at 0 to start from the beginning

    for key in (quizdict):
    #Iterates over keys in the dictionary
        while num_questions > count:  
            if num_questions > 0 and num_questions <= 85:
                current_question=random.choice(list(quizdict.keys()))
                print ">" + current_question 
                #The current question will be a random key from the quizdict dictionary as long as the number inputted by the user is between 0 and 85
                correct_answer=quizdict.get(current_question)
                #Gets right answer from dictionary
                answer=raw_input("Type your answer: \n" )
                #Prompts user to type answer
                
                if answer.lower()==correct_answer.lower():
                #Converts to lower case in order to match correct answer format
                    print ("Right! \n")
                    right_answers.append(current_question)
                    #Adds to the right_answers list at the top
                    scored_points = True
                    #Updates scored_points to reflect the new answer

                else:
                        print ("Wrong. \n")
                        print "\t The answer is",correct_answer+".\n"
                        wrong_answers.append(current_question)
                        #Adds to the wrong_answers list at the top
                        missed_questions = True
                        #Updates missed_questions to reflect the new answer

                del quizdict[current_question]
                #Deletes the question so that it does not repeat itself

                print "Your score is",str(len(right_answers))+".\n"
                #Converts the length of the right_answers list(number of right answers) to string to display the new score
                count = count + 1
                #Increments the count to the next question until the maximum amount that the user specified is reached
                                

            else:
                num_questions=int(raw_input("Choose a number of questions to display between 1 and 100. To exit, press 0. \n"))

                #Prompts user for number of questions again.

            
        def quiz_result():
            total_score= (len(right_answers)/float(num_questions))*100
            #Calculation is the length of right answers (since it is a list and not an int) divided by num_questions * 100 for the percentage
            #In Python 2.X, it appears a divided number has to be converted to float to not truncate and appear as "0"
            
            print "\tYou scored",len(right_answers),"right out of",num_questions,"questions. Your grade is", "{0:.0f}%.".format(float(total_score))

            if total_score >=60:
                print "\tYou passed this test. \n"
                if total_score == 100:
                    print "\tYou aced it! Congratulations. \n"
            else:
                print "\tYou failed this test.\n"
                
        if num_questions >= 1:
            quiz_result()

        def restart():
            if num_questions >= 1:
            #Only to be run if questions are one or more.
                restart=raw_input("Would you like to play again? Press \"y\" for yes or \"n\" for no. \n")
                #This prompts the user to start again or end the game
                if restart == "y" or restart == "Y":
                    #This is so that lowercase and capital Y are both recognized
                    num_questions
                else:
                    print "Goodbye!"
                    sys.exit()
                    #Exits program
        
        if wrong_answers:
            review = raw_input("Would you like to review the questions you missed? Press \"y\" for yes or \"n\" for no. \n")
            if review == "y" or review == "Y":
                for wrong in wrong_answers:
                    print (wrong)+"\n"
                    #This shows all wrong answers in the list wrong_answers
                restart()
                #Gives option to restart after showing all wrong answers.
            else:
                    restart()
        else:
            restart()

if __name__ == '__main__':
    main()

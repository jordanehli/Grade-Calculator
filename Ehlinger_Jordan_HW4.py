#Author: Jordan Ehlinger
#Assignment Number & Name: HW4 Grade Calculator
#Due Date: N/A
#Program Description: Receive a student's grades for different assignments and then calculate their weighted final grade and present it along with their final letter grade.


##DECLARE GLOBAL CONSTANTS
#weight of each assignment listed as global constants
EXAM_1_WEIGHT = 0.20
EXAM_2_WEIGHT = 0.20
EXAM_3_WEIGHT = 0.20
HOMEWORK_WEIGHT = 0.20
RESEARCH_PROJECT_WEIGHT = 0.10
FINAL_PROJECT_WEIGHT = 0.10


##INPUT VALIDATION METHOD
def get_grade(assignment_name):
    #intentional bad value
    grade=-1
    #while loop for input validation
    while grade<0 or grade>100:
        #using f string since input only allows one argument
        grade=float(input(f"What is your grade for {assignment_name}? "))
        #ensures input isn't blank
        if grade == "":
            #intentional bad value
            grade=-1
        #ensures input is between 0-100 inclusive
        elif grade<0 or grade>100:
            print("Grade must be a number between 0 and 100")
            #intentional bad value
            grade=-1
        #returns the valid grade back to the main function
        else:
            return float(grade)


##CALCULATE WEIGHTED GRADE METHDOD
def calc_average(exam_1_grade,exam_2_grade,exam_3_grade,homework_grade,research_grade,final_project_grade):
    #multiplies grade by the assignment weight
    grade_1_weighted = exam_1_grade * EXAM_1_WEIGHT
    grade_2_weighted = exam_2_grade * EXAM_2_WEIGHT
    grade_3_weighted = exam_3_grade * EXAM_3_WEIGHT
    grade_4_weighted = homework_grade * HOMEWORK_WEIGHT
    grade_5_weighted = research_grade * RESEARCH_PROJECT_WEIGHT
    grade_6_weighted = final_project_grade * FINAL_PROJECT_WEIGHT

    #sums the weighted grades to determine student's final grade and returns it back to the main function
    weighted_total_grade = float(grade_1_weighted+grade_2_weighted+grade_3_weighted+grade_4_weighted+grade_5_weighted+grade_6_weighted)
    return weighted_total_grade


##DETERMINE LETTER GRADE
def calc_letter(weighted_total_grade):
    #if loop to determine letter grade based on student's final number grade
    if weighted_total_grade >= 89.50:
        letter_grade=str("A")
    elif weighted_total_grade >= 79.50:
        letter_grade=str("B")
    elif weighted_total_grade >= 69.50:
        letter_grade=str("C")
    elif weighted_total_grade >= 59.50:
        letter_grade=str("D")
    else:
        letter_grade=str("F")
    #returns the letter grade back to the main function
    return letter_grade


##DEFINE MAIN
def main():

    #call function to get grade using assignment name as parameter
    exam_1_grade = get_grade("Exam 1")
    exam_2_grade = get_grade("Exam 2")
    exam_3_grade = get_grade("Exam 3")
    homework_grade = get_grade("Homework")
    research_grade = get_grade("Research Project")
    final_project_grade = get_grade("Final Project")

    #call function to calculate the student's final grade and display it as a final number grade
    weighted_total_grade = calc_average(exam_1_grade,exam_2_grade,exam_3_grade,homework_grade,research_grade,final_project_grade)
    print("Final Numeric Grade: ", format(weighted_total_grade, '.2f'))

    #call function to determine and display the final letter grade
    letter_grade = calc_letter(weighted_total_grade)
    print("Final Letter Grade: ", letter_grade)


##CALL MAIN
main()

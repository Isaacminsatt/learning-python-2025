# Course options to choose from for our recommendation.
english_above_6_shorter = "English_Literature_Shorter_Course"
english_above_6_longer = "English_Literature_Longer_Course"
english_in_6_shorter = "Grammar_Shorter_Course"
english_in_6_longer = "Grammar_Longer_Course"

math_above_6_shorter = "Geometry_Shorter_Course"
math_above_6_longer = "Geometry_Longer_Course"
math_in_6_shorter = "Algebra_Shorter_Course"
math_in_6_longer = "Algebra_Longer_Course"

history_above_6_shorter = "World_History_Shorter_Course"
history_above_6_longer = "World_History_Longer_Course"
history_in_6_shorter = "Ancient_Civilizations_Shorter_Course"
history_in_6_longer = "Ancient_Civilizations_Longer_Course"

geography_above_6_shorter = "Advanced_Human_Geography_Shorter_Course"
geography_above_6_longer = "Advanced_Human_Geography_Longer_Course"
geography_in_6_shorter = "Human_Geography_Shorter_Course"
geography_in_6_longer = "Human_Geography_Longer_Course"

myanmar_above_6_shorter = "Language_skill_Shorter_Course"
myanmar_above_6_longer = "Language_skill_Longer_Course"
myanmar_in_6_shorter = "Reading_Shorter_Course"
myanmar_in_6_longer = "Reading_Longer_Course"

# Collect user attributes to inform our recommendation.
recom = ""
rec_course = input("Would you like to learn about our recommended course? "
              + "(yes/no) : ")
if rec_course == "no":
    print("Okay! Feel free to watch our courses.")
else:
    grade = int(input("What grade are you in? "))
    favorite_subject = input("What is your favorite subject? (English," + 
                        " Math, History, Geography, and Myanmar) :")
    time = input("How much time can you study per week? (a lot/a little) : ")
    if ((grade == 6 or grade < 6) and
        favorite_subject == "English" and
        time == "a little"):
        recom = english_in_6_shorter
    elif ((grade == 6 or grade < 6) and
        favorite_subject == "English" and
        time == "a lot"):
        recom = english_in_6_longer
        
    elif (grade > 6 and favorite_subject == "English" and
          time == "a lot"):
        recom = english_above_6_longer
    elif (grade > 6 and favorite_subject == "English" and
          time == "a little"):
        recom = english_above_6_shorter
        
    elif ((grade == 6 or grade < 6) and
          favorite_subject == "Math" and
         time == "a little"):
        recom = math_in_6_shorter
    elif ((grade == 6 or grade < 6) and
          favorite_subject == "Math" and
         time == "a lot"):
        recom = math_in_6_longer
    elif (grade > 6 and favorite_subject == "Math" and
          time == "a lot"):
        recom = math_above_6_longer
    elif (grade > 6 and favorite_subject == "Math" and
          time == "a little"):
        recom = math_above_6_shorter
        
    elif ((grade == 6 or grade < 6) and
          favorite_subject == "History" and
         time == "a little"):
        recom = history_in_6_shorter
    elif ((grade == 6 or grade < 6) and
          favorite_subject == "History" and
         time == "a lot"):
        recom = history_in_6_longer
    elif (grade > 6 and favorite_subject == "History" and
         time == "a lot"):
        recom = history_above_6_longer
    elif (grade > 6 and favorite_subject == "History" and
         time == "a little"):
        recom = history_above_6_shorter
        
    elif ((grade == 6 or grade < 6) and
          favorite_subject == "Geography" and
         time == "a little"):
        recom = geography_in_6_shorter
    elif ((grade == 6 or grade < 6) and
          favorite_subject == "Geography" and
         time == "a lot"):
        recom = geography_in_6_longer
    elif (grade > 6 and favorite_subject == "Geography" and
         time == "a lot"):
        recom = geography_above_6_longer
    elif (grade > 6 and favorite_subject == "Geography" and
         time == "a little"):
        recom = geography_above_6_shorter
        
    elif ((grade == 6 or grade < 6) and
          favorite_subject == "Myanmar" and
         time == "a little"):
        recom = myanmar_in_6_shorter
    elif((grade == 6 or grade < 6) and
          favorite_subject == "Myanmar" and
         time == "a lot"):
        recom = myanmar_in_6_longer
    elif (grade > 6 and favorite_subject == "Myanmar" and
          time == "a lot" ):
        recom = myanmar_above_6_longer
    elif (grade > 6 and favorite_subject == "Myanmar" and
          time == "a little" ):
        recom = myanmar_above_6_shorter
    print("We recommend the Online Learning Platform course: " + recom)
    
import difflib
from __builtin__ import raw_input


def degreeScore(word_tokens):
    score = 10
    desiredDegree = "M.Sc"
    word_tokens_lower = [x.lower() for x in word_tokens]
    # searches for similar words
    degree = difflib.get_close_matches(desiredDegree.lower(), word_tokens_lower)
    close_match_fail = False
    close_match = ""
    if degree == []:
        for word in word_tokens_lower:
            if (desiredDegree.lower() in word):
                close_match_fail = Truez
                close_match = word
                break
    stop_search = False
    while (not stop_search):
        if degree == [] and close_match_fail == False:
            answer2 = raw_input("There are no matches. Search again? (Y/N) \n")
            if answer2 == "Y" or answer2 == "y" or answer2 == "yes" or answer2 == "Yes":
                desiredDegree = raw_input("Degree level needed (i.e. 'phd', 'ba', 'bachelor'): ")
                degree = difflib.get_close_matches(desiredDegree.lower(), word_tokens_lower)
            else:
                stop_search = True
        else:
            if close_match_fail == True:
                print("Closest match to " + desiredDegree + " is " +
                close_match + ".")
                stop_search = True
            else:
                print("Closest match to " + desiredDegree + " is " +
                    degree[0] + ".")
                stop_search = True
    close_match_fail = False
    close_match = ""
    stop_search = False
    while (not stop_search):
        answer1 = raw_input("Would you like to search for another degree? (Y/N)\n")
        if answer1 == "Y" or answer1 == "y" or answer1 == "yes" or answer1 == "Yes":
            desiredDegree = raw_input("Degree level needed (i.e. 'phd', 'ba', 'bachelor'): ")
            degree = difflib.get_close_matches(desiredDegree.lower(), word_tokens_lower)
            if degree == []:
                for word in word_tokens_lower:
                    if (desiredDegree.lower() in word):
                        close_match_fail = True
                        close_match = word
                        break
            if degree == [] and close_match_fail == False:
                answer3 = raw_input("There are no matches. Search again? (Y/N) \n")
                if answer3 == "Y" or answer3 == "y" or answer3 == "yes" or answer3 == "Yes":
                    desiredDegree = raw_input("Degree level needed (i.e. 'phd', 'ba', 'bachelor'): ")
                    degree = difflib.get_close_matches(desiredDegree.lower(), word_tokens_lower)
                else:
                    stop_search = True
            else:
                if close_match_fail == True:
                    print("Closest match to " + desiredDegree + " is " +
                        close_match + ".")
                else:
                    print("Closest match to " + desiredDegree + " is " +
                            degree[0] + ".")
        else:
            stop_search = True
    degreeFound = False
    answer4 = raw_input("Would you like to search the word 'degree'? (Y/N) \n")
    if answer4 == "Y" or answer4 == "y" or answer4 == "yes" or answer4 == "Yes":
        print("Searching 'degree' and returning adjacent words...")
        for word in word_tokens_lower:
            if ("degree" in word):
                index = word_tokens_lower.index(word)
                if index - 1 >= 0 and index + 1 < len(word_tokens_lower):
                    prev_word = word_tokens_lower[index - 1]
                    after_word = word_tokens_lower[index + 1]
                    print("Word before 'degree': " + prev_word)
                    print("Word after 'degree': " + after_word)
                    degreeFound = True
                    break
                elif index - 1 >= 0 and index + 1 >= len(word_tokens_lower):
                    prev_word = word_tokens_lower[index - 1]
                    print("Word before 'degree': " + prev_word + "\n")
                    print("No word found after 'degree'.")
                    degreeFound = True
                    break
                elif index - 1 < 0 and index + 1 < len(word_tokens_lower):
                    after_word = word_tokens_lower[index + 1]
                    print("Word after 'degree': " + after_word + "\n")
                    print("No word found before 'degree'.")
                    degreeFound = True
                    break
                else:
                    # should not happen
                    print("The only word in the resume is 'degree'.")
                    degreeFound = True
                    break
        if degreeFound == False:
            print("The word 'degree' does not appear in the resume.")
    else:
        pass
    answer = raw_input("Did you find the degree you were looking for? (Y/N)\n")
    # yes if desired degree found else degree not attained or present
    if answer == "yes" or answer == "Y" or answer == "y" or answer == "Yes": score -= 0
    else: score -= 10
    return score


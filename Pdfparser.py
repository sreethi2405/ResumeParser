
import pdftotext
import getCategory
import tokenizer
import gender_guesser

def init():

    # input the file name
    filename = input("Enter the PDF Resume Name to Parse(with .pdf extension)")
    text = pdftotext.convert(filename)
    fout = open("results.tex", "w")
    fout.write("This document contains the result of parsing\n\\ The data of required attributes is present\n\
    \\title { RESUME PARSING }\n \\begin{document}\n\n")
    text=str(text).replace("\u200b", "") # removing additional characters present while parsing a pdf to text
    return text.replace("\xa0", "")

resume = init()
def main(resume):

    # have the words as tokens in a list
    tokens = tokenizer.input_file_lines(resume, [])
    word_tokens = tokenizer.input_file_words(resume, [])

    while '' in tokens:
        tokens.remove('')
    while ' ' in tokens:
        tokens.remove(' ')
    # get email

    email = ""
    print(tokens)
# code for retrieving the mail id from resume

    for token in word_tokens:
        if "@" in token:
            email = token
            break

    fout = open("results.tex", "a")
    fout.write("\n\n Email id : { " + email + " }\n")


    for i in range(tokens.__len__()):
        if(tokens[i]!=' '):
            print("\nName :" +tokens[i]+ "\n")
            fout.write("\n Name : {" + tokens[i] + "}\n\n")
            # gender guessing
            sex = gender_guesser.genderguesser(tokens[i])
            if sex == 1:
                print("\nGender : MALE")
                fout.write("\n GENDER : { MALE }\n\n")
                break
            if sex == 0:
                print("Gender : FEMALE")
                fout.write("\n GENDER : { FEMALE }\n\n")

           # print(sex)
            break

   # fout.close()

    print("\nQualification Details :")
    recentqualification = getCategory.getqualification(tokens)
    print("\nEmail : ")
    return (email)

if type(resume) == list:
    for i in range(len(resume)):
        print( main(resume[i]))
    fout = open("results.txt", "a")
    fout.write("\\end{document}")
    fout.close()


elif resume != "":
    print (main(resume))
    fout = open("results.txt", "a")
    fout.write("\\end{document}")
    fout.close()


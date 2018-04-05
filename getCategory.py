import re
import tokenizer
import datetime



def getqualification(tokens):
    #print(resume)
    fout = open("results.tex", "a")
    education = ["Education", "EDUCATION", "education", "Academics", "ACADEMICS", "academics"]
    courseplace = ["university", "college", "institute", "technology"]
    titles = ["activities", "honors", "skills", "experience", "achievements", "awards", "hobbies", "hobby", "university", "college", "institute", "technology", "high school", "high", "coursework"]
    yrregx = re.compile("(.*)\d{4}(.*)")
    tokenyrregex = re.compile("\d{4}")
    for k in range(len(education)):
        regex = re.compile("(.*)"+education[k] + "(.*)")


        yrs = []
        qualification = []
        institution = ""
        for i in range(len(tokens)):
            m = regex.search(tokens[i])
            if m:
                previoustoken = tokens[i]
                for k in range(len(courseplace)):
                    courseregex = re.compile("(.*)" + courseplace[k] + "(.*)")
                    for l in range(i, i+3):
                        uni=courseregex.search(str(tokens[l]).lower())
                        if uni:
                            institution= tokens[l]
                            print(tokens[l])
                            if(previoustoken!=tokens[l-1]):
                               for q in range(i+1, l):
                                   qualification.append(tokens[q])
                                   print(qualification)
                                  # fout.write("\n" + qualification)
                            else:
                                index=[]
                                for q in range(len(titles)):
                                    quaregex=re.compile("(.*)"+titles[q]+"(.*)")
                                    for j in range(l+1,len(tokens)):
                                        match=quaregex.search(str(tokens[j]).lower())
                                        if(match):
                                            index.append(j)
                                index.sort()
                                for j in range(l+1,index[0]):
                                    qualification.append(tokens[j])
                                print(qualification)
                            for j in range(i+ 1, len(tokens)):
                                searchyr = yrregx.search(tokens[j])
                                if searchyr:
                                    yrtoken = tokenizer.input_file_words(str(tokens[j]).lower(), [])
                                    break
                            break
                    if (institution!=""):
                         break
    for i in range(len(yrtoken)):
        yrsearchtoken = tokenyrregex.search(yrtoken[i])
        if yrsearchtoken:
            yrs.append(yrtoken[i])
        elif (re.match(r'(.*)present(.*)',yrtoken[i], re.M | re.I)):
            yrs.append("present")
        elif (re.match(r'(.*)now(.*)',yrtoken[i], re.M | re.I)):
            yrs.append("present")
    print(yrs)

    return (institution)



print ("Welcome to my philosphy quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Ok, goodbye!")
    quit()

print ("Ok! Let's play!")
score = 0

print("Question 1:")
answer = input("Which Greek philosopher is believed to have introduced inductive reasoning? ")
if answer.lower() == "socrates":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect!")
    print ("Socrates is said to have introduced inductive reasoning by questioning the fundamental premises of an argument to then build upon said truths.")
    
print ("Question 2:")
answer = input("Locke's fundamental natural rights consist of life, liberty, and ")
if answer.lower() == "property":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect!")
    print ("In Locke's 'Two Treatises of Government', he emphasizes on the natural rights that are fundamental to peoples. With that being said, life, liberty, and property are inalienable rights to any individual.")

print ("Question 3:")
answer = input("What term did Kierkegaard use to call one who acts out of faith despite logical and ethical implications? ")
if answer.lower() == "knight of faith":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect!")
    print ("The knight of faith is one who transcends reason and logic in and through the virtue of the absurd. Unlike the knight of infinite resignation, the knight of faith makes a leap of faith in an effort to attain whatever it is they long for.")

print ("Question 4:")
answer = input("'I think, therefore I am' is a philosophical phrase used as proof of one's existence in the cosmos. It was coined by: ")
if answer.lower() == "descartes":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect!")
    print ("'I think, therefore I am' was coined by Descartes in 1637 in his work 'Discourse on Method'. It represents the attainability of knowledge as a proof for one's existence.")

print ("Question 5:")
answer = input("Who proposed the idea of the 'general will' in the 18th century? ")
if answer.lower() == "rousseau":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect!")
    print ("Jean Jacques Rousseau propelled the idea of the general will in an aim for the common good. While asserting inherent virture, Rousseau's 'general will' expresses what is best from a collective standpoint.")

print ("Question 6:")
answer = input("'Dasein' was a concept famously used by ")
if answer.lower() == "heidegger":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect!")
    print ("'Dasein' is used by Heidegger in reference to the experience of 'being'. That is, Heidegger's phenomalogical investigation of oneself is catalogued under the concept of 'Dasein'.")

print ("Question 7:")
answer = input("'The Second Sex' is known to be a groundbreaking work written by ").lower()
if answer == "de beauvoir" or "simone de beauvoir":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect!")
    print ("In 'The Second Sex', Simone de Beauvoir touches on the disadvantaged position that women have in society. In a historical context, de Beauvoir is a pioneer of the 20th century feminist movement with her existential approach to a social issues.")

print ("Question 8:")
answer = input("Kant's principle of practical rationality is known as the ")
if answer.lower() == "categorical imperative":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect!")
    print ("Kant's Categorical Imperatives are laws by which one must abide to despite any temptations. The laws are based upon the idea of universability, that which can be applied to all rational beings.")

print ("All done!")
print ("You got " + str(score) + " questions correct!")
print ("You got " + str((score/8) * 100) + "%. ")



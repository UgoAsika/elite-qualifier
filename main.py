print("Hello i am a chat bot, make sure to use ? after questions when speaking to me, please capitalization as well at the start of each question, if you want to leave the program make sure to just type q, thank you. Concievable questions : well_being_questions = How are you?" "How is your day?"
"How food are you at math?" "How good is your reading?" "How is where you live?"
 "How old are you?"       "What is your name?",   "Are you human?" "What is your favorite color" "Where do you live?" "What is your favorite sport?" "Who is your favourite athlete?" "What is your favourite food?", "How tall are you")




userreply = input("How are you?").lower()
good = ("good", "great", "awesome", "excellent")
bad = ("bad", "terrible", "poor")
if userreply in good:
  print("Great, lets get started")
else:
  print("Sorry to hear that, would a conversation improve your day?")
  anotherreply = input("Would it?").lower()
  possible_Answers = ["yeah", "yes", "yup", "ok", "alright","yessir", "yes sir", "sure", "of course", "k", "ofcourse", "for sure", "forsure"]
  if anotherreply in possible_Answers:
    print("Alright, lets begin!")
  else:
    print("Alright, i will be ending this conversation immediately.")
    quit()


well_being_questions = ["How are you?", "How is your day?",
"How food are you at math?", "How good is your reading?", "How is where you live?" ]

Knowledge_questions = ["How old are you?", "What is your name?", "Are you human?", "What is your favorite color", "Where do you live?", "What is your favorite sport?", "Who is your favourite athlete?", "What is your favourite food?",
"How tall are you?"]


real_conversation = input("What do you want to know about me?")

if real_conversation == "q":
  print("Good Bye.")
  quit()

while real_conversation != "q":
  if real_conversation in well_being_questions:
    print("Great!")
  if real_conversation == Knowledge_questions[0]:
    print("I am brand new.")
  if real_conversation == Knowledge_questions[1]:
    print("My name is chat bot")
  if real_conversation == Knowledge_questions[2]:
    print("I am what you want me to be.")
  if real_conversation == Knowledge_questions[3]:
    print("My favourite colour is red.")
  if real_conversation == Knowledge_questions[4]:
    print("I live in a computer.")
  if real_conversation == Knowledge_questions[5]:
    print("My favourite sport is basketball.")
  if real_conversation == Knowledge_questions[6]:
    print("My favourite athlete is stephen curry.")
  if real_conversation == Knowledge_questions[7]:
    print("I dont eat but based on what i have seen i would have to say pizza.")
  if real_conversation == Knowledge_questions[8]:
    print("I do not have a height.")
  real_conversation = input("What do you want to know about me?")

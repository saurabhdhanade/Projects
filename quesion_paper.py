questions_prompt =[
"what is clr of apple? \na) red\nb) green\nc) orenge \n\n",
"what is clr of teeth? \na) red\nb) green\nc)white \n\n",
"what is clr of hairs? \na) red\nb) black\nc) orenge \n\n"
]


class Question:
    def __init__(self,prompt,answer):
        self.prompt=prompt
        self.answer=answer

question = [
    Question(questions_prompt[0],'a'),
    Question(questions_prompt[1],'c'),
    Question(questions_prompt[2],'b')]

def run_test(questions):
    score = 0
    for ques in questions:
        answer=input(ques.prompt)
        if answer==ques.answer:
            score+=1

    print("You got "+ str(score)+ "/" + str(len(questions))+ "correct")
run_test(question)

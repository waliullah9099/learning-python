qna = {
    "hi": "hello",
    "what is your name": "my name is Habiba Aktar",
    "how old are you": "i am only 16 years old"
}


while True:
    try:
        ques = input()
        if ques == "quit":
            break
        else:
            print(qna[ques])

    except:
        print("i don't know")
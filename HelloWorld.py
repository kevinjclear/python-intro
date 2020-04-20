name = input("What is your name? ")

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(name + " said: " + "\"" + message + "\"")
    else:
        print("Goodbye, " + name +"!")

def greet(input):
    if "hello" in input:
        return "hello there"
    else:
        return "what do you mean"

greeting = greet("hello")
print(greeting)
greeting = greet("whatup")
print(greeting)
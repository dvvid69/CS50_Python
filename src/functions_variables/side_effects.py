emoticon = "v.v"


def main():
    global emoticon  # <--- macht die variable emoticon veränderbar in einer funktion
    say("is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)


main()

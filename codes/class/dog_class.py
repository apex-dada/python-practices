class Dog:
    def bark(self):
        print("diguuuu")

def talk(phrase):
    
    def say(word):
        print(word)
        
    words = phrase.split()
    letters= phrase
    for word in words:
        say(word)
        
    for letter in letters:
        say(letter)    
        
        
talk("This is a phrase")
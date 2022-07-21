name = input("Enter your name: ")
place = input("Enter your place: ")
nickname1 = input("Enter your name what people call you at work: ")
nickname2 = input("Enter your name what people call you outside work: ")
position = input("Enter your position that challenged you: ")
skill1 = input("Enter your skill1: ")
skill2 = input("Enter your skill2: ")
skill = input("Enter your skill that people think you're good at: ")
expertise = input("Enter your expertise: ")
role = input("Enter a skill you want to do more: ")
interested_skill = input("Enter your interested skill: ")
relax_skill = input("Enter your relaxing skill: ")
communication = input("Enter your communication style: ")
feedback1 = input("Enter your first way of taking feedback: ")
feedback2 = input("Enter your second way of taking feedback: ")
food = input("Enter your fovorite food: ")

story = "Hi! My name is " + name + ". \nI grew up in " + place + ". \nThe people that work with me (either in the past or currently) would describe me as " + nickname1 + \
        ", but outside of work people would describe me as " + nickname2 + \
        ". \nThe position that challenged me outside my comfort zone the most was " + position + ". \nThere I learned new things and acquired skills such as " + skill1 + \
        ", and " + skill2 + ". \nMost people believe I’m fantastic at " + skill + ". However, my real expertise on this team could be " + expertise + \
        ". One thing I really hope to do more in my current role is " + role + ". \nOne skill I want to get better at is " + interested_skill + \
        " (and if you ideas on how to do this, please let me know). To be at my best and work at my best I need "  + relax_skill + \
        ". \nMy preferred communication style is (email, phone, in-person, etc.) " + communication + \
        ". The best way to give me constructive feedback is to do " + feedback1 + ", and " + feedback2 + \
        ". \nIf you ever want to get me food, here is my favorite thing to eat " + food + "."

print((story))


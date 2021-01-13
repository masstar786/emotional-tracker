name = (input('Enter name: '))
age = int(input('Enter age: '))
emotion = (input('Choose Emotion from Happy, Sad, Angry: '))
if age < 18:
    print("You are underage")
else:
    print("Welcome aboard partner")
if emotion == 'Happy':
    print("I'm so proud of you for being positively happy, don't let anyone take that shine from you")
elif emotion == 'Sad':
    print("Shift you thoughts somewhere else and distract the sadness, everything will be fine soon")
elif emotion == 'Angry':
    print("Think about why you are angry, breathe and it will all get better for you")

print("Hey there", name, "! I see you're", age, "years old!", "Why you feeling", emotion)

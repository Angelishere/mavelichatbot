import tkinter as tk
from tkinter import scrolledtext, ttk
from PIL import Image, ImageTk  # Import Pillow modules
import random
import re

# Chatbot functions

#checks probability
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

#responses for unknown 
def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sorry! i didn't catch that.",
                "Sorry, unclear, can you rephrase?",
                "I'm puzzled, could you clarify?",
                "What does that mean?"][
        random.randrange(6)]
    return response

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
    #hello response
    response1 = ["Namaskaram!",
                "Greetings with joy,let the spirit of onam shine bright!",
                "Ah Hello!",
                "Swagatham!,onam ashamsakal",
                "Greetings my friend! How are you today?",
                "Hello there! What would you like to know today?"][
        random.randrange(6)]
    
    #goodbye response
    response2 = ["Farewell, and may gentle winds guide your path.",
                "Farewell, my friend. May you be blessed!",
                "Goodbye, my friend. Until we meet again!",
                "I've heard there's an amazing sadya feast happening somewhere in Kerala right now. I must be off to find it before it's all gone! Farewell!",
                "Time to bid adieu, but don't worry, I'll be back... someday!",
                "Watch me vanish like I'm hiding in the Onam sadya buffet! Poof, I'm gone! Just kidding, take care ",
                "I must embark on a great quest to find the perfect banana leaf for next year's Onam sadya. Until then, feast well, my friend"][
        random.randrange(7)]
    
    #iamfine response
    response3 = ["Thank you for your kind inquiry. I am in good health and spirits. May blessings and well-being be with you as well.",
                "Enik parama sugham!",
                "I am fine, how about you?",
                "I am well, my friend, and I hope the same for you.",
                "Thank you for your concern. I am in the best of health, both in body and spirit.",
                "Like the monsoon rain that nourishes Kerala's fields, I am refreshed and well!",
                "Until the next Onam, may your life be filled with laughter and prosperity. Goodbye, my friend!",
                "With the blessings of Vamana, I bid you adieu. May your path be filled with success and happiness"][
        random.randrange(8)]
    
    #welcome response
    response4 = ["You are most welcome, my friend. May your days be filled with joy.",
                "No thanks are necessary, for it is a pleasure to be of service,Be well.",
                "The pleasure is mine, dear friend. May our paths cross again in the future.",
                "I'm glad I could be of help. Don't hesitate to reach out whenever you need. ",
                "Not a problem at all. If you ever need help again, don't hesitate to ask!",
                "You are welcome, my friend!"][
        random.randrange(6)]
    
    #thanks response
    response5 = ["Thank you for your kind words. Your praise is truly appreciated.",
                "It is an honor to receive such praise. Thank you sincerely.",
                "Your praise is a treasure. I am thankful for your kind thoughts.",
                "Thank you for your generous words. May your kindness be returned to you",
                "Your kind words are like a ray of sunshine. Thank you.",
                "I am humbled by your compliment. Thank you for your generosity."][
        random.randrange(6)]
    
    #advice response
    response6 = ["In every interaction, choose kindness. Small acts of kindness can make a big difference in someone's day.!",
                "A humble heart is the foundation of greatness. Stay grounded and treat all with respect.",
                "Strength lies in unity. In harmony, we find prosperity.",
                "True wealth is inner peace. Meditate and find tranquility within.",
                "Lead by example and with integrity. Your character is your greatest legacy",
                "Embrace diversity, for it enriches our lives and broadens our perspectives.",
                "In the face of adversity, never compromise your values. Stand firm in what you believe.",
                "Give without expecting in return. Generosity is the true measure of wealth.",
                "Protect the Earth, for it sustains us all. Preserve its beauty for generations to come."][
        random.randrange(9)]
    
    #who are you? response
    response7 = ["I'm Mahabali, and I'm originally from the netherworld known as Pathala. But here's the twist - I make a special trip to visit Kerala every year during Onam to be with my beloved people.",
                "I am Mahabali, also known as Maveli. I am but a humble servant of the people, and my legacy is one of benevolence and harmony. "][
        random.randrange(2)]
    
    #whereyoufrom response
    response8 = ["I hail from the ancient and illustrious land of Kerala, where the spirit of unity, abundance, and harmony has always thrived. ",
                "Kerala is my home, a place rich in culture, heritage, and the warmth of its people.",
                "I am from Kerala where the coconut palms sway, the backwaters glisten, and the spirit of Onam shines brightest."][
        random.randrange(3)]
    
    #what is onam response
    response9 ="Onam is a harvest festival in Kerala, marking the end of the monsoon season and during onam people pay tribute to the legendary King Mahabali, who is believed to visit Kerala during this time to see his people."
    
    #whatyoueat response
    response10 ="I wish i could devour an onasadhya but i cannot eat anything because I'm a bot obviously!"
    
    #bored response
    response11 = ["Well, want to know about onam?",
                "I can tell a joke.",
                "You could always sleep the boredom away",
                "You could maybe watch a movie?",
                "you could go for cycling",
                "Try meditating! thats what i do when i am bored."][
        random.randrange(6)]

    #whatdoing response
    response12 = ["Just hanging out and enjoying some free time.",
                "I'm dancing to the rhythm of life, my friend.",
                "I'm on a journey to inspire and be inspired.",
                "Taking it easy and enjoying the present moment",
                "I am contemplating the lessons of life and learning from the experiences of the past.",
                "Preparing for a grand celebration of Onam, a time when unity and joy reign in my kingdom."][
        random.randrange(6)]
    

    response(response1, ['hello', 'hi', 'hey', 'sup', 'heyo','namaskaram','hala','maveli'], single_response=True)
    response(response2, ['bye', 'goodbye','tata','cya','later'], single_response=True)
    response(response3, ['how', 'are', 'you', 'doing'], required_words=['how'])
    response(response3, ['enthond','vishesham'], required_words=['vishesham'])
    response(response4, ['thankyou','thanks','nanni','thank','you'], single_response=True)
    response(response5, ['you','are','nice','beautiful','generous','amazing','adipoli','awesome'], required_words=['you','are'])
    response(response6, ['can','you','give','me','advice'], required_words=['advice'])
    response(response7, ['who', 'are','you'], required_words=['who','you'])
    response(response8, ['where', 'are','you','from'], required_words=['where','from'])
    response(response9, ['what','is','onam'], required_words=['what','onam'])
    response(response10, ['what','you','eat'], required_words=['you', 'eat'])
    response(response11, ['i','am','bored'], required_words=['i', 'bored'])
    response(response12, ['what','are','you','doing'], required_words=['you', 'doing'])
    


    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return unknown() if highest_prob_list[best_match] < 1 else best_match

#make user input in lower
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# Tkinter GUI functions
def handle_user_input():
    user_input = user_entry.get()
    user_entry.delete(0, tk.END)

    if user_input:
        bot_response = get_response(user_input)
        chat_history.config(state=tk.NORMAL)
        chat_history.insert(tk.END, f'You: {user_input}\n')
        chat_history.insert(tk.END, f'Maveli: {bot_response}\n')
        chat_history.config(state=tk.DISABLED)
        chat_history.see(tk.END)

# Create the main GUI window
root = tk.Tk()
root.title("Maveli Chat Bot")

# Load and display the background image
background_image = Image.open("C:/Users/angel/OneDrive/Desktop/mavelichat/mav.png")  # Replace with the path to your background image
background_photo = ImageTk.PhotoImage(background_image)

# Create a label for the background image and make it fill the entire window
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Style for the GUI
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TText", font=("Helvetica", 12))

# Create a scrolled text widget for chat history
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, height=15, width=40)
chat_history.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create an entry widget for user input
user_entry = ttk.Entry(root)
user_entry.pack(fill=tk.X, padx=10, pady=10)

# Create a "Send" button to submit user input
send_button = ttk.Button(root, text="Send", command=handle_user_input)
send_button.pack(pady=10)

# Run the Tkinter GUI main loop
root.mainloop()

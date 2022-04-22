from tkinter import *

#GUI
root = Tk()
root.title("Caesar Cipher Encoder")

#store alphabet and punctuation as string, not as list, because longer syntax and you can pretty much do the same things to the string as to the list
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "

#function
def Encode_Message():
    original_message = message_entry_field.get()
    offset = offset_field.get()
    encoded_message = ""
    for letter in original_message:
        if letter.lower() not in alphabet and letter not in punctuation: 
            letter_not_in_alphabet_label = Label(text="Your message contains a symbol that is outside of the alphabet. Please input a message with only letters, spaces and symbols (..,?'!)")
            letter_not_in_alphabet_label.pack()
        else:
            if letter.lower() in alphabet:
                old_index = alphabet.index(letter.lower())
                new_index = (old_index - int(offset)) % len(alphabet)
                encoded_message += alphabet[new_index]
            else:
                encoded_message += letter
    label_encoded_message = Label(text="Your encoded message: " + str(encoded_message))
    label_encoded_message.pack()           

#original message label
label_original_message = Label(text="Message to encode: ")
label_original_message.pack()

#original message entry field
message_entry_field = Entry(root, width=50, borderwidth=5)
message_entry_field.pack()
message_entry_field.insert(0, "Only use letters, spaces and symbols (..,?'!): ")

#offset field label
label_offset = Label(text="Offset by (use a whole number: ")
label_offset.pack()

#offset field 
offset_field = Entry(root, width=50, borderwidth=5)
offset_field.pack()
offset_field.insert(0, "Use a whole number - if you use a positive integer the letters will be shifted to the left, if negative integer to the right: ")

#encode your message button
Message_Button = Button(root, text= "Encode Message", command=Encode_Message)
Message_Button.pack()

root.mainloop()
from tkinter import *
import os


'''**************************************************************************************************************'''


#FORMATING
globalFont = "helvetica"
signInColor = "#deede9"
signUpColor = "#98c8bc"
turquoiseColor = "#027976"
greyColor = "#404040"
blueColor = "#BBF3F9"
pinkColor = "#F5DBEA"
boldPinkColor = "#AD2E77"
smallButtonFontColor = "#2b393b"
hand = "hand2"

#get direct path to folder
directory_path = os.path.dirname(__file__)

#account samples [username, password, remainingAttempts]
accounts = [["test1", "0000", 0], ["test2", "1234", 3]]


'''**************************************************************************************************************'''


#FUNCTIONS

#choose the frame to show
def showFrame(frame):
	frame.tkraise()
	#reset entries, notes
	usernameFrame2.delete(0, "end")
	passwordFrame2.delete(0, "end")
	usernameFrame5.delete(0, "end")
	passwordFrame5.delete(0, "end")
	noteMessageFrame2.configure(text="")
	noteMessageFrame5.configure(text="")
	anotherAccountButtonFrame2.configure(text="")
	anotherAccountButtonFrame3.configure(text="")
	
#*******************************************************************************************************************#
#format buttons
def keep_flat(event):						# on click
	if isinstance(event.widget, Button):	# if the click came from a button
		event.widget.config(relief=FLAT)	# enforce button to stay flat	

#*******************************************************************************************************************#
#Connect (Frame 2, 3)
def connect():
	
	#username or password is missing
	if usernameFrame2.get()=="" or passwordFrame2.get()=="":
		noteMessageFrame2.configure(text="Username or password is missing!")
		return

	global accountIndex
	accountIndex = -1

	for account in accounts:
		accountIndex += 1

		#username exists
		if usernameFrame2.get()==account[0]:

			#username exists + remainingAttempts=0 ➡ account is locked
			if account[2]==0:
				noteMessageFrame2.configure(text="Account is locked!")
				connectButtonFrame2.configure(state="disabled", cursor="arrow")
				anotherAccountButtonFrame2.configure(text="Use another account")
				return
			
			#username exists + password correct ➡ got to frame 4
			if passwordFrame2.get()==account[1]:
				account[2]=3	#reset the remainingAttempts (set to 3)
				showFrame(frame4)
				return
			
			#username exists + password incorrect ➡ go to frame 3
			else:
				usernameLabel.configure(text="Hi " + account[0] + "!")
				account[2] -=1
				noteMessageFrame3.configure(text="Remaining attempts: " + str(account[2]))
				connectButtonFrame3.configure(state="normal", cursor=hand)
				showFrame(frame3)
				return

	#user name does not exist
	noteMessageFrame2.configure(text="Username doesn't exist")

#*******************************************************************************************************************#
#Password attempts (Frame 3)
def passwordAttempt():
	global accountIndex

	#remainingAttempts=0 ➡ account is locked
	if accounts[accountIndex][2]==0:
		noteMessageFrame3.configure(text="Account is locked!")
		connectButtonFrame3.configure(state="disabled", cursor="arrow")
		anotherAccountButtonFrame3.configure(text="Use another account")
		return
	
	#password correct ➡ frame 4
	if passwordFrame3.get()==accounts[accountIndex][1]:
		accounts[accountIndex][2]=3	#reset the remainingAttempts (set to 3)
		showFrame(frame4)
		return
	#password incorrect
	else:
		accounts[accountIndex][2]-=1
		noteMessageFrame3.configure(text="Remaining attempts: " + str(accounts[accountIndex][2]))
		if accounts[accountIndex][2]==0:
			noteMessageFrame3.configure(text="Account is locked!")
			connectButtonFrame3.configure(state="disabled", cursor="arrow")
			anotherAccountButtonFrame3.configure(text="Use another account")

#*******************************************************************************************************************#
#account is locked ➡ show option to use another account
def useAnotherAccount():
	connectButtonFrame2.configure(state="normal", cursor=hand)
	showFrame(frame2)

#*******************************************************************************************************************#
#Create a new account (Frame 5)
def create():
	#username or password is missing
	if usernameFrame5.get()=="" or passwordFrame5.get()=="":
		noteMessageFrame5.configure(text="Username or password is missing!")
		return

	#check if user name exists
	usernameUsed = False
	for account in accounts:
	#username exists
		if usernameFrame5.get()==account[0]:
			usernameUsed = True
			noteMessageFrame5.configure(text="Username already exists!")
			return
	#username doesn't exist ➡ create account
	if not usernameUsed:
		accounts.append([usernameFrame5.get(), passwordFrame5.get(), 3])
		noteMessageFrame5.configure(text="Account is successfully created!")

		#go to start page buttom
		goToStartButton = Button(credentials,text="Go to start page",
			command=lambda:{
				showFrame(frame1),
				goToStartButton.grid_remove()},
			bg=turquoiseColor, fg="white", font=(globalFont, 13, "bold"),
			bd=0, highlightthickness=0, activebackground=turquoiseColor, activeforeground= "white", relief="flat", cursor=hand)
		goToStartButton.grid(row=5, columnspan=3, sticky="nsew", ipady=10)	


'''**************************************************************************************************************'''


# MAIN CODE
if __name__ == "__main__":

	#GUI setup
	window = Tk()								# create window
	window.title("App")							# set the title
	window.resizable(False, False)				#non-resizable window
	window.option_add("*Font", globalFont)
	window.bind('<Button>', keep_flat)


#***FRAME 1*********************************************************************************************************#
	#START PAGE
	frame1 = Frame(window)

	#background image
	bgFrame1 = PhotoImage(file = directory_path+"\\frame1_bg.png")
	Label(frame1, image=bgFrame1).grid(row=0, column=0)


	#sign in button
	signInButtonImage = PhotoImage(file = directory_path+"\\frame1_signIn.png")
	signInButtonFrame1 = Button(frame1, image=signInButtonImage, bd=0, highlightthickness=0, relief="flat", cursor=hand,
	command=lambda:showFrame(frame2))
	signInButtonFrame1.place(relx=.5, rely=.62, anchor=CENTER)
	
	#sign up button
	signUpButtonImage = PhotoImage(file = directory_path+"\\frame1_signUp.png")
	signUpButtonFrame1 = Button(frame1, image=signUpButtonImage, bd=0, highlightthickness=0, relief="flat", cursor=hand,
	command=lambda:showFrame(frame5))
	signUpButtonFrame1.place(relx=.5, rely=.71, anchor=CENTER)

	#help button
	helpButtonImage = PhotoImage(file = directory_path+"\\frame1_help.png")
	helpButton = Button(frame1, image=helpButtonImage, bd=0, highlightthickness=0, relief="flat", cursor=hand,
	command=lambda: {
		helpBox.place(relx=0.13, rely=0.15),
		closeHelpButton.place(relx=0.78, rely=0.155)})
	helpButton.place(relx=0.93, rely=0.05, anchor=CENTER)

	helpBoxImage = PhotoImage(file = directory_path+"\\frame1_helpBox.png")
	helpBox = Label(frame1, image=helpBoxImage)

	closeHelpButton = Button(frame1, text="Close",
		bg="#DDF9FC", fg="#75BABD", activeforeground="#75BABD", activebackground="#DDF9FC",
		bd=0, highlightthickness=0, relief="flat", cursor=hand,
		command=lambda: {
			helpBox.place_forget(),
			closeHelpButton.place_forget()})

#***FRAME 2*********************************************************************************************************#
	#SIGN IN  PAGE
	frame2 = Frame(window)
	
	#background image
	bgFrame2 = PhotoImage(file = directory_path+"\\frame2_bg.png")
	Label(frame2, image=bgFrame2).grid(row=0, column=0)

	#username + password frame
	credentials = Frame(frame2)
	credentials.place(relx=0.5, rely=0.48, anchor=CENTER)

	#username label
	Label(credentials, text="username",
		bg=pinkColor, fg=greyColor
		).grid(row=0, column=0, ipadx=5, ipady=5)
	#username entry
	usernameFrame2 = Entry(credentials, selectbackground=turquoiseColor, bd=0)
	usernameFrame2.grid(row=0, column=2, ipady=7)

	#password label
	Label(credentials, text="password",
		bg=pinkColor, fg=greyColor
		).grid(row=2, column=0, ipadx=5, ipady=5)
	#password entry
	passwordFrame2 = Entry(credentials, show="•", selectbackground=turquoiseColor, bd=0)
	passwordFrame2.grid(row=2, column=2, ipady=7)

	#connect to account buttom
	
	connectButtonFrame2 = Button(credentials,text="Connect", bg=boldPinkColor, fg="white", font=(globalFont, 13, "bold"),
		bd=0, highlightthickness=0, activebackground=boldPinkColor, activeforeground= "white", relief="flat", cursor=hand,
		command=connect)
	connectButtonFrame2.grid(row=5, columnspan=3, sticky="nsew", ipady=10)
	
	#note message
	noteMessageFrame2 = Label(credentials,text="",
	bg=pinkColor, fg="red4", font=(globalFont, 10),)
	noteMessageFrame2.grid(row=4, columnspan=3, sticky="nsew", ipady=10)

	#spacing
	Label(credentials, text="", bg=pinkColor).grid(row=1, columnspan=3, ipadx=131)
	Label(credentials, text="", bg=pinkColor).grid(row=3, columnspan=3, ipadx=131, ipady=10)
	
	#use another account button
	anotherAccountButtonFrame2 = Button(frame2, text="",
		bg=pinkColor, fg=greyColor, font=(globalFont, 11),
		bd=0, highlightthickness=0, activebackground=pinkColor, activeforeground= turquoiseColor, relief="flat", cursor=hand,
		command=useAnotherAccount)
	anotherAccountButtonFrame2.place(relx=.5, rely=.7, anchor=CENTER)

	#sign up button
	signUpButtonFrame2 = Button(frame2, text="Don't have an account?",
		bg=pinkColor, fg=turquoiseColor, font=(globalFont, 11),
		bd=0, highlightthickness=0, activebackground=pinkColor, activeforeground= turquoiseColor, relief="flat", cursor=hand,
		command=lambda:showFrame(frame5))
	signUpButtonFrame2.place(relx=.5, rely=.75, anchor=CENTER)



#***FRAME 3*********************************************************************************************************#
	#INCORRECT PASSWORD PAGE
	frame3 = Frame(window)
	
	#background image
	bgFrame3 = PhotoImage(file = directory_path+"\\frame2_bg.png")
	Label(frame3, image=bgFrame3).grid(row=0, column=0)

	#username + password frame
	credentials = Frame(frame3)
	credentials.place(relx=0.5, rely=0.48, anchor=CENTER)

	#username label
	usernameLabel = Label(credentials,
		bg=pinkColor, fg=greyColor)
	usernameLabel.grid(row=0, columnspan=3, sticky="nsew", ipady=5)
	Label(credentials, text="Please insert the correct password to log in",
		bg=pinkColor, fg=greyColor, font=(globalFont, 9),
		).grid(row=1, columnspan=3, sticky="nsew", ipady=5)

	#password label
	Label(credentials, text="password",
		bg=pinkColor, fg=greyColor
		).grid(row=3, column=0, ipadx=5, ipady=5)
	#password entry
	passwordFrame3 = Entry(credentials, show="•", bd=0)
	passwordFrame3.grid(row=3, column=2, ipady=7)

	#note message
	noteMessageFrame3 = Label(credentials,text="Remaining attempts: ",
	bg=pinkColor, fg="red4", font=(globalFont, 10),)
	noteMessageFrame3.grid(row=5, columnspan=3, sticky="nsew", ipady=10)

	#connect to account buttom
	connectButtonFrame3 = Button(credentials,text="Connect", bg=boldPinkColor, fg="white", font=(globalFont, 13, "bold"),
		bd=0, highlightthickness=0, activebackground=boldPinkColor, activeforeground= "white", relief="flat", cursor=hand,
		command=passwordAttempt)
	connectButtonFrame3.grid(row=6, columnspan=3, sticky="nsew", ipady=10)

	#spacing
	Label(credentials, text="", bg=pinkColor).grid(row=2, columnspan=3, ipadx=131)
	Label(credentials, text="", bg=pinkColor).grid(row=4, columnspan=3, ipadx=131, ipady=10)

	#use another account button
	anotherAccountButtonFrame3 = Button(frame3, text="",
		bg=pinkColor, fg=greyColor, font=(globalFont, 11),
		bd=0, highlightthickness=0, activebackground=pinkColor, activeforeground= turquoiseColor, relief="flat", cursor=hand,
		command=useAnotherAccount)
	anotherAccountButtonFrame3.place(relx=.5, rely=.7, anchor=CENTER)

	#sign up button
	signUpButtonFrame3 = Button(frame3, text="Don't have an account?",
		bg=pinkColor, fg=turquoiseColor, font=(globalFont, 11),
		bd=0, highlightthickness=0, activebackground=pinkColor, activeforeground= turquoiseColor, relief="flat", cursor=hand,
		command=lambda:showFrame(frame5))
	signUpButtonFrame3.place(relx=.5, rely=.75, anchor=CENTER)

#***FRAME 4*********************************************************************************************************#
	#WELCOME PAGE
	frame4 = Frame(window)

	#background image
	bgFrame4 = PhotoImage(file = directory_path+"\\frame4_bg.png")
	Label(frame4, image=bgFrame4).grid(row=0, column=0)

	#log out button
	logOutButtonImage = PhotoImage(file = directory_path+"\\frame1_signIn.png")
	logOutButtonImage = Button(frame4, text="Log out",
		bg = turquoiseColor, fg="white", font=(globalFont, 10, "bold"), padx=5, pady=5,
		bd=0, highlightthickness=0, relief="flat", cursor=hand,
		command=lambda:showFrame(frame1))
	logOutButtonImage.place(relx=.09, rely=.05, anchor=CENTER)


#***FRAME 5*********************************************************************************************************#
	#SIGN UP PAGE
	frame5 = Frame(window)

	#background image
	bgFrame5 = PhotoImage(file = directory_path+"\\frame5_bg.png")
	Label(frame5, image=bgFrame5).grid(row=0, column=0)

	#username + password frame
	credentials = Frame(frame5)
	credentials.place(relx=0.5, rely=0.48, anchor=CENTER)

	#username label
	Label(credentials, text="username",
		bg=blueColor, fg=greyColor
		).grid(row=0, column=0, ipadx=5, ipady=5)
	#username entry
	usernameFrame5 = Entry(credentials, selectbackground=turquoiseColor, bd=0)
	usernameFrame5.grid(row=0, column=2, ipady=7)

	#password label
	Label(credentials, text="password",
		bg=blueColor, fg=greyColor
		).grid(row=2, column=0, ipadx=5, ipady=5)
	#password entry
	passwordFrame5 = Entry(credentials, show="•", selectbackground=turquoiseColor, bd=0)
	passwordFrame5.grid(row=2, column=2, ipady=7)

	#create account buttom
	Button(credentials,text="Create", command=create,
		bg=turquoiseColor, fg="white", font=(globalFont, 13, "bold"),
		bd=0, highlightthickness=0, activebackground=turquoiseColor, activeforeground= "white", relief="flat", cursor=hand
		).grid(row=5, columnspan=3, sticky="nsew", ipady=10)

	#note message
	noteMessageFrame5 = Label(credentials,text="",
	bg=blueColor, fg="red4", font=(globalFont, 10),)
	noteMessageFrame5.grid(row=4, columnspan=3, sticky="nsew", ipady=10)

	#spacing
	Label(credentials, text="", bg=blueColor).grid(row=1, columnspan=3, ipadx=131)
	Label(credentials, text="", bg=blueColor).grid(row=3, columnspan=3, ipadx=131, ipady=10)

	#sign in button
	signUpButtonFrame5 = Button(frame5, text="I already have an account",
		bg=blueColor, fg=boldPinkColor, font=(globalFont, 11),
		bd=0, highlightthickness=0, activebackground=blueColor, activeforeground= turquoiseColor, relief="flat", cursor=hand,
		command=lambda:showFrame(frame2))
	signUpButtonFrame5.place(relx=.5, rely=.75, anchor=CENTER)



#******************************************************************************************************************#
	#add all frames to window
	for frame in (frame1, frame2, frame3, frame4, frame5):
		frame.grid(row=0, column=0)
	
	#show frame1
	showFrame(frame1)


#******************************************************************************************************************#

# start the GUI
	window.mainloop()
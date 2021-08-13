import sys, os, shutil, time, subprocess
from contextlib import contextmanager
try:
    import gpt_2_simple as gpt2
except:
    pass
    proc = subprocess.Popen('pip freeze', shell=True, stdout=subprocess.PIPE)
    output = str(proc.communicate()[0])
    if 'gpt-2-simple' in output:
        print('You are running on a newer version of tensorflow. For this script to work, you must be running on tensorflow version 1.15.2. Please install this tensorflow version before running this program again.\n\nTIP: You will need to build tensorflow 1.15.2 from source to use it.')
        quit()
    else:
        inss = input('You are missing a required dependency. Would you like to install it now? (y/n): ')
        if inss.lower() == 'y':
            os.system('pip install gpt_2_simple')
            try:
                import gpt_2_simple as gpt2
            except:
                print('You are running on a newer version of tensorflow. For this script to work, you must be running on tensorflow version 1.15.2. Please install this tensorflow version before running this program again.\n\nTIP: You will need to build tensorflow 1.15.2 from source to use it.')
        elif inss.lower() == 'n':
            print('Please install the dependency with "pip install gpt_2_simple" before running this program again.')
        else:
            print('Invalid response.')
try:
    import pyttsx3
except:
    pass
    inss = input('You are missing a required dependency. Would you like to install it now? (y/n): ')
    if inss.lower() == 'y':
        os.system('pip install pyttsx3')
        import pyttsx3
    elif inss.lower() == 'n':
        print('Please install the dependency with "pip install pyttsx3" before running this program again.')
    else:
        print('Invalid response.')
@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
clearConsole()
engine = pyttsx3.init()
directory_path = os.getcwd()
if not os.path.exists(os.path.join(directory_path, 'novaSetup.txt')):
    print("Nova First Time Setup\n")
    print("Nova: Hello, my name is Nova and I am a chatbot that runs on GPT-2, nice to meet you!")
    temp = input("Nova: Before we begin, you need to choose what version of GPT-2 to run. There are 2 options, small, large and super large. Small uses less storage spcce but is worse at gneerating responses in conversations. Large uses over 1GB of space but is better at generating responses in conversations. Super Large uses lots of storage space but is the best at generating responses in conversations. Choose now (type 's' for small, 'l' for large and 'sl' for super large): ")
    if temp == 'l' or 'L':
        model_name = '355M'
        print('Nova: OK! Give me a second, this should only take a few minutes depending on your connection.')
        stat = str(shutil.disk_usage("/")).split(",")[2].split("=")[1].replace(")","")
        avail = int(stat) / 1000000
        if avail < 1600:
            print("Nova: You do not have enough storage space for the files, shutting down...")
            quit()
        else:
            with suppress_stdout():
                gpt2.download_gpt2(model_name=model_name)
            print('Nova: Files downloaded')
    elif temp == 's' or 'S':
        model_name = '124M'
        print('Nova: OK! Give me a second, this should only take a few minutes depending on your connection.')
        stat = str(shutil.disk_usage("/")).split(",")[2].split("=")[1].replace(")","")
        avail = int(stat) / 1000000
        if avail < 600:
            print("Nova: You do not have enough storage space for the files, shutting down...")
            quit()
        else:
            with suppress_stdout():
                gpt2.download_gpt2(model_name=model_name)
            print('Nova: Files downloaded')
    elif temp.lower() == 'sl':
        model_name = '774M'
        print('Nova: OK! Give me a second, this should only take a few minutes depending on your connection.')
        stat = str(shutil.disk_usage("/")).split(",")[2].split("=")[1].replace(")","")
        avail = int(stat) / 1000000
        if avail < 3200:
            print("Nova: You do not have enough storage space for the files, shutting down...")
            quit()
        else:
            with suppress_stdout():
                gpt2.download_gpt2(model_name=model_name)
            print('Nova: Files downloaded')
    else:
        print('Nova: Shutting down now, goodbye!')
        time.sleep(1)
        quit()
    fm = open('novaSetup.txt', 'w')
    fm.write(model_name)
    fm.close()
mod = open('novaSetup.txt','r')
model_name = mod.read()
mod.close()
clearConsole()
print('Initialising GPT-2, this could take some time...')
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, model_name=model_name)
print('Done!')
time.sleep(1.5)
clearConsole()
if not os.path.exists(os.path.join(directory_path, 'humanInfo.txt')):
    print('Welcome to Nova')
    time.sleep(1)
    print("\nNova: Hello! My name is Nova, I am a chatbot that runs on GPT-2, nice to meet you!\nNova: To start, what is your name?")
    human_name = input("Human: ")
    print("Nova: Hello " + human_name + "!\nNova: What are your pronouns? (example: if you use female pronouns, type 'she/her')")
    human_pronouns = input('Human: ')
    print("Nova: Ok, I will make sure to refer to you by " + human_pronouns + ' pronouns!\nNova: Next, how old are you?')
    human_age = input('Human: ')
    print('Nova: Finally, which city/town do you live in?')
    human_city = input('Human: ')
    print("Nova: Great! Let's begin chatting!")
    humanInfo = "Human Name: " + human_name + '\nHuman Age: ' + human_name + '\nHuman Pronouns: ' + human_pronouns + '\nHuman City: ' + human_city
    human = open('humanInfo.txt','w')
    human.write(humanInfo)
    human.close()
hu = open('humanInfo.txt','r')
humanInfo = hu.read()
hu.close()
time.sleep(2)
def menu():
    clearConsole()
    print('Welcome to Nova\n\nMenu\nOptions for conversation are listed below, type the number that corresponds with the option you want for a conversation with Nova.\n\n1. General Conversation\n2. Conversation About Hometown\n3. Conversation About Books\n4. Jokes\n5. Copy Mode\n6. Quit Nova')
    option = int(input(''))
    return option
def endNova():
    print('Nova has been shutdown, thanks for using Nova!\n\nNova by jack-debug. Version 1.0.0')
    quit()
def generalConv():
    clearConsole()
    print('Enter "quit" to exit chat and return to menu.\n\nNOTE: Nova can take some time to generate answers based on the speed of the machine running Nova. I apologise if Nova takes a while to generate answers.')
    time.sleep(4)
    clearConsole()
    ongoing = True
    humanAnswer = input('Human: ')
    conv = 'Nova Chatbot Conversation\n\nNova is a chatbot that can have conversations with humans.\n\nConversation Topic: General Conversation\n' + humanInfo + '\nNova Name: Nova\nNova Pronouns: they/them\n\nConversation between Nova and a human:\nHuman: ' + humanAnswer + '\nNova:'
    while ongoing == True:
        try:
            novaResp = gpt2.generate(sess, model_name=model_name, length=50, temperature=0.7, prefix=conv, nsamples=1, batch_size=1, return_as_list=True)[0].replace(conv,'').split('\n')[0]
        except:
            pass
            print('An error occurred, sorry for the inconvenience, returing to main menu')
            time.sleep(5)
            openMenu()
        print('Nova:' + novaResp)
        engine.say(novaResp)
        engine.runAndWait()
        conv = conv + novaResp + '\n'
        humanResp = input('Human: ')
        if humanResp == 'quit':
            print('Quitting conversation...')
            openMenu()
        conv = conv + 'Human: ' + humanResp + '\nNova:'
def hometownConv():
    clearConsole()
    print('Enter "quit" to exit chat and return to menu.\n\nNOTE: Nova can take some time to generate answers based on the speed of the machine running Nova. I apologise if Nova takes a while to generate answers.')
    time.sleep(4)
    clearConsole()
    ongoing = True
    humanAnswer = input('Human: ')
    conv = 'Nova Chatbot Conversation\n\nNova is a chatbot that can have conversations with humans.\n\nConversation Topic: Humans Hometown\n' + humanInfo + '\nNova Name: Nova\nNova Pronouns: they/them\n\nConversation between Nova and a human:\nHuman: ' + humanAnswer + '\nNova:'
    while ongoing == True:
        try:
            novaResp = gpt2.generate(sess, model_name=model_name, length=50, temperature=0.7, prefix=conv, nsamples=1, batch_size=1, return_as_list=True)[0].replace(conv,'').split('\n')[0]
        except:
            pass
            print('An error occurred, sorry for the inconvenience, returing to main menu')
            time.sleep(5)
            openMenu()
        print('Nova:' + novaResp)
        engine.say(novaResp)
        engine.runAndWait()
        conv = conv + novaResp + '\n'
        humanResp = input('Human: ')
        if humanResp == 'quit':
            print('Quitting conversation...')
            openMenu()
        conv = conv + 'Human: ' + humanResp + '\nNova:'
def bookConv():
    clearConsole()
    print('Enter "quit" to exit chat and return to menu.\n\nNOTE: Nova can take some time to generate answers based on the speed of the machine running Nova. I apologise if Nova takes a while to generate answers.')
    time.sleep(4)
    clearConsole()
    ongoing = True
    humanAnswer = input('Human: ')
    conv = 'Nova Chatbot Conversation\n\nNova is a chatbot that can have conversations with humans.\n\nConversation Topic: Books\n' + humanInfo + '\nNova Name: Nova\nNova Pronouns: they/them\n\nConversation between Nova and a human:\nHuman: ' + humanAnswer + '\nNova:'
    while ongoing == True:
        try:
            novaResp = gpt2.generate(sess, model_name=model_name, length=50, temperature=0.7, prefix=conv, nsamples=1, batch_size=1, return_as_list=True)[0].replace(conv,'').split('\n')[0]
        except:
            pass
            print('An error occurred, sorry for the inconvenience, returing to main menu')
            time.sleep(5)
            openMenu()
        print('Nova:' + novaResp)
        engine.say(novaResp)
        engine.runAndWait()
        conv = conv + novaResp + '\n'
        humanResp = input('Human: ')
        if humanResp == 'quit':
            print('Quitting conversation...')
            openMenu()
        conv = conv + 'Human: ' + humanResp + '\nNova:'
def jokeConv():
    clearConsole()
    print('Enter "quit" to exit chat and return to menu.\n\nNOTE: Nova can take some time to generate answers based on the speed of the machine running Nova. I apologise if Nova takes a while to generate answers.')
    time.sleep(4)
    clearConsole()
    ongoing = True
    humanAnswer = input('Human: ')
    conv = 'Nova Chatbot Conversation\n\nNova is a chatbot that can have conversations with humans.\n\nConversation Topic: Jokes\n' + humanInfo + '\nNova Name: Nova\nNova Pronouns: they/them\n\nConversation between Nova and a human:\nHuman: ' + humanAnswer + '\nNova:'
    while ongoing == True:
        try:
            novaResp = gpt2.generate(sess, model_name=model_name, length=50, temperature=0.7, prefix=conv, nsamples=1, batch_size=1, return_as_list=True)[0].replace(conv,'').split('\n')[0]
        except:
            pass
            print('An error occurred, sorry for the inconvenience, returing to main menu')
            time.sleep(5)
            openMenu()
        print('Nova:' + novaResp)
        engine.say(novaResp)
        engine.runAndWait()
        conv = conv + novaResp + '\n'
        humanResp = input('Human: ')
        if humanResp == 'quit':
            print('Quitting conversation...')
            openMenu()
        conv = conv + 'Human: ' + humanResp + '\nNova:'
def copyConv():
    clearConsole()
    print('Enter "quit" to exit chat and return to menu.')
    time.sleep(2)
    clearConsole()
    ongoing = True
    while ongoing == True:
        hum = input('Human: ')
        if hum == 'quit':
            print('Quitting conversation...')
            openMenu()
        print('Nova: ' + hum)
        engine.say(hum)
        engine.runAndWait()
def openMenu():
    clearConsole()
    opt = menu()
    if opt == 1:
        generalConv()
    elif opt == 2:
        hometownConv()
    elif opt == 3:
        bookConv()
    elif opt == 4:
        jokeConv()
    elif opt == 5:
        copyConv()
    elif opt == 6:
        endNova()
openMenu()
#shutil.rmtree(os.path.join("models", "124M")) ## for when convo is done
# gpt2.generate(sess, model_name=model_name, length=50, temperature=0.7, prefix="Nova: ", nsamples=1, batch_size=1, return_as_list=True)[0]
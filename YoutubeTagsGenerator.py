# Do not touch anything beyond this line unless you know what you're doing.
import random
import string
import os
from colorama import Fore, init
init()

print((Fore.RED + """

 __     __      _______    _            _______                 _____                           _             
 \ \   / /     |__   __|  | |          |__   __|               / ____|                         | |            
  \ \_/ /__  _   _| |_   _| |__   ___     | | __ _  __ _ ___  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
   \   / _ \| | | | | | | | '_ \ / _ \    | |/ _` |/ _` / __| | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
    | | (_) | |_| | | |_| | |_) |  __/    | | (_| | (_| \__ \ | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
    |_|\___/ \__,_|_|\__,_|_.__/ \___|    |_|\__,_|\__, |___/  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                    __/ |                                                     
                                                   |___/                                                      
"""))
print(Fore.LIGHTBLACK_EX + 'Made by Nicuse#6163' + Fore.LIGHTRED_EX)
topics = input('Enter video topics (separate with commas): ')
topics = topics.split(',')
keywords = input('Enter keywords (separate with commas): ')
keywords = keywords.split(',')
type = input('Enter type ("hashtags" or "tags"): ')
if type.lower() == 'tags':
    type = False
else:
    type = True
outputForm = input('Output type (txt, printlist, print): ')
generateAmount = int(input('Enter amount to generate: '))
removeDuplicateTags = input('Remove duplicate tags? (Yes or No): ')
if removeDuplicateTags.lower() == 'yes':
    removeDuplicateTags = True
else:
    removeDuplicateTags = False
def generateKeyword(amount):
    return_table = []
    for i in range(amount):
        return_table.append(random.sample(keywords, 1)[0])
    return ' '.join(return_table)

def generateTopic(): return random.choice(topics)

def generateTag(): return ''.join(f'{generateTopic()} {generateKeyword(1)}')

def generateHashtag():
    ok = f'#{generateTopic()}{generateKeyword(1)}'
    ok = ''.join([i for i in ok if i != ' '])
    return ok

def generateRS(l):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=l))


generated = []
for i in range(generateAmount):
    if type == True:
        generated.append(generateHashtag())
        for i in topics:
            generated.insert(0, f'#{i}')
    else:
        generated.append(generateTag())
        for i in topics:
            generated.insert(0, i)
if removeDuplicateTags:
    generated = [i for v,i in enumerate(generated) if i not in generated[:v]]

if outputForm == 'txt':
    with open(f'{generateRS(5)}_Gen.txt', 'w') as f:
        f.write('Here you go!')
        for i in generated:
            f.write(f'\n\n{i},')
        f.close()
elif outputForm == 'printlist':
    print(generated)
else:
    for i in generated:
        print(f'{i},')

if type == True:
    print(f'\nGenerated {len(generated)} hashtags.')
else:
    print(f'\nGenerated {len(generated)} tags.')

characters = []
for i in generated:
    characters.append(len(i))

characters = sum(characters)
if type == False and characters > 500:
    print("WARNING: There is a limit of 500 characters. YouTube won't allow adding more tags if it exceeds the limit.")

os.system('pause >nul') #(press any key to exit the code)

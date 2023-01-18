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
for i, v in enumerate(keywords):
    keywords[i] = v.strip()
for i, v in enumerate(topics):
    topics[i] = v.strip()
while True:
    type = input('Enter type ("hashtags" or "tags"): ')
    if type in ['hashtags', 'tags']:
        break
    print('[!] Error occurred: Please enter "hashtags" or "tags"')
if type.lower() == 'tags':
    type = False
else:
    type = True
while True:
    outputForm = input('Output type (txt, printlist, print): ')
    if outputForm in ['txt', 'printlist', 'print']:
        break
    print(f'[!] Error occurred: Please enter the avaliable options. (txt, printlist, print)')

while True:
    try:
        generateAmount = int(input('Enter amount to generate: '))
        break
    except ValueError:
        print(f'[!] Error occurred: Please enter a valid integer value.')
while True:
    removeDuplicateTags = input('Remove duplicate tags? (Yes or No): ').lower()
    if removeDuplicateTags in ['yes', 'no']:
        break
    print('[!] Error occurred: Please enter "Yes" or "No"')
if removeDuplicateTags.lower() == 'yes':
    removeDuplicateTags = True
    print(Fore.LIGHTBLACK_EX + 'The tags generated will be decreased due to "remove duplicate tags"' + Fore.LIGHTRED_EX)
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

if type == True:
    generated = [v.replace(" ", "") for v in generated]

fName = f'{generateRS(5)}_Gen.txt'
file_path = os.path.join(os.getcwd(), fName)

if outputForm == 'txt':
    with open(file_path, 'w') as f:
        f.write('Here you go!')
        for i in generated:
            f.write(f'\n\n{i},')
        f.close()
    print(f'\nFile generated with name "{fName}" in {file_path}')
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

import random
import time
import os
from datetime import datetime

if __name__ == '__main__':

    while True:

        input_path = './input/'
        files = os.listdir(input_path)
        if len(files) == 0:
            print('No files')
            input()
            exit()
        selected = ''
        while True:
            print('0 : Quit')
            for i, file_name in enumerate(files):
                print('['+str(i+1)+']:', file_name)
            num = input('Select file number: ')
            if num == '0':
                print('Bye')
                input()
                exit()

            if '0'<num<=str(len(files)):
                selected = files[int(num) - 1]
                extension = selected.split('.')[1]
                if extension == 'txt':
                    os.system('cls')
                    break
                print('not supported file')
                input()
            os.system('cls')


        f = open(input_path + selected, 'r', encoding='UTF-8')
        people = list(map(lambda x: x.rstrip(), f.readlines()))
        f.close()

        theory = selected.split('.')[0]
        today = datetime.today().strftime("%Y-%m-%d")
        now = datetime.today().strftime("%H:%M:%S")

        done = []
        confused = []
        person = ""

        shape = ['?', '_', '/', 'x', '*', 'w', '?']
        while True:
            print("0: Quit 1: Get Random")
            sel = input()
            if sel == '0':
                break
            elif sel == '1':
                for s in shape:
                    print('\r'+s, end='')
                    time.sleep(0.3)
                print('\r', end='')
                person = random.choice(people)
                print('->', person)
            else:
                print('Wrong Number')
                input()
                os.system('cls')
                continue

            sel2 = input()
            if sel2 == 'done':
                people.remove(person)
                done.append(person)

                d = open(os.getcwd() + '\\output\\' + theory + '_done_' + today + '.txt', 'a')
                d.write(person+'\n')
                d.close()
            elif sel2 == 'not':
                confused.append(person)
                people.remove(person)

                c = open(os.getcwd() + '\\output\\' + theory + '_not_' + today + '.txt', 'a')
                c.write(person + '\n')
                c.close()
            else:
                pass
            if not people:
                os.system('cls')
                print('Good Job!')
                break

            os.system('cls')

        os.system('cls')
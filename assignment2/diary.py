response = input("What happened today? ")
while response is not "done for now":
    with open('diary.txt', 'a') as file:
        file.write(f'{response} \n')

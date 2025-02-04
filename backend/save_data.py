def logData(data):
    # opens the right file
    with open("userData.txt", "w") as dataBase:
        # print all of the data nicely
        for i in range(len(data)):
            to_write = data[i].to_json()
            dataBase.write(f'user {i+1}:\n')
            dataBase.write(f'{to_write["userName"]}\n')
            dataBase.write(f'{to_write["password"]}\n')
            dataBase.write(f'{to_write["age"]}\n')
            dataBase.write(f'{to_write["gender"]}\n\n\n')

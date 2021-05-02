
dictionary = {"멋사": "멋쟁이 사자처럼", "파이썬": "지금 배우는 언어"}
def create_word():
    n = input('world : ')
    k = input('meaning : ')
    dictionary[n] = k
    print('성공')
def read_dictionary():
    for key, value in dictionary.items():
        print(key, value)
def update_word():
    n = input('Enter word: ')
    if not n in dictionary:
        print('실패')
    else:
        k1 = input('Enter meaning: ')
        dictionary[n] = k1
        print("success")


def delete_word():
    n = input('Enter word: ')
    if not n in dictionary:
     print('실패')
    else:
        del dictionary[n] 
        print('success')





def console_help():
    print("Command list")
    print("---")
    print("C for create")
    print("R for read")
    print("U for update")
    print("D for delete")
    print("Q for quit")
def receive_input():
    command = input("Input command: ")
    if command == 'c' or command == 'C':
        create_word()
        return True
    if command == 'r' or command == 'R':
        read_dictionary()
        return True
    if command == 'u' or command == 'U':
        update_word()
        return True
    if command == 'd' or command == 'D':
        delete_word()
        return True
    if command == 'q' or command == 'Q':
        return False
    else:
        print("Please enter one of the letters above.")
        return True
def main():
    console_help()
    while receive_input():
        pass
if __name__ == "__main__":
    main()


# Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок за допомоги декораторів.

# Вимоги до завдання:
# Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. 
# Цей декоратор відповідає за повернення користувачеві повідомлень типу "Enter user name", "Give me name and phone please" тощо.
# Декоратор input_error повинен обробляти винятки, що виникають у функціях - handler і це винятки: 
# KeyError, ValueError, IndexError. Коли відбувається виняток декоратор повинен повертати відповідну відповідь користувачеві. 
# Виконання програми при цьому не припиняється.

from collections.abc import Callable

phone_book = {}

def input_error(func:Callable):                         #define decorator
    def inner(*args,**kwargs):                          #inner function wich catch exceprions
        try:                                            #try execute decorated function
            return func(*args,**kwargs)                 #return result of execution
        except KeyError:                                
            return "Invalid command"
        except ValueError:
            return "Wrong command format"
        except IndexError:
            return "Contact not exist" 
    return inner                                        #return inner function

@input_error                                            #use decorator
def add_contact(data:list) -> str:                      #define function for add contact
    name, number = data                                 #unpack data
    phone_book[name] = number                           #add record to dictionary
    return "Record added."                              #return confirm 

@input_error                                            #use decorator
def change_contact(data:list) -> str:                   #define function for change contact
    name, number = data                                 #unpack data
    if not phone_book.get(name):                        #if record not exist 
        raise IndexError()                              #rise exception
    phone_book[name] = number                           #update dictionary
    return "Contact updated"                            #return confirm 

@input_error                                            #use decorator
def show_phone(data:list) ->str:                        #define function for show number
    name, *_ = data                                     #unpack data
    return phone_book[name]                             #try return phone by given name

def show_all():                                         #define function for show all phone book
    for name, phone in phone_book.items():              #each record display
        print(f"{name:<30}{phone:>15}")                 #with format 

@input_error                                            #use decorator
def parse_input(user_input:str) -> list:                #define function to parse command
    user_input = user_input.lower().strip().split()     #split input string by " "
    return (user_input.pop(0), user_input)              #return command and left data


def main():                                             #define main function
    print("Welcome to the assistant bot!")              #greeting
    while True:                                         #start unlimit cycle
        get_command, data = parse_input(input("Enter a command: ")) #parse data from user
        match get_command:                              #select action for entered command
            case ("exit"|"close"):                      #terminate cycle 
                print("Good bye!")
                break
            case ("hello"):                             #communicate with user
                print("How can I help you?")
            case ("add"):                               #add contact
                print(add_contact(data))
            case ("change"):                            #change contact
                print(change_contact(data))
            case ("phone"):                             #show phone by name
                print(show_phone(data))
            case ("all"):                               #show all phone book
                show_all()
            case (_):                                   #unknown command
                print("Invalid command")

main()                                                  #run code
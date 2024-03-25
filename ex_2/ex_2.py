# Необхідно створити функцію generator_numbers, яка буде аналізувати текст, 
# ідентифікувати всі дійсні числа, що вважаються частинами доходів, і повертати їх як генератор. 
# Дійсні числа у тексті записані без помилок, чітко відокремлені пробілами з обох боків. 
# Також потрібно реалізувати функцію sum_profit, 
# яка буде використовувати generator_numbers для підсумовування цих чисел і обчислення загального прибутку.

# Вимоги до завдання:
# Функція generator_numbers(text: str) повинна приймати рядок як аргумент і повертати генератор, 
# що ітерує по всіх дійсних числах у тексті. 
# Дійсні числа у тексті вважаються записаними без помилок і чітко відокремлені пробілами з обох боків.
# Функція sum_profit(text: str, func: Callable) має використовувати генератор generator_numbers 
# для обчислення загальної суми чисел у вхідному рядку та приймати його як аргумент при виклику.

from collections.abc import Callable                                        #import Callable for sintax?
import re                                                                   #import regular expressions
 
def generator_numbers(text: str):                                           #define Generator
    regex_num = "\s[0-9]{1,}[\.|,]?[0-9]{0,}\s"                             #pattern for any numbers with both side spaces
    numbers = [float(w) for w in re.findall(regex_num,text)]                #split text by words and convert to float elements, wich mach regexp
    for num in numbers:                                                     #for each number 
        yield num                                                           #return number

def sum_profit(text: str, func: Callable) -> float:                         #define function
    sum = 0                                                                 #set sum to 0
    for el in func(text):                                                   #for each element in generator 
        sum += el                                                           #add to sum
    return sum                                                              #return sum

def main():                                                                 #define main function
    text = """Загальний дохід працівника складається з декількох частин: 
              1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."""
    print(f"Загальний дохід: {sum_profit(text,generator_numbers)}")         #print result of work

main()                                                                      #run code
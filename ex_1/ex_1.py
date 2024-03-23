# Реалізуйте функцію caching_fibonacci, 
# яка створює та використовує кеш для зберігання і повторного використання вже обчислених значень чисел Фібоначчі.

# Вимоги до завдання:
# Функція caching_fibonacci() повинна повертати внутрішню функцію fibonacci(n).
# fibonacci(n) обчислює n-те число Фібоначчі. Якщо число вже знаходиться у кеші, функція має повертати значення з кешу.
# Якщо число не знаходиться у кеші, функція має обчислити його, зберегти у кеш та повернути результат.
# Використання рекурсії для обчислення чисел Фібоначчі.

from collections.abc import Callable

def caching_fibonacci() -> Callable[[int],int]:             #function for lock cache
    cache = {}                                              #empty dict for cache
    def fibonacci(number_for_fibo:int) -> int:              #define fibonacci function
        if cache.get(number_for_fibo) == None:              #check if cache exist
            if number_for_fibo < 0:                         #if negative number enter - return 0
                return 0                                    
            if number_for_fibo < 2:                         #if enter 0 or 1
                cache[number_for_fibo] = number_for_fibo    #add to cache 0 or 1
            else:                                           #else calculate value and add to cache
                cache[number_for_fibo] = fibonacci(number_for_fibo-1) + fibonacci(number_for_fibo-2)
        return cache.get(number_for_fibo)                   #return value from cache
    return fibonacci                                        #return inner function to provide locking

def main():                                                 #define main function   
    fibo = caching_fibonacci()                              #set fibo to use locking functionality                       

main()                                                      #run code

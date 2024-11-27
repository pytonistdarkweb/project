# class Point3D:
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
        
# pipu = Point3D(3,4,5)
# pipa = Point3D(3,4,5)
# pipo = Point3D(3,4,5)


# print(pipu.x)

#------1
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = 5

# filtred_numbers = [i for i in a if i < b]
# print(filtred_numbers) 

#------2
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


# result = list(filter(lambda elem: elem in b, a))


# print(result)


# import time 
# from threading import Thread


# def clock(delay):
#     time.sleep(delay)
#     print(f"Current time: {time.strftime('%X')}, delay {delay}")
    
    
    
    
# treade1 = Thread (target=clock, args=(2,))
    
# treade2 = Thread (target=clock, args=(3,))




# if __name__ == '__main__':
#     start = time.time()
#     print(f"Time start: {time.strftime('%X')}")
#     clock(5)
#     treade1.start()
#     treade2.start()
#     print(f"Time end: {time.strftime('%X')}")
#     print(f"======== Total time: {time.time() - start:0.2f} ========")



# x = 5
# y = 10
# print(y > x * x or y >= 2 * x and x < y)


# print((a and b) or (not a )and (not b))
# a = True
# b = False
# class Students:  #объявляем класс 
    
    
#     count = 0 #переменная со значением 0 объявляется внутри класса 
    
    
    
#     def __init__(self,name,mark): #конструктор методов  используется в этой функции 
#         self.name = name 
#         self.mark = mark 
#         Students.count += 1 # с каждым добавлением добавляется и колличество 
    
    
    
#     def counter(self): 
#         print('Всего студентов {}'.format(Students.count) ) 
    
    
    
#     def students_cl(self): 
#         print('Имя:{}, Отметка: {}'.format(self.name,self.mark))



# st1 = Students("Тимур", 5) 
# st2 = Students("Антон", 3) 
# st1.students_cl() 
# st2.students_cl() 




# number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]


# for number_even in number:
#     if number_even % 2 == 0:
#         print(number_even)
 
 
class GREET_CLASS:
    def greet(self,hello):
        self.hello = hello 
        return hello
        
        
st1 = GREET_CLASS()



print(st1.greet('hello world!'))
    
    
    

        
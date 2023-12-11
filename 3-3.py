#                 01
""" 
String.upper() – აბრუნებს სტრიქონს დიდი ასოებით
String.lower() – აბრუნებს სტრიქონს პატარა ასოებით
String.count() – განსაზღვრავს სტრიქონში ქვესტრინგის არსებობის რაოდენობას
String.find() – აბრუნებს პირველი ნაპოვნი სიმბოლოს ინდექსს
String.replace() – ცვლის მითითებულ ქვესტრინგს ახალი ფრაგმენტით
String.split() – ყოფს სტრიქონს ქვესტრიქონებად
String.join() – აერთიანებს კოლექციას სტრიქონში
"""



'''                 02                 '''
a = input()
print(a.capitalize())


'''                 03                 '''
x = input()
print(x.count("-"))


'''                 04                 '''
#              Error


'''                 05                 '''
-1


'''                 06                 '''
y = input()
print(y.find("ra"))


'''                 07                '''
x = input()
print("-".join(x.split("--")))


'''                 08                '''
c = input()
print(c.rjust(3, "0"))


'''                 09                '''
x=  input()
print(len(x.split()))



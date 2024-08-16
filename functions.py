'''
length = int(input("enter length"))
width = int(input("enter width"))
height= int(input("enter height"))

def prism_vol(a, b, c):
   return a * b * c

print("the voluem of prism is " + str(prism_vol(length, width, height)) + "cubit ft")

celsius = int(input("enter an integer value of degree celsius"))

def farenheit(celsius):
   return(1.8 * celsius + 32)

print("the farenheit value is" + str(celsius) + "degree is" + str(farenheit(celsius)))

'''

def convert_temp(celsius):
    calc = celsius * 1.8
    return (calc + 32)

celsius = 12
print(convert_temp(celsius))

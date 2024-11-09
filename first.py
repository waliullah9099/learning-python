one = 1

some_numbers = 100000

isOnline = True
isHappy = False
my_name = "MR London"

book_price = 21.0

if isOnline:
    print("Please write me a success message")


amar_age = 22
tmr_age = 18

if amar_age > tmr_age:
    print("Amar is older than Tomi")
else: 
    print("Tomi is older than Amar")


if 1 > 2:
  print("1 is greater than 2")
elif 2 > 1:
  print("1 is not greater than 2")
else:
  print("1 is equal to 2")

num = 100
while num >= 90:
    print(num)
    num -=1


lop_condition = True

while lop_condition:
    print("lop_condition keeps: 0%" %(lop_condition))
    lop_condition = False


for i in range(1, 11):
    print(i)

for i in range(90, 100):
    print(i)

my_interger = [1,2,3,4,5,6,2]
# print(my_interger)
# print(my_interger[0])
# print(my_interger[3])

x, y, z, w,h, e,n = my_interger
# print(x, y, z, w, h, e,n)

tmr_kotha = ["valo thaken", "ami ki dowa korbo ? ", " apnar jonnno dowa apnar familu korbe"]
# print(tmr_kotha[1])

tmr_valo_lage = []
tmr_valo_lage.append("cha ami khai na")
tmr_valo_lage.append("thanda amar posondo na")
# print(tmr_valo_lage)

tmr_somperke = {
    "name": "Habiba",
    "class" : 12,
    "isStudent": True
}
tmr_somperke["age"] = 18
# print(tmr_somperke)
# print("tmr nam hoy %s" %(tmr_somperke["name"]))
# print("tmi poro %s" %(tmr_somperke["class"]))

# for you in tmr_somperke:
#     print(you)

# for key in tmr_somperke:
#     print("%s --> %s" %(key, tmr_somperke[key]))


for key, value in tmr_somperke.items():
    print("%s ------- > %s" %(key, value))
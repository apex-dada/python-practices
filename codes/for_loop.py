# #for loop+ execute a block of code for a fixed numbers of times unlike while loop. we can repeat/iterate ir over a range , string , sequence , etc.

# #for loops works better if we want to execute our code for fixed number of time

# #syntax of for loop= for variable in range (initial value,ending value) . {intial value is inclusive and ending value is exclusive}for
# #   for x in range(1,11):
# #    print(x)          it will print 1,2,3,4,5,6,7,8,9,10.wont print 11 because its exclusive

# #for x in reversed(range(1,11)):
# #    print(x)   it will print 10,9,8,5,4,3,2,1 {printing in reverse for reversed() function}


# #for x in range(1,11,2):   {range(initial,ending,steps)}
# #    print(x)   it will print 1,3,5,7,9 . because we added 2 steps

# for x in range(1,21):
# #     if x==13:
# #         continue
# #     else:
# #         print(x)       # it will skin 13 and print 1 to 20 for using continue keyword.


# for x in range(1,21):
# #     if x==13:
# #         break
# #     else:
# #         print(x)  #it will print 1 to 13 beacuse we used break keyword.



# # ---------------countdown timer program--------------------
# #we will create a coutndown timer useing time library and for loop

# #import time
# #
# # myTime= int(input("enter the time in seconds"))
# # print("\n countdown begains!")
# # for x in range(0,myTime):
# #     print(x)
# #     time.sleep(1)
# #
# # print("time is over")

# #counting in backwards

# # import time
# # myTime=int(input("enter the time in second:"))
# # print("\nCountdonw begins!")
# # for x in range(myTime,0,-1):
# #     print(x)
# #     time.sleep(1)
# # print("time is over")

# # ****digital clock with hour minute and seconds******

# import time
# myTime=int(input("enter the time in seconds:"))
# for x in range(myTime,0,-1):
#     seconds=x%60
#     minutes=int(x/60) % 60
#     hours=int(x/3600)
#     time.sleep(1)

#     print(f"timer:{hours:02}:{minutes:02}:{seconds:02}")
# print("hello!time is up")    


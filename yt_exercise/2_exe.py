# Generate Fibonacci Series and sum of even numbers.

# def sumseries(lst):
#     temp = 0
#     for i in lst:
#         if i % 2 == 0:
#             temp = temp +i
#     print("Sum of Even number in series: ",temp)
# def fibonacci(n):
#     series = [0,1]
#     for i in range(n-2):
#         temp = series[-1] + series[-2]
#         series.append(temp)
#     print(series)
#     sumseries(series)
#
# n = int(input("Enter a length of series: "))
# fibonacci(n)

# Calculate Dog's Age
# assume  dog first 10 years equals humans 2 year then  dog's 2 year equals human's 1 year

# humanyear = int(input("Enter a age of human: "))
# dogyear = 0
#
# if humanyear <= 0:
#     print('Enter a valid age..')
#
# elif humanyear <= 2:
#     dogyear = 5 * humanyear
#     print(f" For Human year {humanyear}, Dog is  {dogyear} old.")
#
# else:
#     dogyear = 10 +(humanyear - 2) * 2
#     print(f" For Human year {humanyear}, Dog is  {dogyear} old.")


# Calculate number of notes in amount

# count ={}
# notes = [2000,500,200,100,50,20,10,5,2,1]
# amount = int(input("Enter your amount: "))
#
# def notecount(count,notes,amount):
#     for note in notes:
#         if amount != 0:
#             if amount >= note:
#                 temp = amount // note
#                 count[note] = temp
#                 amount = amount % note
#
# notecount(count,notes,amount)
# print(f"For transaction {amount} You required{count}: ")

# Calculate taxi fair
# assume     first 5 km fair is 10 km per hour

# def fare(ride):
#     if ride == 0:
#         print("You need to travel first!!")
#     elif ride <5:
#         fare = ride *10
#     else:
#         fare = 50 + (ride-5)*5
#     print(f"For {ride} KM ,the fare is {fare}")
#
# ride = float(input("Enter your travelled distance: "))
# fare(ride)
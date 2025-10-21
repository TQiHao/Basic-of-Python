# Full Name: Toh Qi Hao
# Tutorial Group: CSIT 110 - T04
# Declaration: it is my own program, i have not passed my program to my friends
# and willing to accept whatever penalty given to you. 

# task 1: display a welcome messsage 
# ask the user to enter his/her email: 

print("Welcome to our online services\n")
print("*********")
print("* Task 1 *")
print("*********\n")
user_email = input("Enter an email address for validation: ")
print("\n==>Please validate a link sent to your email address :) ")
input("press any key to continue\n")

#task 2

print("*********")
print("* Task 2 *")
print("*********\n")

#title: We provide the following three services

print("\nWe provide the following three services")
print("="*39)

service1 = input("\tBooking of service 1:     ")
service2 = input("\tBooking of service 2:     ")
service3 = input("\tBooking of service 3:     ")

#title: Cost of various services (cents per second)

print("\nCost of various services (cents per second)")
print("="*50)


price1 = input(f"\tBooking of service {service1: <15}:    ")
price2 = input(f"\tBooking of service {service2: <15}:    ")
price3 = input(f"\tBooking of service {service3: <15}:    ")

print("\nSummary of various costs")
print("="*24)
print("\nService                         Cost per sec")
print("-"*44)
print("{:<25} {:>10}".format(service1, price1) + " cent(s)")
print("{:<25} {:>10}".format(service2, price2) + " cent(s)")
print("{:<25} {:>10}".format(service3, price3) + " cent(s)")

#task 3: Users can now request services by entering the number of hours / minutes / seconds
#(separated by spaces when entering the three values). 

print("\n*********")
print("* Task 3 *")
print("*********\n")

#title: Booking of various services (hours minutes seconds)

print("Booking of various services (hours minutes seconds)")
print("="*55)

hour1 = input(f"Enter hours minutes seconds for {service1:<15}:    ")
hour2 = input(f"Enter hours minutes seconds for {service2:<15}:    ")
hour3 = input(f"Enter hours minutes seconds for {service3:<15}:    ")

h1, m1, s1 = hour1.split()
h2, m2, s2 = hour2.split()
h3, m3, s3 = hour3.split()

print("\nYou have booked the following services")
print("=" * 40)
print(f"\n{'Service':<15} {'Hours':<8} {'Minutes':<8} {'Seconds':<8}")
print('-' * 43)
print(f"{service1:<15} {h1:<8} {m1:<8} {s1:<8}")
print(f"{service2:<15} {h2:<8} {m2:<8} {s2:<8}")
print(f"{service3:<15} {h3:<8} {m3:<8} {s3:<8}")

#Task 4: the number of hours / minutes / seconds for the 1st service
# and the 3rd service MUST be swapped

print("\n*********")
print("* Task 4 *")
print("*********\n")

hour1 = hour3 
h1,h3 = h3,h1
m1,m3 = m3,m1
s1,s3 = s3,s1

print("\nAfter the swapped timings")
print("="*27)
print(f"\n{'Service':<15} {'Hours':<8} {'Minutes':<8} {'Seconds':<8}")
print('-' * 43)
print(f"{service1:<15} {h1:<8} {m1:<8} {s1:<8}")
print(f"{service2:<15} {h2:<8} {m2:<8} {s2:<8}")
print(f"{service3:<15} {h3:<8} {m3:<8} {s3:<8}")

print("\n*********")
print("* Task 5 *")
print("*********\n")

total_secs1 = (int(h1) * 3600) + (int(m1) * 60) + int(s1)
total_secs2 = (int(h2) * 3600) + (int(m2) * 60) + int(s2)
total_secs3 = (int(h3) * 3600) + (int(m3) * 60) + int(s3)
total_cost1 = int(total_secs1) * int(price1)
total_cost2 = int(total_secs1) * int(price2)
total_cost3 = int(total_secs1) * int(price3)
final_cost = int(total_cost1) + int(total_cost2) + int(total_cost3)
in_singapore_dollar = int(final_cost)/100

print("\nSummary of charges")
print("=" * 20)
print(f"\n{'Service':<15} {'Hours':<8} {'Minutes':<8} {'Seconds':<8} {'usage (sec)':<8} {'unit charge':<8} {'Total costs':<8}")
print("-" * 80)
print(f"{service1:<15} {h1:<8} {m1:<8} {m1:<8} {total_secs1:<12} {price1:<12} {total_cost1:<12}")
print(f"{service2:<15} {h2:<8} {m2:<8} {m2:<8} {total_secs2:<12} {price2:<12} {total_cost2:<12}")
print(f"{service3:<15} {h3:<8} {m3:<8} {m3:<8} {total_secs3:<12} {price3:<12} {total_cost3:<12}")
print("=" * 80)
print(f"{'Total cost':<68} {final_cost:<12}")
print(f"{'Singapore $':<68} {in_singapore_dollar:<12}")
print("\nThank you for using our service")
print("An Invoice of payment $" + str(in_singapore_dollar) + " will be sent to " + user_email)

# last statement of your program
input("Enter any character to end")
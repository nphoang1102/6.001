# Define main function
def main():
   # Setup some constants first
   portion_down_payment = 0.25
   current_savings = 0
   total_month = 0
   r = 0.04

   # Prompting for user input, cast to float here for computation
   # and decimal point
   annual_salary = float(input("Enter your annual salary: "))
   portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
   total_cost = float(input("Enter the cost of your dream home: ")) * portion_down_payment
   monthly_salary = annual_salary/12
   
   # Calculation, paying for the down payment only, not the whole house...
   while (current_savings < total_cost):
      total_month += 1
      current_savings += (current_savings*r/12)
      current_savings += (monthly_salary*portion_saved)

   # Display result and terminate
   print("Number of months:", total_month)
   return None

# Invoke main
main()
# 
# Some more iteration with a slight twist of branching
# 
# - Hoang N -

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
   semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
   monthly_salary = annual_salary/12
   
   # Calculation, paying for the down payment only, not the whole house...
   while (current_savings < total_cost):
      total_month += 1
      # Hmm according to the test cases, the salary raise is percentile of monthly salary though
      # Also you cannot expect a raise after the first month too
      if ((total_month % 6) == 1) and (total_month > 1): 
         monthly_salary += (monthly_salary*semi_annual_raise)
      current_savings += (current_savings*r/12)
      current_savings += (monthly_salary*portion_saved)

   # Display result and terminate
   print("Number of months:", total_month)
   return None

# Invoke main
main()
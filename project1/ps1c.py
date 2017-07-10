# 
# Some more iteration and branching with bisection search algorithm
# 
# - Hoang N -

# Define main function
def main():
   # Layout some constants first
   portion_down_payment = 0.25
   semi_annual_raise = 0.07
   r = 0.04
   total_cost = 1000000.0 * portion_down_payment

   # Variables for bisection search and approximation
   high = 10000
   low = 0
   guess_rate = int(round((high + low)/2.0))
   steps = 0

   # Variables to store closest approximation
   final_total_month = 0
   final_guess_rate = 0.0

   # Prompting user for input
   annual_salary = float(input('Enter the starting salary: '))

   # Declare this here for condition checking below
   total_month = 0

   # Start bisection search, 
   # forcing the guessing to be as closest as possible
   while (abs(high-low) > 1):
      # One search interval done, update search terms and count up
      if steps:
         # It is quite significant to use <= here instead of < only
         # now that I think about it hard enough. So theoratically,
         # when the bisection search found a rate that fit, it should
         # try to reduce some precision to actually find the optimal
         # value instead of increasing it, thus explain the <= here
         # instead of <. Also < here means <= at the else below.
         if (total_month <= 36):
            high = guess_rate
         else:
            low = guess_rate
         guess_rate = int(round((high + low)/2.0))

      # Reseting variables for every new bisection search step
      total_month = 0
      current_savings = 0.0
      monthly_salary = annual_salary/12.0;
      steps += 1

      # Finding the months
      while (current_savings < total_cost):
         total_month +=1
         # Hmm according to the test cases, the salary raise is percentile of monthly salary though
         # Also you cannot expect a raise after the first month too
         if ((total_month % 6) == 1) and (total_month > 1): 
            monthly_salary += (monthly_salary*semi_annual_raise)
         current_savings += (current_savings*r/12.0)
         current_savings += (monthly_salary*guess_rate/10000.0)

      # Storing the closest value here
      if (total_month == 36):
         final_total_month = total_month
         final_guess_rate = guess_rate

   # Display result and terminate
   if (final_total_month == 36):
      print('Best saving rate:', float(guess_rate/10000.0))
      print('Steps in bisection search:', steps)
   else:
      print('It is not possible to pay the down payment in three years')
   return None

# Invoke main
main()

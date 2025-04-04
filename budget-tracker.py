income = 0
expenses = {}
expense_amount = 0
total_expenses = 0
total_income = 0
overspent = 0

def console_printer():
  print('--- Personal Budget Tracker ---')
  print('1. Add Income')
  print('2. Add Expense')
  print('3. View Summary')
  print('4. Exit')

def add_income():
  global total_income
  income = int(input('Enter the income amount: '))
  income = float(income)
  total_income += income
  print(f'Income of {income} added successfully.')
    
def record_expense():
  global total_income
  global total_expenses
  expense_category = str(input('Enter the expense category (e.g groceries, rent): '))
  expense_amount =  int(input('Enter the expense amount: '))
  if expense_amount < total_income:
    total_income -= expense_amount
    expenses[expense_category] = expense_amount
    expense_amount = float(expense_amount)
    total_expenses += expense_amount
    print(f'Expense of {expense_amount} added to {expense_category}')
    print('  ')
    print(f'Your total income is {total_income}.')
  else:
    print('  ')
    print('Warning... You have exceeded your budget limit.')

def view_summary():
  print('--- Budget Summary ---')
  print(f'Total Income: {total_income}')
  print(f'Total Expense: {total_expenses}')
  for key in expenses:
    value = expenses[key]
    print(f'You have spent {value} on {key}.')
    
def program_logic():
  console_printer()
  operation = int(input('Enter your choice (1-4): '))
  if (operation == 1):
    add_income()
    program_logic()

  elif (operation == 2):
    record_expense()
    program_logic()

  elif (operation == 3):
    view_summary()
    program_logic()

  else:
    print('You have successfully exited the program.')    

program_logic()

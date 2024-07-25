items = []
while True:
print('---Welcome to the supermarket---')
print ('1. View items\n2. Add items\n3. Purchase items \n4. Search items\n5. Edit items \n6. Exit program') 
choice = input( 'Enter the number of your choice: ')
if choice == '1'
   print ('------------VIew Items--------------')
   print( 'The number of items in the inventory are: %d' % len(items))
   if len(items) != 0:
    print( 'Here are all the items available in the supermarket: ')
    for index, item in enumerate(items, 1):
         print(f' {index). Name: {item["name"]}, Quantity: (item["quantity"]}, Price: ${item["price"]: 2f}')
elif choice == '2'
     print('---------------Add Items---------------')
     print( 'To add an item, fill in the form:')
     item = {}
     item[ 'name'] = input('Item name: ')
     while True:
           try:
               item['quantity'] = int(input('Item quantity: '))
               break
           except VaLueerror:
                print( 'Quantity should only be in digits')
      while True:
           try:
               item['price'] = float (input( 'Price $: '))
               break
           except ValueError:
               print('Price should be a numeric value')
      print( 'Item has been successfully added.')
      items. append (item)

elif choice == '3'
    print('----------Purchase items---------')
    print( 'Items in stock:')
    for index, item in enumerate(items, 1):
        print(f' (index). {item["name"]}')
    purchase_index = input('Enter the number of the item you want to purchase: ')
    try:
        purchase_index = int (purchase_index)
        if 1 <= purchase_index <= len(items):
            selected_item = items [purchase_index - 1]
            print(f'Selected item: {selected_item["name"]}')
            purchase_quantity = int(input('Enter the quantity wanted: '))
                     if purchase_quantity ‹= selected_item['quantity']:
                        total_cost = selected_item['price'] * purchase_quantity
                        print(f'Pay ${total_cost:.2f} at checkout counter.')
                        selected_item[ 'quantity'] -= purchase_quantity 
                  else:
                        print ("Quantity required is not available")
        else:
            print("Invalid item number")
      except ValueError:
      print( 'Invalid input. Please enter a valid number.')

    elif choice == '4'
         print('---------Search items---------')
         find_item = input( 'Enter the item name to search in inventory: '). lower ()
         found = False
         for item in items:
             if find_item == item['name']. lower ():
                 print(f'The item named {find_item} is displayed below with its details:')
                 print(f'Name: {item["name"]}, Quantity: {item["quantity"]}, Price: ${item["price"]:.2f}')
                 found = True
                 break
         if not found:
             print( 'Item not found.')
  elif choice == '5'
    print('---------Edit items---------')
    item_name = input('Enter the name of the item that you want to edit:'). lower()
    found = False
    for item in items:
        if item_name == item[ 'name']. lower ():
            print(f'Here are the current details of {item_name}: ')
            print(f'Name: {item["name"]}, Quantity: {item["quantity"]}, Price: ${item["price"]: 2f}')
            item[ 'name'] = input( 'Item name: ')
            while True:
                try:
                    item[ 'quantity'] = int(input('Item quantity: '))
                    break
                except ValueError:
                    print( 'Quantity should only be in digits')
            while True:
                try:
                    item[ 'price'] = float (input( 'Price $: '))
                    break
                 except ValueError:
                    print( 'Price should be a numeric value')
            print('Item has been successfully updated. ')
            found = True
            break
      if not found:
        print( 'Item not found.')
  elif choice == '6'
    print('---------Exiting---------')
    break
  else:
      print( 'You entered an invalid option. Please try again.')
      
print( 'Thank you for using the supermarket management system!')
            

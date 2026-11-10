# 4x3 Arrays: item names, prices, and stock
item_names = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
    ["j", "k", "l"]
]

prices = [
    [5000, 5000, 3000],
    [7000, 7000, 7000],
    [3000, 4000, 5000],
    [6000, 8000, 6000]
]

stock = [
    [5, 5, 5],
    [5, 5, 5],
    [5, 5, 5],
    [5, 5, 5]
]

valid_money = [1000, 2000, 5000, 10000, 20000, 50000, 100000]
balance = 0

machine_status = "IDLE"
while True:
    machine_status = "IDLE"
    
    code = input("\nEnter item code (format RowColumn, e.g., 01): ")
    
    if len(code) != 2 or not code.isdigit():
        print("Invalid code format.")
        continue

    row = int(code[0])
    column = int(code[1])

    # Checking for a 4x3 array
    if row > 3 or column > 2:
        print("Invalid code. Slot does not exist.")
        continue

    if stock[row][column] <= 0:
        print("Out of stock.")
        continue

    item_price = prices[row][column]
    print(f"Selected: {item_names[row][column]}")
    print(f"Price: Rp{item_price}")
    
    # Payment Processing Loop
    while balance < item_price:
        print(f"Current balance: Rp{balance}")
        money_in = input("Insert Rupiah money (or type 'c' to cancel): ")
        
        if money_in.lower() == 'c':
            print(f"Transaction canceled. Refunding: Rp{balance}")
            balance = 0
            break
            
        if money_in.isdigit():
            inserted_money = int(money_in)
            if inserted_money not in valid_money:
                print("Invalid money. Only valid Rupiah moneys accepted.")
            else:
                balance += inserted_money
        else:
            print("Invalid input.")

    # Proceed only if balance is good
    if balance >= item_price:
        print("\nReleasing item...")
        
       # Drop sensor simulation (With a yes or no for demonstration)
        sensor_input = input("Did the item drop successfully? (y/n): ")
        sensor = sensor_input.lower() == 'y'
        
        if not sensor:
            print(f"Item stuck, Refunding exact balance: Rp{balance}")
            balance = 0
            continue
            
        # Deduct price and stock
        stock[row][column] -= 1
        change = balance - item_price
        
        print(f"\nItem dispensed successfully! Change due: Rp{change}")
        
        # Rupiah Change Breakdown
        r100 = change // 100000
        change %= 100000
        
        r50 = change // 50000
        change %= 50000
        
        r20 = change // 20000
        change %= 20000
        
        r10 = change // 10000
        change %= 10000
        
        r5 = change // 5000
        change %= 5000
        
        r2 = change // 2000
        change %= 2000
        
        r1 = change // 1000
        change %= 1000
        
        if (r100 + r50 + r20 + r10 + r5 + r2 + r1) > 0:
            print("Dispensing Change:")
            if r100 > 0: print(f"  Rp100.000 x {r100}")
            if r50 > 0:  print(f"  Rp50.000 x {r50}")
            if r20 > 0:  print(f"  Rp20.000 x {r20}")
            if r10 > 0:  print(f"  Rp10.000 x {r10}")
            if r5 > 0:   print(f"  Rp5.000 x {r5}")
            if r2 > 0:   print(f"  Rp2.000 x {r2}")
            if r1 > 0:   print(f"  Rp1.000 x {r1}")
            
        balance = 0
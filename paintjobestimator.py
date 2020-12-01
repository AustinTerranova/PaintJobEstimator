newCalculation = True;
while newCalculation:
    
    
    while True:
        try: 
            #print("please enter a number greater than 0");
            squareFeetSpace = int(input("Enter the square feet of wall space to be painted: "));
            if squareFeetSpace <= 0:
                print("please enter a number greater than 0");
                continue;
            break;
        except (ValueError, TypeError):
            print("please enter a valid integer");

    
    while True:
        try:
            #print("please enter a number greater than 0");
            paintPrice = int(input("Enter the price per a gallon of paint: "));
            if paintPrice <= 0:
                print("please enter a number greater than 0");
                continue;
            break;
        except (ValueError, TypeError):
            print("please enter a valid integer");


    paintRequired = squareFeetSpace / 350;
    paintCost = paintPrice * paintRequired;
    laborRequired = paintRequired * 6;
    laborCharges = laborRequired * 62.25;
    totalCost = laborCharges + paintPrice * paintRequired;
    
    
    print("number of gallons of paint required:", round(paintRequired));
    print("hours of labor required: %.1f" % laborRequired);
    print("cost of paint: $",round(paintCost));
    print("labor charges: $%.2f" % laborCharges);
    print("total cost: $%.2f" % totalCost);
   

    again = input("If you want to play again type y: ");
    if again != "y":
        newCalculation = False;

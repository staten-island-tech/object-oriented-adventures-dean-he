#while past_intro == True:
    x = input('what would you like to do? [train/shop]')
    bought = []
    if x == 'shop':
        purchase = input('Whalen: Welcome to the shop! What would you like to purchase? Here is what we have:')
        for items in 'shop list':
            print(items)
        option = input('')
        if option in 'item list':
            print(option)
            bought.append(option)
            
        else:
            print("'Whalen: Hey I don't have that item in stock... Here's what I do have though, you can buy these items:'")
            for items in 'item list':
                print(items)
            

    elif x == 'train':
        print(yewsr)



    else:
        print('Invalid option, please choose between [train/shop]')

        

items = ["pencil", "eraser", "notebook", "sharpener", "glue"]
stock_counts = [12, 0, 8, 5, 3]


inventory =  {item: count for item, count in zip(items, stock_counts)}
print ("full inventory:", inventory)


in_stock_items = {item: count for item, count in inventory.items() if count > 0}
print("Items in stock:", in_stock_items)

chosen_item = input("Enter the item you want to check: ")

if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(f"Sorry, {chosen_item} is not available.")
    exit()
    
prices = [10, 5, 40, 15, 20]
markup = int(input("Enter the markup amount to add to every price: "))

marked_up_prices = {item: price + markup for item, price in zip(items, prices)}
print("Marked up prices:", marked_up_prices)

item_index = items.index(chosen_item)
final_price = marked_up_prices[chosen_item]

print(f"The final price of {chosen_item} after markup is: {final_price}")

print("")
print("====school store inventory checker====")
print("item brought", chosen_item)
print("price paied", final_price)
print("updated inventory", in_stock_items)
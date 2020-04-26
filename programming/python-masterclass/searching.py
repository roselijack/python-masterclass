shopping_ist = ["ab","bc","cd"]
found_item = "12"
found_at = None
for i in range(len(shopping_ist)) :
    if shopping_ist[i] == found_item:
        found_at = i
        break;
if found_at!=None:
    print("found the item at index {0}".format(found_at))
else:
    print("not found")

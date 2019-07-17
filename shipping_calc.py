premium_ground_shipping = 125.00

def cost_of_ground_shipping(weight, cost):
 cost = (weight * cost) + 20.00
 return cost


def cost_of_drone_shipping(weight,cost):
 cost = weight * cost
 return cost


def cheapest_shipping(weight):
 if weight <= 2:
   cost1 = cost_of_ground_shipping(weight, 1.50)
   cost2 = cost_of_drone_shipping(weight, 4.50)

   print("Cost of ground shipping: $" + str('%.2f' % cost1))
   print("Cost of drone shipping: $" + str('%.2f' % cost2))
   print("Cost of premium shipping: $" + str('%.2f' % premium_ground_shipping))


   if (cost1 < cost2) and (cost1 < premium_ground_shipping):
      return "You should use ground shipping, it will cost $" + str('%.2f' % cost1)
   elif (cost2 < cost1) and (cost2 < premium_ground_shipping):
      return "You should use drone shipping, it will cost $" + str('%.2f' % cost2)
   else:
      return "You should use premium ground shipping, it will cost $" + str('%.2f' % premium_ground_shipping)

 elif weight > 2 and weight <= 6:
   cost1 = cost_of_ground_shipping(weight, 3.00)
   cost2 = cost_of_drone_shipping(weight, 9.00)

   print("Cost of ground shipping: $" + str('%.2f' % cost1))
   print("Cost of drone shipping: $" + str('%.2f' % cost2))
   print("Cost of premium shipping: $" + str('%.2f' % premium_ground_shipping))

   if (cost1 < cost2) and (cost1 < premium_ground_shipping):
      return "You should use ground shipping, it will cost $" + str('%.2f' % cost1)
   elif (cost2 < cost1) and (cost2 < premium_ground_shipping):
      return "You should use drone shipping, it will cost $" + str('%.2f' % cost2)
   else:
      return "You should use premium ground shipping, it will cost $" + str('%.2f' % premium_ground_shipping)

 elif weight > 6 and weight <= 10:
   cost1 = cost_of_ground_shipping(weight, 4.00)
   cost2 = cost_of_drone_shipping(weight, 12.00)

   print("Cost of ground shipping: $" + str('%.2f' % cost1))
   print("Cost of drone shipping: $" + str('%.2f' % cost2))
   print("Cost of premium shipping: $" + str('%.2f' % premium_ground_shipping))

   if (cost1 < cost2) and (cost1 < premium_ground_shipping):
      return "You should use ground shipping, it will cost $" + str('%.2f' % cost1)
   elif (cost2 < cost1) and (cost2 < premium_ground_shipping):
      return "You should use drone shipping, it will cost $" + str('%.2f' % cost2)
   else:
      return "You should use premium ground shipping, it will cost $" + str('%.2f' % premium_ground_shipping)

 elif weight > 10:
   cost1 = cost_of_ground_shipping(weight, 4.75)
   cost2 = cost_of_drone_shipping(weight, 14.25)

   print("Cost of ground shipping: $" + str('%.2f' % cost1))
   print("Cost of drone shipping: $" + str('%.2f' % cost2))
   print("Cost of premium shipping: $" + str('%.2f' % premium_ground_shipping))

   if (cost1 < cost2) and (cost1 < premium_ground_shipping):
      return "You should use ground shipping, it will cost $" + str('%.2f' % cost1)
   elif (cost2 < cost1) and (cost2 < premium_ground_shipping):
      return "You should use drone shipping, it will cost $" + str('%.2f' % cost2)
   else:
      return "You should use premium ground shipping, it will cost $" + str('%.2f' % premium_ground_shipping)


print(cheapest_shipping(41.5))
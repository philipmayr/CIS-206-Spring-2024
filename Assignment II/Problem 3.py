# ASSIGNMENT II - CIS 206 - phil may'r

# Problem 3
print("This program finds the best option to choose among three publisher's options for author remuneration.")
print()
# first option consts
DELIVERY_OF_FINAL_MANUSCRIPT_REMUNERATION = 5000
PUBLISHING_REMUNERATION = 20000

# second option const
REMUNERATION_FACTOR_PER_NET_PRICE_COPY = 0.125

# third option consts
REMUNERATION_FACTOR_PER_NET_PRICE_COPY_FIRST_4K = 0.10
REMUNERATION_FACTOR_PER_NET_PRICE_COPY_OVER_4k = 0.14

# get net price per copy and number of copies
net_price_per_copy = float(input("Enter net price per copy: $"))
estimated_num_of_copies = float(input("Enter estimated number of copies to be sold: "))

# find first option total remuneration
FIRST_OPTION_TOTAL_REMUNERATION = DELIVERY_OF_FINAL_MANUSCRIPT_REMUNERATION + \
                                  PUBLISHING_REMUNERATION
      
# find second option total remuneration
SECOND_OPTION_TOTAL_REMUNERATION = net_price_per_copy * \
                                   REMUNERATION_FACTOR_PER_NET_PRICE_COPY * \
                                   estimated_num_of_copies

# find third option total remuneration
if estimated_num_of_copies > 4000:
    THIRD_OPTION_TOTAL_REMUNERATION = (net_price_per_copy * \
    REMUNERATION_FACTOR_PER_NET_PRICE_COPY_FIRST_4K * \
    estimated_num_of_copies) + \
    (net_price_per_copy * \
    REMUNERATION_FACTOR_PER_NET_PRICE_COPY_OVER_4k * \
    (estimated_num_of_copies - 4000))
else:
    THIRD_OPTION_TOTAL_REMUNERATION = net_price_per_copy * \
    REMUNERATION_FACTOR_PER_NET_PRICE_COPY_FIRST_4K * \
    estimated_num_of_copies
    
# find best option
if (FIRST_OPTION_TOTAL_REMUNERATION >= SECOND_OPTION_TOTAL_REMUNERATION) and \
   (FIRST_OPTION_TOTAL_REMUNERATION >= THIRD_OPTION_TOTAL_REMUNERATION):
   best_option = "first option"
elif (SECOND_OPTION_TOTAL_REMUNERATION >= FIRST_OPTION_TOTAL_REMUNERATION) and \
     (SECOND_OPTION_TOTAL_REMUNERATION >= THIRD_OPTION_TOTAL_REMUNERATION):
   best_option = "second option"
else:
   best_option = "third option"
    
# print results
print()
print("For the first option, the total remuneration amounts to: "
      + '${:,.2f}'.format(FIRST_OPTION_TOTAL_REMUNERATION))  
print("For the second option, the total remuneration amounts to: "
      + '${:,.2f}'.format(SECOND_OPTION_TOTAL_REMUNERATION))   
print("For the third option, the total remuneration amounts to: "
      + '${:,.2f}'.format(THIRD_OPTION_TOTAL_REMUNERATION))  
print()
print("The best option to choose is the " + best_option + ".")

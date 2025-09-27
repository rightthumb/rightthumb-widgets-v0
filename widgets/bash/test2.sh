#!/bin/bash  

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

#Example for bash split string by space  
  
read -p "Enter any string separated by space: " str  #reading string value  
  
IFS='' #setting space as delimiter  
read -ra ADDR <<<"$str" #reading str as an array as tokens separated by IFS  
  
for i in "${ADDR[@]}"; #accessing each element of array  
do  
echo "$i"  
done  



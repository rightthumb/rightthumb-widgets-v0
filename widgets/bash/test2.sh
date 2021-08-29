#!/bin/bash  
#Example for bash split string by space  
  
read -p "Enter any string separated by space: " str  #reading string value  
  
IFS='' #setting space as delimiter  
read -ra ADDR <<<"$str" #reading str as an array as tokens separated by IFS  
  
for i in "${ADDR[@]}"; #accessing each element of array  
do  
echo "$i"  
done  

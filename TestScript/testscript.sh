#!/bin/bash
echo "Linux Bash Scripting" > words.txt
echo "101 202 303" > numbers.txt
echo "Files created!"
variable="Now I remember!"

echo -e "--------------------"
for file in ./*.txt; do
  if [ -f  "$file" ]; then
    if grep -q "Bash" "$file"; then
      echo "Word found in $file"
      cat "$file"
    else
      echo "Word NOT found in $file"
    fi
    echo "--------------------"
  fi
done
echo -e "Script executed!"

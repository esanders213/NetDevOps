#!/bin/bash

# - # Comments out a line.
# - Best day ever shell script

name="Erik" # - This creates a standard variable.

name_arg=$1  # - This creates a argument variable.  Used in the terminal when launching script.

compliment_arg=$2 # - This is argument 2.

# - You can also read an variable from input of a user.
echo "What is your name? "

# - This line will read "name" from the echo above.
read name

# - echo prints out the words or statements to terminal.

echo "Good morning $name!!"

# - Pauses script for 3 seconds.
sleep 3

echo "You're looking good today $name_arg!!"

sleep 1
echo "You have the best $compliment_arg I've ever seen $name!!"







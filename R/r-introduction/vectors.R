# vectors can be combined via the function c
n <- c(2,3,5)
s <- c('aa', 'bb', 'cc')
print(c(n, s))

# named vector members

# Roulette winnings from Monday to Friday
roulette_vector <- c(-24, -50, 100, -350, 10)

# Assign days as names of roulette_vector
print(names(roulette_vector) <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"))

A_vector <- c(1, 2, 3)
B_vector <- c(4, 5, 6)

# Take the sum of A_vector and B_vector
total_vector <- c(1, 2, 3) + c(4, 5, 6)
  
# Print out total_vector
print(total_vector)
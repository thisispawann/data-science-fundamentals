# Construct a matrix with 3 rows containing the numbers 1 up to 9,
# filled row-wise

matrix1 <- matrix(1:9, byrow = TRUE, nrow = 3)
print(matrix1)

m <- matrix(nrow = 2, ncol = 3)
m
dim(m)

attributes(m)
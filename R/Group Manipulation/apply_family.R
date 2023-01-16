# build the matrix
theMatrix <- matrix(1:9, nrow=3)

# sum the rows
apply(theMatrix, 1, sum)

# sum the columns
apply(theMatrix, 2, sum)

rowSums(theMatrix)

colSums(theMatrix)

# lapply and sapply
theList <- list(A=matrix(1:9, 3), B=1:5, C=matrix(1:4, 2), D=2)
lapply(theList, sum)

sapply(theList, sum)

theNames <- c("Jared", "Deb", "Paul")
lapply(theNames, nchar)

# biuld two lists
firstList <- list(A=matrix(1:16, 4), B=matrix(1:16, 2), C=1:5)
secondList <- list(A=matrix(1:16, 4), B=matrix(1:16, 8), C=15:1)

# test element-by-element if they are identical
mapply(identical, firstList, secondList)

## build a simple function
## it adds the number of rows (or length) of each corresponding element
simpleFunc <- function(x, y){
  NROW(x) + NROW(y)
}
# apply the function to the two lists
mapply(simpleFunc, firstList, secondList)



























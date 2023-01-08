# Lists are a special type of vector that can contain elements of different
# classes
# Lists are a very important data type in R and we should get to know them well

x <- list(1, 'a', TRUE, 1+4i)
print(x)

list_1 <- list(
    x=c(10,20,30), 
    y=c('a', 'b', 'c'), 
    z=c(TRUE, FALSE)
    )
print(list_1)


test <- list('music tracks', 100, 5)

names(test) <- c('product', 'count', 'rating') # names function and product, count, rtating are labels
test

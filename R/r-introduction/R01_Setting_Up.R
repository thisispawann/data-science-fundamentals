# load data

library(datasets)


# summary data
head(iris)

summary(iris)

plot(iris)

# Clear Packages
detach("package:datasets", unload = TRUE)

# Clear plots
dev.off() # but only if there is a plot


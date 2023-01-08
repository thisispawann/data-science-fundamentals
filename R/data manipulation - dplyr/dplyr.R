install.packages("dplyr")
library(dplyr)

install.packages('nycflights13')
library('nycflights13')

View(flights)
head(flights)

# filter function to look specific value
f1 <- filter(flights, month==07) # 7th month 
View(f1)

# view month 7 and day 3
f2 <- filter(flights, month==07, day==3)
View(f2)

View(filter(flights, month==07, day==3, origin=='JFK'))

# slice() allows to select rows by position

slice(flights, 1:4)


# mutate() is used to add new column

over_delay <- mutate(flights, overall_delay = arr_delay - dep_delay)
View(over_delay)
head(over_delay)


# transmute() function is used to show only new column
over_delay <- transmute(flights, overall_delay = arr_delay - dep_delay)
View(over_delay)


# summarise() is used to find descriptive statistics

summarise(flights, avg_air_time = mean(air_time, na.rm=T)) # mean of air_time na removal is True

summarise(flights, tot_air_time = sum(air_time, na.rm = T))

summarise(flights, stdev_air_time = sd(air_time, na.rm = T))

# get multiple values at a time such as mean, sum
summarise(flights, avg_air_time = mean(air_time, na.rm = T), tot_air_time = sum(air_time, na.rm = T))

# group by calculation using group_by()

# Example 1
head(mtcars) # mtcars built-in dataset
View(mtcars)

# group by gear
by_gear <- mtcars %>% group_by(gear)
by_gear
View(by_gear)

a <- summarise(by_gear, gear1 = sum(gear), gear2 = mean(gear))
a
#a <- summarise(group_by(mtcars, cyl), mean(gear))

# sample_n() and sample_frac for creating samples

sample_n(flights, 15) # gives 15 random samples

sample_frac(flights, 0.4) # returns 40% of the total data

# arrange() used to sort dataset

View(arrange(flights, year, dep_time))

head(arrange(flights, desc(dep_time))) # desc -> descending order


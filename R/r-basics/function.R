# Simple function, no arguments
hello_world <- function()
{
  print("printing hello world...")
}

hello_world()

# Function with a single argument
hello_world <- function(name)
{ 
  print(paste('Hello ', name)) # paste -> concat
}

hello_world('abc')

# Function to add 2 numbers
add_num <- function(num1, num2)
{
  print(num1+num2)
}
add_num(10,20)

# Add a vector to a number
add_num(c(10,20,33), 8)

# Function with default argument values

hello_name <- function(name = 'Rajesh')
  
{
  print(paste('Hello ', name))
}

hello_name()
hello_name('Sam')
hello_name(name='James')

# Return a value from a function
hello_name <- function(name='David', title='Cricketer')
{
  return(paste(name, " ", title))
}
hello_name()

# Built in Functions

#generate 1000 random values from a normal distribution of mean 0 and 1
normalDist <- rnorm(1000, 0, 1)
mean(normalDist)
#histogram of normal distribution
hist(normalDist)

# To get more info
?hist

# square of a number
squares <- function(row) {
  for (i in 1:row) {
    a <- i^2
    print(a)
  }
}
squares(4)

# Cube of a number
cubes <- function(row) {
  for(i in 1:row){
    a <- i^3
    print(a)
  }
}
cubes(5)

#Example 1

status <- function(marks)
{
  result = 'Not Defined'
  if(marks>50) result = 'PASS'
  message('Your result is', ' ', result)
}
status(54)
status(20)


# Example 2

status <- function(age){
  ageGroup='Not Defined'
  vote = 'Not Defined'
  if (age>=18)
  {
    ageGroup='ADULT'
    vote = 'YES'
  }
  message('Your age group is ', ageGroup)
  message('Voting status is ', vote)
}
status(18)

# Example to convert a name into uppercase

status<-function(name)
{
  len<-nchar(name)
  if(len>=5) name=toupper(name)
  message('User given name is ', name)
}
status('pawan')
status('Sam')

# Example to calculate bonus

get_bonus<-function(salary, exp)
{
  if(exp>5)
  {
    bonus_per=10
  }else{
    bonus_per = 5
  }
  bonus = salary*(bonus_per/100)
  return (bonus)
}
get_bonus(25000, 6)



























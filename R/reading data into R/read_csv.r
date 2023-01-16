#reading CSV file
url <- "http://www.jaredlander.com/data/TomatoFirst.csv"
tomato <- read.table(file = url, header = TRUE, sep = ",")
head(tomato)

#read_delim
library(readr)
tomato2 <- read_delim(url, delim=',', col_names = TRUE)

#fread
library(data.table)
tomato3 <- fread(input=url, sep=',', header=TRUE)
head(tomato3)

# read Excel data
library(openxlsx)

tomato4 <- read.xlsx("D:/console/projects/data-science/R/reading data into R/excel_sample.xlsx")
tomato4

# reading from databases
install.packages("RSQLite")
library(RSQLite)
drv <- dbDriver('SQLite')
class(drv)

# connecting database
con <- dbConnect(drv, "D:/console/projects/data-science/R/reading data into R/diamonds.db")
class(con)

dbListTables(con)

dbListFields(con, name = 'diamonds')

dbListFields(con, name='DiamondColors')

# SELECT * query from one table
diamondsTable <- dbGetQuery(con, "SELECT * FROM diamonds",
                            stringAsFactors=FALSE)
#  simple SELECT * query from one table
colorTable <- dbGetQuery(con, "SELECT * FROM DiamondColors",
                         stringAsFactors=FALSE)
# do a join between the two tables

longQuery <- "SELECT * FROM diamonds, DiamondColors
              WHERE
              diamonds.color = DiamondColors.Color"
diamondsJoin <- dbGetQuery(con, longQuery,
                             stringsAsFactors=FALSE)
#We can easily check the results of these queries by viewing the resulting data.frames.

head(diamondsTable)

head(colorTable)
head(diamondsJoin)


# data included with R
install.packages('tidyverse')
library(tidyverse)

data(diamonds, package = 'ggplot2')
head(diamonds)

# extract data from websites

# web scraping
install.packages('rvest')
library(rvest)

ribalta <- read_html("https://www.jaredlander.com/data/ribalta.html")

class(ribalta)

ribalta %>% html_nodes('ul') %>% html_nodes('span')

ribalta %>% html_nodes('.street')

ribalta %>% html_nodes('.street') %>% html_text()

ribalta %>% html_nodes('#longitude') %>% html_attr('value')

ribalta %>%
  html_nodes('table.food-items') %>%
  magrittr::extract2(5) %>%
  html_table()


# reading json data
install.packages('jsonlite')
library(jsonlite)

pizza <- fromJSON('http://www.jaredlander.com/data/PizzaFavorites.json')
pizza

class(pizza)

class(pizza$Name)

class(pizza$Details)

class(pizza$Details[[1]])

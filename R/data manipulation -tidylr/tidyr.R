
# The tidyr package helps us to create tidy data.A tidy data is easy to visualize and model.
#gather() - It make wide data longer
#spread() - It makes long data wider
#separate() - It splits a single column into multiple columns
#unite() - It combines multiple columns into a single column
install.packages('tidyr')
library('tidyr')

n = 10

wide <- data.frame(
  ID = c(1:n),
  Face.1 = c(131,372,253,546,786,125,564,346,567,334),
  Face.2 = c(432,200,462,301,1000,326,924,505,254,656),
  Face.3 = c(451,1201,785,653,882,634,694,574,637,555)
)
View(wide)

# gather() - Reshaping data from wide format to long format
long <- wide %>% gather(Face, ResponseTime, Face.1:Face.3)
View(long)

# separate() - splits a single column into multiple columns

long_separate <- long %>% separate(Face, c("Target", "Number"))
View(long_separate)

# unite() - combines multiple columns into a single column

long_unite <- long_separate %>% unite(Face, Target, Number, sep = ".")
View(long_unite)

# spread() - takes two columns (key and value) and spreads into multiple columns
# it makes 'long' data wider

back_to_wide <- long_unite %>% spread(Face, ResponseTime)
View(back_to_wide)

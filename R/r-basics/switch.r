use.switch <- function(x)
{
        switch(x,
        "a"="first",
        "b"="second",
        "z"="last",
        "c"="third",
        "other")
}

print(use.switch("z"))


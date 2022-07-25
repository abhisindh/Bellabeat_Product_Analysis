import os
list_ = os.listdir("D:/programming/Bellabeat_product_analysis/Resources/Datasets/Fitabase Data 4.12.16-5.12.16")

# print('''---
# title: "Data description"
# author: "Abhisindh"
# date: "`r Sys.Date()`"
# output:
#   html_document:
#     df_print: paged
# ---

# ```{r message=FALSE, warning=FALSE, error=FALSE, include=FALSE}
# knitr::opts_chunk$set(echo = TRUE)

# #Pacakges
# library(stats)
# library(Hmisc)
# library(tidyverse)
# library(readr)
# ```''')

for i in list_:
   name = i[0:-4]
   print(f"# {name}")
   #print("```{r include=FALSE}")
   #print(f'{name} <- read_csv("D:/programming/Bellabeat_product_analysis/Resources/Datasets/Fitabase Data 4.12.16-5.12.16/{name}.csv")')
  #print('```\n')
   #print("```{r echo=FALSE}")
   #print(f"describe({name}) %>% html()")
   #print('```\n')
   #print('<hr style="border:2px solid blue">')
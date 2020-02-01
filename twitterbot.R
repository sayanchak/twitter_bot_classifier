myurltrain <- 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTMd6IhuxV_QEXlgeZ1jT9xwA3Kxs7W9RQeP7NeZa6nqc-UhUWKuIx1kLNEpGHYXwUA7P98v0-7z43c/pub?gid=170737123&single=true&output=csv'
twitter_data<- read.csv(url(myurltrain))

I1 <-twitter_data$bot==1
I2 <-twitter_data$bot==0



I1$followers_count

train_bot=twitter_data$bot
train_verified=twitter_data$verified
train_followers_count =twitter_data$followers_count
train_friends_count = twitter_data$friends_count
train_listed_count = twitter_data$listed_count
train_statuses_count = twitter_data$statuses_count

v1<-sort(sample(10000,6000))
twitter.train<-twitter_data[v1,]
twitter.test<-twitter_data[-v1,]

bot.logit.train <- glm(train_bot~train_followers_count
                       +train_friends_count
                       +train_listed_count
                       +train_statuses_count, data=twitter_data)
summary(bot.logit.train)

bot.logit2.train <- glm(train_verified~train_followers_count
                       +train_friends_count
                       +train_listed_count
                       +train_statuses_count, data=twitter_data)
summary(bot.logit2.train)

# from our analysis we see that statuses_count and listed_count are
# statistically significant for this model


plot(train_bot, train_statuses_count)
library(pROC)
bot.logit.predict<-predict(bot.logit.train,twitter.test,type="response")
roc(twitter.test$health,health.logit.predict,plot=T)

name <- "Sean"
tea <- "Chank"
class(name)
class(tea)

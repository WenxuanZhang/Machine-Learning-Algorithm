# Multivariate Regression

library(car)
newdata = Prestige[,c(1:4)]
summary(newdata)

f12<-lm(income~women+education,data=newdata)
f1<-lm(education~women,data=newdata)
f2<-lm(income~women,data=newdata)

edu_w<-f1$residuals
income_w<-f2$residuals
ftest<-lm(income_w ~ edu_w)
d<-cor(newdata)
piw<-d[2,1]
pew<-d[1,3]
vare<-var(newdata$education)
vari<-var(newdata$income)
down<-(1-piw^2)*vare
up<-(1-pew^2)*vari
var(income_w)
cor(edu_w,income_w)*sqrt(var(income_w)/var(edu_w))

# That really works! Hooray!
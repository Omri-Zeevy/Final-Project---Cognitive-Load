setwd("C:/Users/shir/Dropbox/projectData")
data <- read.csv("all_data_Total_15sec.csv") 
#'MRR','MHR','HRV','RMSSD','SDNN','HRmaxHRminDifference','SDRR','HRV_div_aveHR','HRV_div_aveHR_MoveLast15','last5secHRave_div_aveHR','last10secHRave_div_aveHR','last15secHRave_div_aveHR', 'swat rank', 'Day', 'TLX Overall', 'Type'

dataHigh <- data[data$Type=="High",c("MRR","MHR","HRV","RMSSD","SDNN","HRmaxHRminDifference","SDRR","HRV_div_aveHR","HRV_div_aveHR_MoveLast15","last5secHRave_div_aveHR","last10secHRave_div_aveHR","last15secHRave_div_aveHR","swat.rank","Day","TLX.Overall","Type")]
dataMedium <- data[data$Type=="Medium",c("MRR","MHR","HRV","RMSSD","SDNN","HRmaxHRminDifference","SDRR","HRV_div_aveHR","HRV_div_aveHR_MoveLast15","last5secHRave_div_aveHR","last10secHRave_div_aveHR","last15secHRave_div_aveHR","swat.rank","Day","TLX.Overall","Type")]
dataLow <- data[data$Type=="Low",c("MRR","MHR","HRV","RMSSD","SDNN","HRmaxHRminDifference","SDRR","HRV_div_aveHR","HRV_div_aveHR_MoveLast15","last5secHRave_div_aveHR","last10secHRave_div_aveHR","last15secHRave_div_aveHR","swat.rank","Day","TLX.Overall","Type")]

summary(dataHigh)
summary(dataMedium)
summary(dataLow)

###Normal distribution of the data ###############################################################
#MHR
shapiro.test(dataHigh$MHR)
shapiro.test(dataMedium$MHR)
shapiro.test(dataLow$MHR)
par(mfrow=c(1,1))
hist(data$MHR,xlim = c(50, 100),main="histograma of All data MHR")
qqnorm(data$MHR, pch = 1, frame = FALSE,main="Normal Q-Q Plot MHR")
qqline(data$MHR, col = "red", lwd = 1)

#ks.test(data$MRR)
#ks.test(data$MRR,alternative = c("two.sided"),exact = NULL)

#par(mfrow=c(3,1))
#hist(data$MHR,xlim = c(40, 100))
#hist(dataHigh$MHR,xlim = c(40, 100))
#hist(dataHigh$MHR,xlim = c(40, 100))


#HRV
shapiro.test(dataHigh$HRV)
shapiro.test(dataMedium$HRV)
shapiro.test(dataLow$HRV)
par(mfrow=c(1,1))
hist(data$HRV,xlim = c(50, 100),main="histograma of All data HRV")
qqnorm(data$HRV, pch = 1, frame = FALSE,main="Normal Q-Q Plot HRV")
qqline(data$HRV, col = "red", lwd = 1)


#MRR
shapiro.test(dataHigh$MRR)
shapiro.test(dataMedium$MRR)
shapiro.test(dataLow$MRR)
par(mfrow=c(1,1))
hist(data$MRR,xlim = c(500, 1400),main="histograma of All data MRR")
qqnorm(data$MRR, pch = 1, frame = FALSE,main="Normal Q-Q Plot MRR")
qqline(data$MRR, col = "red", lwd = 1)

#RMSSD
shapiro.test(dataHigh$RMSSD)
shapiro.test(dataMedium$RMSSD)
shapiro.test(dataLow$RMSSD)
par(mfrow=c(3,1))
hist(dataHigh$RMSSD,main="histograma of High data RMSSD")
hist(dataMedium$RMSSD,main="histograma of Medium data RMSSD")
hist(dataLow$RMSSD,main="histograma of Low data RMSSD")

#SDNN
shapiro.test(dataHigh$SDNN)
shapiro.test(dataMedium$SDNN)
shapiro.test(dataLow$SDNN)
par(mfrow=c(3,1))
hist(dataHigh$SDNN,main="histograma of High data SDNN")
hist(dataMedium$SDNN,main="histograma of Medium data SDNN")
hist(dataLow$SDNN,main="histograma of Low data SDNN")

#HRmaxHRminDifference
shapiro.test(dataHigh$HRmaxHRminDifference)
shapiro.test(dataMedium$HRmaxHRminDifference)
shapiro.test(dataLow$HRmaxHRminDifference)
par(mfrow=c(3,1))
hist(dataHigh$HRmaxHRminDifference,main="histograma of High data HRmaxHRminDifference")
hist(dataMedium$HRmaxHRminDifference,main="histograma of Medium data HRmaxHRminDifference")
hist(dataLow$HRmaxHRminDifference,main="histograma of Low data HRmaxHRminDifference")

#plots#####################################################################################

#type-TLX 
par(mfrow=c(1,3))
boxplot(dataLow$TLX.Overall ,main="Low" ,ylim = c(0, 100),ylab="TLX")
boxplot(dataMedium$TLX.Overall ,main="Medium",ylim = c(0, 100),ylab="TLX")
boxplot(dataHigh$TLX.Overall,main="High",ylim = c(0, 100),ylab="TLX")
#type-SWAT 
par(mfrow=c(1,3))
boxplot(dataLow$swat.rank ,main="Low" ,ylim = c(0, 27),ylab="swat rank")
boxplot(dataMedium$swat.rank ,main="Medium",ylim = c(0, 27),ylab="swat rank")
boxplot(dataHigh$swat.rank,main="High",ylim = c(0, 27),ylab="swat rank")

#HRV distribution plot
par(mfrow=c(1,1))
plot(data$Type,data$HRV_div_aveHR,ylim = c(0, 0.05),ylab="HRV",xlab="Type",main="HRV distribution plot")

#MHR distribution plot
par(mfrow=c(1,1))
plot(data$Type,data$MHR,ylim = c(50,100),ylab="MHR",xlab="Type",main="MHR distribution plot")

#MRR distribution plot
par(mfrow=c(1,1))
plot(data$Type,data$MRR,ylim = c(500,1500),ylab="MRR",xlab="Type",main="MRR distribution plot")

##ggplot
library(ggplot2)
#ggplot(data, aes(HRV_div_aveHR, colour =Type )) + stat_ecdf()
ggplot(data[data$HRV_div_aveHR < 0.25, ], aes(HRV_div_aveHR, colour = Type)) + stat_ecdf()

#ggplot(data[data$MHR , ], aes(MHR, colour = Type)) + stat_ecdf()
#ggplot(data = data$MHR, mapping = aes(), environment = parent.frame())

#hist plot of low medium high
par(mfrow=c(3,1))
hist(dataLow$HRV ,ylim = c(1, 20),xlim = c(0, 6),main="Low", xlab = "HRV")
hist(data_Medium$HRV,ylim = c(1, 20),xlim = c(0, 6),main="Medium" , xlab = "HRV")
hist(data_High$HRV ,ylim = c(1,20),xlim = c(0, 6),main="High", xlab = "HRV")

#corelation###########################################################################

#dtat for corelation
dataLow_Cor <- dataLow[c("MRR","MHR","HRV","RMSSD","SDNN","HRmaxHRminDifference","SDRR","HRV_div_aveHR","HRV_div_aveHR_MoveLast15","last5secHRave_div_aveHR","last10secHRave_div_aveHR","last15secHRave_div_aveHR","swat.rank","TLX.Overall")]
dataMedium_Cor <- dataMedium[c("MRR","MHR","HRV","RMSSD","SDNN","HRmaxHRminDifference","SDRR","HRV_div_aveHR","HRV_div_aveHR_MoveLast15","last5secHRave_div_aveHR","last10secHRave_div_aveHR","last15secHRave_div_aveHR","swat.rank","TLX.Overall")]
dataHigh_Cor <- dataHigh[c("MRR","MHR","HRV","RMSSD","SDNN","HRmaxHRminDifference","SDRR","HRV_div_aveHR","HRV_div_aveHR_MoveLast15","last5secHRave_div_aveHR","last10secHRave_div_aveHR","last15secHRave_div_aveHR","swat.rank","TLX.Overall")]
dataAll_Cor <- data[c("MRR","MHR","HRV","RMSSD","SDNN","HRmaxHRminDifference","SDRR","HRV_div_aveHR","HRV_div_aveHR_MoveLast15","last5secHRave_div_aveHR","last10secHRave_div_aveHR","last15secHRave_div_aveHR","swat.rank","TLX.Overall")]

cor_Low <- cor(dataAll_Cor ,method ="spearman")
cor_Medium <- cor(dataMedium_Cor,method ="spearman")
cor_High <- cor(dataHigh_Cor,method ="spearman")
cor_All <- cor(datAll_Cor,method ="spearman")

write.csv(cor_Low,"C:/Users/shir/Dropbox/projectData/dataCor.csv")

#single corelation 
cor(data$HRV, data$swat.rank, method = c("spearman"))
cor(datAll_Cor$HRV, datAll_Cor$TLX.Overall, method = c("spearman"))

cor(datAll_Cor$MRR, datAll_Cor$swat.rank, method = c("spearman"))
cor(datAll_Cor$MRR, datAll_Cor$TLX.Overall, method = c("spearman"))

cor(datAll_Cor$MHR, datAll_Cor$swat.rank, method = c("spearman"))
cor(datAll_Cor$MHR, datAll_Cor$TLX.Overall, method = c("spearman"))


##day difference########################################################
dataMorning <- data[data$Day=="Morning",c("HRV","swat.rank","TLX.Overall","Day")]
dataNoon <- data_clean_All[data_clean_All$Day=="Noon",c("HR_N","HRV","swat.rank","TLX.Overall","Day")]
dataEvening <- data_clean_All[data_clean_All$Day=="Evening",c("HR_N","HRV","swat.rank","TLX.Overall","Day")]

par(mfrow=c(1,1))
plot(data$Day,data$HRV,ylab="HRV",xlab="day time",ylim=c(0,6),main="all data")
plot(dataLow$Day,dataLow$HRV,ylab="HRV",xlab="day time",ylim=c(0,6),main="Low data")
plot(dataMedium$Day,dataMedium$HRV,ylab="HRV",xlab="day time",ylim=c(0,6),main="Medium data")
plot(dataHigh$Day,dataHigh$HRV,ylab="HRV",xlab="day time",ylim=c(0,6),main="High data")

par(mfrow=c(3,1))
hist(dataMorning$HRV,xlab="HRV",main="Morning",ylim=c(0,2000))
hist(dataNoon$HRV,xlab="HRV",main="Noon",ylim=c(0,60))
hist(dataEvening$HRV,xlab="HRV",main="Evening",ylim=c(0,60))

shapiro.test(dataMorning$HRV)
shapiro.test(dataNoon$HRV)
shapiro.test(dataEvening$HRV)


##table of mean +- standard errror ########################################################

cat("MRR Low:",mean(dataLow$MRR),"-+",sd(dataLow$MRR)/sqrt(length(dataLow$MRR)))
cat("MRR Medium:",mean(dataMedium$MRR),"-+",sd(dataMedium$MRR)/sqrt(length(dataMedium$MRR)))
cat("MRR High:",mean(dataHigh$MRR),"-+",sd(dataHigh$MRR)/sqrt(length(dataHigh$MRR)))

cat("MHRLow:",mean(dataLow$MHR),"-+",sd(dataLow$MHR)/sqrt(length(dataLow$MHR)))
cat("MHR Medium:",mean(dataMedium$MHR),"-+",sd(dataMedium$MHR)/sqrt(length(dataMedium$MHR)))
cat("MHR High:",mean(dataHigh$MHR),"-+",sd(dataHigh$MHR)/sqrt(length(dataHigh$MHR)))

cat("HRV Low:",mean(dataLow$HRV),"-+",sd(dataLow$HRV)/sqrt(length(dataLow$HRV)))
cat("HRV Medium:",mean(dataMedium$HRV),"-+",sd(dataMedium$HRV)/sqrt(length(dataMedium$HRV)))
cat("HRV High:",mean(dataHigh$HRV),"-+",sd(dataHigh$HRV)/sqrt(length(dataHigh$HRV)))

cat("HRV Low:",mean(dataLow$HRV),"-+",sd(dataLow$HRV)/sqrt(length(dataLow$HRV)))
cat("HRV Medium:",mean(dataMedium$HRV),"-+",sd(dataMedium$HRV)/sqrt(length(dataMedium$HRV)))
cat("HRV High:",mean(dataHigh$HRV),"-+",sd(dataHigh$HRV)/sqrt(length(dataHigh$HRV)))

cat("RMSSD Low:",mean(dataLow$RMSSD),"-+",sd(dataLow$RMSSD)/sqrt(length(dataLow$RMSSD)))
cat("RMSSD Medium:",mean(dataMedium$RMSSD),"-+",sd(dataMedium$RMSSD)/sqrt(length(dataMedium$RMSSD)))
cat("RMSSD High:",mean(dataHigh$RMSSD),"-+",sd(dataHigh$RMSSD)/sqrt(length(dataHigh$RMSSD)))

cat("SDNN Low:",mean(dataLow$SDNN),"-+",sd(dataLow$SDNN)/sqrt(length(dataLow$SDNN)))
cat("SDNN Medium:",mean(dataMedium$SDNN),"-+",sd(dataMedium$SDNN)/sqrt(length(dataMedium$SDNN)))
cat("SDNN High:",mean(dataHigh$SDNN),"-+",sd(dataHigh$SDNN)/sqrt(length(dataHigh$SDNN)))

cat("HRmaxHRminDifference Low:",mean(dataLow$HRmaxHRminDifference),"-+",sd(dataLow$HRmaxHRminDifference)/sqrt(length(dataLow$HRmaxHRminDifference)))
cat("HRmaxHRminDifference Medium:",mean(dataMedium$HRmaxHRminDifference),"-+",sd(dataMedium$HRmaxHRminDifference)/sqrt(length(dataMedium$HRmaxHRminDifference)))
cat("HRmaxHRminDifference High:",mean(dataHigh$HRmaxHRminDifference),"-+",sd(dataHigh$HRmaxHRminDifference)/sqrt(length(dataHigh$HRmaxHRminDifference)))

cat("SDRR Low:",mean(dataLow$SDRR),"-+",sd(dataLow$SDRR)/sqrt(length(dataLow$SDRR)))
cat("SDRR Medium:",mean(dataMedium$SDRR),"-+",sd(dataMedium$SDRR)/sqrt(length(dataMedium$SDRR)))
cat("SDRR High:",mean(dataHigh$SDRR),"-+",sd(dataHigh$SDRR)/sqrt(length(dataHigh$SDRR)))

cat("HRV_div_aveHR Low:",mean(dataLow$HRV_div_aveHR),"-+",sd(dataLow$HRV_div_aveHR)/sqrt(length(dataLow$HRV_div_aveHR)))
cat("HRV_div_aveHR Medium:",mean(dataMedium$HRV_div_aveHR),"-+",sd(dataMedium$HRV_div_aveHR)/sqrt(length(dataMedium$HRV_div_aveHR)))
cat("HRV_div_aveHR High:",mean(dataHigh$HRV_div_aveHR),"-+",sd(dataHigh$HRV_div_aveHR)/sqrt(length(dataHigh$HRV_div_aveHR)))

cat("HRV_div_aveHR_MoveLast15 Low:",mean(dataLow$HRV_div_aveHR_MoveLast15),"-+",sd(dataLow$HRV_div_aveHR_MoveLast15)/sqrt(length(dataLow$HRV_div_aveHR_MoveLast15)))
cat("HRV_div_aveHR_MoveLast15 Medium:",mean(dataMedium$HRV_div_aveHR_MoveLast15),"-+",sd(dataMedium$HRV_div_aveHR_MoveLast15)/sqrt(length(dataMedium$HRV_div_aveHR_MoveLast15)))
cat("HRV_div_aveHR_MoveLast15 High:",mean(dataHigh$HRV_div_aveHR_MoveLast15),"-+",sd(dataHigh$HRV_div_aveHR_MoveLast15)/sqrt(length(dataHigh$HRV_div_aveHR_MoveLast15)))

cat("last5secHRave_div_aveHR Low:",mean(dataLow$last5secHRave_div_aveHR),"-+",sd(dataLow$last5secHRave_div_aveHR)/sqrt(length(dataLow$last5secHRave_div_aveHR)))
cat("last5secHRave_div_aveHR Medium:",mean(dataMedium$last5secHRave_div_aveHR),"-+",sd(dataMedium$last5secHRave_div_aveHR)/sqrt(length(dataMedium$last5secHRave_div_aveHR)))
cat("last5secHRave_div_aveHR:",mean(dataHigh$last5secHRave_div_aveHR),"-+",sd(dataHigh$last5secHRave_div_aveHR)/sqrt(length(dataHigh$last5secHRave_div_aveHR)))

cat("last10secHRave_div_aveHR Low:",mean(dataLow$last10secHRave_div_aveHR),"-+",sd(dataLow$last10secHRave_div_aveHR)/sqrt(length(dataLow$last10secHRave_div_aveHR)))
cat("last10secHRave_div_aveHR Medium:",mean(dataMedium$last10secHRave_div_aveHR),"-+",sd(dataMedium$last10secHRave_div_aveHR)/sqrt(length(dataMedium$last10secHRave_div_aveHR)))
cat("last10secHRave_div_aveHR High:",mean(dataHigh$last10secHRave_div_aveHR),"-+",sd(dataHigh$last10secHRave_div_aveHR)/sqrt(length(dataHigh$last10secHRave_div_aveHR)))

cat("last15secHRave_div_aveHR Low:",mean(dataLow$last15secHRave_div_aveHR),"-+",sd(dataLow$last15secHRave_div_aveHR)/sqrt(length(dataLow$last15secHRave_div_aveHR)))
cat("last15secHRave_div_aveHR Medium:",mean(dataMedium$last15secHRave_div_aveHR),"-+",sd(dataMedium$last15secHRave_div_aveHR)/sqrt(length(dataMedium$last15secHRave_div_aveHR)))
cat("last15secHRave_div_aveHR High:",mean(dataHigh$last15secHRave_div_aveHR),"-+",sd(dataHigh$last15secHRave_div_aveHR)/sqrt(length(dataHigh$last15secHRave_div_aveHR)))


##Heart rate for each subject Time Series ##########################################################
setwd("C:/Users/shir/Dropbox/projectData")
Sdata <- read.csv("all_data_A_15sec.csv") 

dataHM <- Sdata[Sdata$Type=="High",c("MHR","Day")]
dataHM <- dataHM[dataHM$Day=="Morning",c("MHR")]
dataHN <- Sdata[Sdata$Type=="High",c("MHR","Day")]
dataHN <- dataHN[dataHN$Day=="Noon",c("MHR")]
dataHE <- Sdata[Sdata$Type=="High",c("MHR","Day")]
dataHE <- dataHE[dataHE$Day=="Evening",c("MHR")]
dataMM <- Sdata[Sdata$Type=="Medium",c("MHR","Day")]
dataMM <- dataMM[dataMM$Day=="Morning",c("MHR")]
dataMN <- Sdata[Sdata$Type=="Medium",c("MHR","Day")]
dataMN <- dataMN[dataMN$Day=="Noon",c("MHR")]
dataME <- Sdata[Sdata$Type=="Medium",c("MHR","Day")]
dataME <- dataME[dataME$Day=="Evening",c("MHR")]
dataLM <- Sdata[Sdata$Type=="Low",c("MHR","Day")]
dataLM <- dataLM[dataLM$Day=="Morning",c("MHR")]
dataLN <- Sdata[Sdata$Type=="Low",c("MHR","Day")]
dataLN <- dataLN[dataLN$Day=="Noon",c("MHR")]
dataLE <- Sdata[Sdata$Type=="Low",c("MHR","Day")]
dataLE <- dataLE[dataLE$Day=="Evening",c("MHR")]

par(mfrow=c(3,3))
plot(dataHM,pch =20, xlab= "time", ylab= "MHR" ,main = "MHR High Morning")
lines(dataHM)
plot(dataHN,pch =20, xlab= "time", ylab= "MHR",main = "MHR High Noon")
lines(dataHN)
plot(dataHE,pch =20, xlab= "time", ylab= "MHR",main = "MHR High Evening")
lines(dataHE)

plot(dataMM,pch =20, xlab= "time", ylab= "MHR",main = "MHR Medium Morning")
lines(dataMM)
plot(dataMN,pch =20, xlab= "time", ylab= "MHR",main = "MHR Medium Noon")
lines(dataMN)
plot(dataME,pch =20, xlab= "time", ylab= "MHR",main = "MHR Medium Evening")
lines(dataME)

plot(dataLM,pch =20, xlab= "time", ylab= "MHR",main = "MHR Low Morning")
lines(dataLM)
plot(dataLN,pch =20, xlab= "time", ylab= "MHR",main = "MHR Low Noon")
lines(dataLN)
plot(dataLE,pch =20, xlab= "time", ylab= "MHR",main = "MHR Low Evening")
lines(dataLE)

#plot relationship between all measures to TLX and SWAT #############################################################################

#TLX 
par(mfrow=c(1,1))
plot(data$TLX.Overall,data$MRR)
plot(data$TLX.Overall,data$MHR)
plot(data$TLX.Overall,data$HRV)
plot(data$TLX.Overall,data$RMSSD)
plot(data$TLX.Overall,data$SDNN)
plot(data$TLX.Overall,data$HRmaxHRminDifference)
plot(data$TLX.Overall,data$SDRR)
plot(data$TLX.Overall,data$HRV_div_aveHR)
plot(data$TLX.Overall,data$HRV_div_aveHR_MoveLast15)
plot(data$TLX.Overall,data$last5secHRave_div_aveHR)
plot(data$TLX.Overall,data$last10secHRave_div_aveHR)
plot(data$TLX.Overall,data$last15secHRave_div_aveHR)

#SWAT 
par(mfrow=c(1,1))
plot(data$swat.rank,data$MRR)
plot(data$swat.rank,data$MHR)
plot(data$swat.rank,data$HRV)
plot(data$swat.rank,data$RMSSD)
plot(data$swat.rank,data$SDNN)
plot(data$swat.rank,data$HRmaxHRminDifference)
plot(data$swat.rank,data$SDRR)
plot(data$swat.rank,data$HRV_div_aveHR)
plot(data$swat.rank,data$HRV_div_aveHR_MoveLast15)
plot(data$swat.rank,data$last5secHRave_div_aveHR)
plot(data$swat.rank,data$last10secHRave_div_aveHR)
plot(data$swat.rank,data$last15secHRave_div_aveHR)


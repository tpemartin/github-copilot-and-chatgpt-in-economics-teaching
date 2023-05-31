
# 資料

  * [111年傷亡道路交通事故資料](https://data.gov.tw/dataset/161199)

## Import data

```r
# csv data url
dataUrl = "https://www-api.moda.gov.tw/OpenData/Files/4437"

# download data
download.file(dataUrl, destfile = "data.csv")

# import data 
data = read.csv("data.csv", fileEncoding = "UTF-8-BOM")
```
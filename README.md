# DeAPIed
Dehashed scraping tool to extract data from burp responses

## How to use
1) Browse dehashed using burpsuite, click on all the entries you want so that burp can store the json response.
2) Filter all responses that have this format: `/search/<DEHASHED ID>`. They contain the response with the data we want to scrape.
3) Select all requests to extract in burp. Save them to a file. DO NOT encode them in base64.
4) This is not an automatic tool (too lazy), so read the script and modify the parameters accordingly to your preferences. Input and Output filenames are hardcoded into the script (again, too lazy).
5) Run the script: `deAPIed.py`. The data will be converted and written to the file of your choice.


:)

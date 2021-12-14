# satrix_etf
A python script for comparing ETF's from Satrix (https://www.satrix.co.za/products)

About a year or so ago I got introduced to Satrix Investments and took the plunge into ETF investing. Satrix offers more than maybe 20 ETFs and Unit Trusts to choose from. Their website allows comparisons accross only 2 selected instruments, across various metrics. I am a novice already so anything that required me to choose 1 or 2 instruments to start off with from a basket of about 20 was always going to be daunting. Nevermind the terminology I had to learn that was in the Mininimum Disclosure Documents that I also needed to familiarise with. 

So what's a young novice guy, interested in starting off investing in ETF's first, with no understanding what TER is, or what Annualised perfomance means, or why portfolio size is a metric that matters to do? Well browse through all the names of the ETF's of course and just make random selections. I started off with the JSE Top 40, for the sake of patriotism (maybe not the best investment criterion), the MSCI Emerging Markets, to get some exposure to China, and at the time MSCI World, because it tracked a few big names. But the engineer in me always believed there should have been a better way to collect all of this data and have a more rigorous analysis, informed by data collected from these MDDs. 

So in the last 30 or so days, I got started on my Pandas, BeautifulSoup, requests and requests_html. This is the result of that work. 

1) The first step is to set an investment philosophy, and identify the metrics best suited to reflect my chosen investment philosophy from the fund metrics that are presented in the MDD.pdfs. 
2) The second step is to get started on writing python scripts to scrap all of the MDD .pdf files from the satrix.co.za/products page. 
3) Stage 2 is to extract all of the data from the downloaded MDD.pdfs into a Pandas DataFrame, and then using the chosen metrics from stage 1 to reflect the desired investment philosophy, create some kind of an algorithm to assist in decision making and then coding it. 
4) Stage 3, (perhaps the most difficult), is to then commit to making monthly purchases of whichever ETFs will be recommended by the data based on this endevour. 

Needless to say, this is pretty much be for improving my Python and problem solvinf skills than it is for ETF picking. My previous boss always said you don't improve your coding by doing more tutorials you find a project and commit to it to the end. So here goes.

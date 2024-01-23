import pandas as pd

URL = {
    "Satrix Top 40": "https://satrix.co.za/products/product-details?id=44",
    "Satrix MSCI World": "https://satrix.co.za/products/product-details?id=33",
    #    "Satrix Balanced ": "https://satrix.co.za/products/product-details?id=29",
    "Satrix Money Market": "https://satrix.co.za/products/product-details?id=40",
    "Satrix DIVI": "https://satrix.co.za/products/product-details?id=22",
    "Satrix FINI": "https://satrix.co.za/products/product-details?id=23",
    "Satrix INDI": "https://satrix.co.za/products/product-details?id=24",
    "Satrix RESI": "https://satrix.co.za/products/product-details?id=27",
    "Satrix RAFI": "https://satrix.co.za/products/product-details?id=25",
    "Satrix SWIX 40": "https://satrix.co.za/products/product-details?id=26",
    "Satrix ALSI": "https://satrix.co.za/products/product-details?id=28",
    "Satrix Capped Swix ALSI": "https://satrix.co.za/products/product-details?id=47",
    "Satrix Local Bond": "https://satrix.co.za/products/product-details?id=31",
    "Satrix ILBI": "https://satrix.co.za/products/product-details?id=43",
    "Satrix Momentum": "https://satrix.co.za/products/product-details?id=34",
    "Satrix Quality": "https://satrix.co.za/products/product-details?id=36",
    "Satrix Equally Weighted Top 40": "https://satrix.co.za/products/product-details?id=32",
    #"Satrix SmartCore™": "https://satrix.co.za/products/product-details?id=53",
    "Satrix TRACI": "https://satrix.co.za/products/product-details?id=91",
    "Satrix MSCI Emerging Markets": "https://satrix.co.za/products/product-details?id=45",
    "Satrix GOVI": "https://satrix.co.za/products/product-details?id=84",
    "Satrix MAPPS Growth": "https://satrix.co.za/products/product-details?id=92",
    "Satrix S&amp;P 500": "https://satrix.co.za/products/product-details?id=46",
    "Satrix Shari'ah Top 40": "https://satrix.co.za/products/product-details?id=87",
    "Satrix MAPPS Protect": "https://satrix.co.za/products/product-details?id=93",
    "Satrix Nasdaq 100": "https://satrix.co.za/products/product-details?id=51",
    "Satrix S&amp;P GIVI SA Top 50": "https://satrix.co.za/products/product-details?id=88",
    "Satrix Low Volatility": "https://satrix.co.za/products/product-details?id=94",
    "Satrix Mid Cap": "https://satrix.co.za/products/product-details?id=50",
    "Satrix Value Equity": "https://satrix.co.za/products/product-details?id=95",
    "Satrix Inflation-Linked Bond": "https://satrix.co.za/products/product-details?id=86",
    "Satrix Equity Momentum": "https://satrix.co.za/products/product-details?id=89",
    "Satrix Property": "https://satrix.co.za/products/product-details?id=35",
    "Satrix Low Equity Balanced": "https://satrix.co.za/products/product-details?id=30",
    "Satrix MSCI China": "https://satrix.co.za/products/product-details?id=60",
    "Satrix Global Bond": "https://satrix.co.za/products/product-details?id=61",
    "Satrix S&amp;P Namibia Bond": "https://satrix.co.za/products/product-details?id=100",
    "Satrix MSCI World ESG": "https://satrix.co.za/products/product-details?id=62",
    "Satrix MSCI Emerging Markets ESG": "https://satrix.co.za/products/product-details?id=63",
    "Satrix Global Infrastructure": "https://satrix.co.za/products/product-details?id=65",
    "Satrix Healthcare Innovation": "https://satrix.co.za/products/product-details?id=69",
    "Satrix Inclusion and Diversity": "https://satrix.co.za/products/product-details?id=64",
    "Satrix Capped All Share": "https://satrix.co.za/products/product-details?id=66",
    "Satrix MSCI India": "https://satrix.co.za/products/product-details?id=68",
    "Satrix Smart City Infrastructure": "https://satrix.co.za/products/product-details?id=71",
}

for fund, url in URL.items():
    print(fund)
    # Read HTML tables from the webpage
    tables = pd.read_html(url)

    # Check if any tables were found
    if tables:
        # Assume the first table is the one you want
        df = tables[2]

        # Print the DataFrame
        print(df)
    else:
        print("No tables found on the page.")


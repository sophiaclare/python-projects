import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def read_data():
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        data = []
        for row in spreadsheet:
            data.append(row)
    return data


def run():
    data = read_data()

    sales = []
    months = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)
        month = row['month']
        months.append(month)

    # Calculate total sales across all months
    total_sales = sum(sales)

    # Calculate the average sales
    average_sales = round(sum(sales) / len(sales), 1)

    # Find the month with the highest sales
    highest_month = months[sales.index(max(sales))]

    # Find the month with the lowest sales
    lowest_month = months[sales.index(min(sales))]

    # Calculate monthly changes as a percentage
    monthly_changes = []
    for i in range(1, len(sales)):
        change = (sales[i] - sales[i - 1]) / sales[i - 1] * 100
        monthly_changes.append(round(change, 1))

    # Create a Pandas DataFrame of the sales data
    sales_data = pd.DataFrame({'Month': months, 'Sales': sales})

    # Create a bar chart of the sales by month
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(sales_data['Month'], sales_data['Sales'], color='#006699', edgecolor='#333333', linewidth=1.5)
    ax.set_xlabel('Month', fontsize=12)
    ax.set_ylabel('Sales', fontsize=12)
    ax.set_title('Monthly Sales', fontsize=16, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add trend line to the bar chart
    x = np.arange(len(sales_data))
    z = np.polyfit(x, sales_data['Sales'], 1)
    p = np.poly1d(z)
    ax.plot(x, p(x), color='r')

    # Add data labels to the bars
    for i, v in enumerate(sales_data['Sales']):
        ax.text(i, v + 100, '$ {:,.0f}'.format(v), color='#333333', fontweight='bold', ha='center', fontsize=10)

    plt.show()

    # Print the results
    print('Total sales across all months: ${:,.0f}'.format(total_sales))
    print('Average sales: ${:,.1f}'.format(total_sales / len(sales)))
    print('Month with the highest sales: {}'.format(highest_month))
    print('Month with the lowest sales: {}'.format(lowest_month))
    print('Monthly changes as a percentage: {}'.format(['{}%'.format(round(change, 1)) for change in [(sales[i] - sales[i-1])/sales[i-1] * 100 for i in range(1, len(sales))]]))

    # Calculate the proportion of sales for each month
    proportions = [sale / total_sales for sale in sales]

    # Create a Pandas DataFrame of the sales data
    sales_data = pd.DataFrame({'Month': months, 'Proportion': proportions})



    # Create a pie chart of the sales by month
    fig, ax = plt.subplots(figsize=(8, 8))
    colors = ['#007ACC', '#009933', '#CC6600', '#FFCC00', '#993399', '#FF9999', '#66CCCC', '#6600CC', '#99CC00', '#FF6600', '#CC0033', '#003300']
    ax.pie(sales_data['Proportion'], labels=sales_data['Month'], autopct='%1.1f%%', startangle=90,
           textprops={'fontsize': 8, 'color': 'white'}, colors=colors, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})

    # Add a legend to the chart
    plt.legend(sales_data['Month'], loc='upper right', bbox_to_anchor=(1.1, 1), fontsize=12)

    # Add a title to the chart
    ax.set_title('Monthly Sales Proportions', fontsize=16, fontweight='bold')

    # Make the pie chart circular
    ax.axis('equal')

    plt.tight_layout()
    plt.show()

run()
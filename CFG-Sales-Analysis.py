import csv
import pandas as pd
import matplotlib.pyplot as plt


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
    ax = sales_data.plot.bar(x='Month', y='Sales', legend=False)
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')

    plt.show()

    # Print the results
    print('Total sales across all months: ${}'.format(total_sales))
    print('Average sales: ${}'.format(average_sales))
    print('Month with the highest sales: {}'.format(highest_month))
    print('Month with the lowest sales: {}'.format(lowest_month))
    print('Monthly changes as a percentage: {}'.format(['{}%'.format(change) for change in monthly_changes]))


run()

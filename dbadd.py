from openpyxl import load_workbook
import pandas as pd


def dbadd(node1, node2):   
    # Load an Excel file
    wb = load_workbook('edge_cons.xlsx')

    # Select the first sheet
    ws = wb.active

    # Add a new row
    ws.append([node1.upper(), node2.upper()])

    # Save the Excel file
    wb.save('edge_cons.xlsx')


# Load an Excel file into a DataFrame
df = pd.read_excel('edge_cons.xlsx')

x = False
while x == False:
    node1 = input("Enter first node or 'q' to quit: ")
    if node1.upper() == "Q":
        print("Take Care!")
        x = True
        continue
    node2 = input("Enter second node: ")

    if not(df[(df['First'] == node1.upper()) & (df['Second'] == node2.upper())].empty) or not(df[(df['First'] == node2.upper()) & (df['Second'] == node1.upper())].empty) == True:
        continue

    dbadd(node1, node2)


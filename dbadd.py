from openpyxl import load_workbook


def dbadd(node1, node2):   
    # Load an Excel file
    wb = load_workbook('edge_cons.xlsx')

    # Select the first sheet
    ws = wb.active

    # Add a new row
    ws.append([node1.upper(), node2.upper()])

    # Save the Excel file
    wb.save('edge_cons.xlsx')

x = False
while x == False:
    node1 = input("Enter first node or 'q' to quit: ")
    if node1.upper() == "Q":
        x = True
        continue
    node2 = input("Enter second node: ")
    dbadd(node1, node2)
# python package indetable: https://pypi.org/
# pretty table: https://pypi.org/project/prettytable/
# install > preferences > settings > project (with the name of project) > project interpreter >
    # > + > search for prettytable by Luke Maurits > install package >

#from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes

#table = PrettyTable()
table = ColorTable(theme=Themes.OCEAN)
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", 1295, 1158259, 600.5])
table.add_row(["Brisbane", 5905, 1857594, 1146.4])
table.add_row(["Darwin", 112, 120900, 1714.7])
table.add_row(["Hobart", 1357, 205556, 619.5])
table.add_row(["Sydney", 2058, 4336374, 1214.8])
table.add_row(["Melbourne", 1566, 3806092, 646.9])
table.add_row(["Perth", 5386, 1554769, 869.4])

print(table)

table2 = ColorTable(theme=Themes.OCEAN)
table2.header_style = "upper" # upercase
table2.align = "l" # align to left
table2.add_column("Pockemon Name", ["Combee", "Charmandeer", "Pikachu"])
table2.add_column("Type", ["Electric", "Water", "Fire"])

print(table2)
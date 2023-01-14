## Tunnel Vibes

from tunnels_cls import Node, Graph, Edge

MC = Node("MC")
SLC = Node("SLC")
PAC = Node("PAC")
STC = Node("STC")
QNC = Node("QNC")
AL = Node("AL")
ML = Node("ML")
PHYS = Node("PHYS")
DP = Node("DP")
DC = Node("DC")
E2 = Node("E2")
E3 = Node("E3")
E5 = Node("E5")
E7 = Node("E7")
RCH = Node("RCH")
C2 = Node("C2")
DWE = Node("DWE")
HH = Node("HH")




edge1 = Edge(MC,PAC)
edge2 = Edge(MC,SLC)
edge3 = Edge(DC, MC)
edge4 = Edge(E3, E5)
edge5 = Edge(RCH, DWE)
edge6 = Edge(E2, DWE)
edge7 = Edge(E3, DC)
edge8 = Edge(C2, DC)


# is_connected(MC,SLC)
PAC.printcons()

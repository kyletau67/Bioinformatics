
#Pairs
P1, P2, P3, P4, P5, P6 = 19758, 16435, 19805, 17160, 18560, 18049

#Expected probability of dominance for offspring of each pair
E1, E2, E3 = 2, 2, 2                                  
E4 = 2 * 0.75                                         
E5 = 2 * 0.5

E = E1 * P1 + E2 * P2 + E3 * P3 + E4 * P4 + E5 * P5   
print(E)     
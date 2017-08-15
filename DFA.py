from igraph import *

transistion_table=[];
n=input("Enter the number of States: ");
i=0
while(i<n):
    L=[]
    L.append(input("Q[%d] on '0' goes to state: " %(i)))
    if(L[0]>=n):
        print("ERROR: There is no State number %d\n" %(L[0]))
        continue
    L.append(input("Q[%d] on '1' goes to state: " %(i)))
    if(L[1]>=n):
        print("ERROR: There is no State number %d\n" %(L[1]))
        continue
    L.append(0)
    transistion_table.append(L)
    i=i+1
    print

while(1):
    nf=input("Enter Number of Final States: ")
    if(nf<=n):
        break
    print("ERROR: Number of Final states cannot be more than the total number of states")
i=0
while(i<nf):
    f=input("Enter Final State %d: " %(i+1))
    if(f>n):
        print("There are only %d States" %(n))
        continue
    transistion_table[f][2]=1;
    i=i+1

print("Here is the transistion table:")
print("STATE\t|\tOn '0'\t|\tOn '1'\t| Final State")
print("--------+---------------+---------------+--------------")
for i in range(0,n):
    temp="Not Final"
    if(transistion_table[i][2]==1):
        temp="Final"
    print("Q[%d]\t|\t%d\t|\t%d\t| %s" %(i,transistion_table[i][0],transistion_table[i][1],temp))

while(1):
    start=input("\nEnter Starting State: ")
    if(start<n):
        break
    print("ERROR: There are only %d States" %(n))

while(1):
    test_string=raw_input("\nEnter String to be Checked")
    flag=False
    for i in test_string:
        if(i!="1" and i!="0"):
            flag=True
    if(flag==False):
        break
    print("String can only be a combination of 0's and 1's")

test_array=[]
for i in range(0,len(test_string)):
    test_array.append(int(test_string[i]))

state=start
for i in range(0,len(test_string)):
    state=transistion_table[state][test_array[i]]
    print("Q[%d]->" % (state)),

if(transistion_table[state][2]==1):
    print("Accepted")
else:
    print("Rejected")

#Plotting The DFA
vertices=[]
for i in range(0,n):
    vertices.append(i)
edges=[]
for i in range(0,len(transistion_table)):
    edges.append((i,transistion_table[i][0]))
    edges.append((i,transistion_table[i][1]))
vertex_color=[]
for i in transistion_table:
    if(i[2]==1):
        vertex_color.append("RED")
    else:
        vertex_color.append("GREEN")

g = Graph(vertex_attrs={"label": vertices, "color": vertex_color,"size":30}, edges=edges, directed=True)
plot(g)

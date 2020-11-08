import networkx as nx
import matplotlib.pyplot as plt
#%matplotlib inline
link_for_graph="https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/"
graph={
    '0':{'1':4,'7':8},
    '1':{'0':4,'7':11,'2':8},
    '2':{'8':2,'3':7,'5':4,'1':8},
    '3':{'2':7,'5':14,'4':9},
    '4':{'3':9,'5':10},
    '5':{'4':10,'3':14,'2':4,'6':2},
    '6':{'8':6,'5':2,'7':1},
    '7':{'6':1,'8':7,'1':11,'0':8},
    '8':{'2':2,'6':6,'7':7}
}

def visualisation():
    G=nx.Graph()
    G.add_nodes_from(graph)
    nx.draw(G)
    plt.draw()
    plt.show()
def Djikstra(A_list,s_node,e_node):
    #visualizing
    #visualisation()

    node_cost=float('inf')
    unvisited_node=[i for i in graph.keys()]
 
    graph_keys=unvisited_node.copy()
    index_of_s_node=unvisited_node.index(s_node)
    #print('index_of_s_node : ',index_of_s_node)
    
    index_of_e_node=unvisited_node.index(e_node)
    #print('index_of_e_node : ',index_of_e_node)
    A_list_inf=[]
    
    for i in graph.keys():
        A_list_inf.append([graph.get(i).get(keys,node_cost) for keys in graph]) #for infinity values to indirect vertices

    A_list_current=A_list_inf[index_of_s_node].copy() #it will be the final array of all nodes cost
    A_list_current_rough=A_list_current.copy()  #just for finding next minimum cost

    stack=dict() #for path saving

    
    #Main Working of Djikstra
    
    for i in range (len(unvisited_node)):
        
        current_node=A_list_current_rough.index(min(A_list_current_rough)) #next minimum entry

        node_cost=A_list_current[current_node]

        for index,values in enumerate(A_list_inf[current_node]):
            


            if node_cost+values<A_list_current[index]:

                A_list_current[index]=node_cost+values
                A_list_current_rough[index]=node_cost+values #increment of cost recursively w.r.t previous node
                if  stack.get(current_node)==None:
                    stack[current_node]=[unvisited_node[index]]
                else:
                    stack[current_node].append(unvisited_node[index])
        
        A_list_current_rough[current_node]=float('inf') #so that a used node will not be used again, as we only want minimum
        

    #finding path now
    stack_keys=[i for i in stack.keys()] 
    back_track=str(e_node)
    path=str(e_node)
    for i in stack_keys[::-1]:
        if back_track in stack.get(i):
            path+=str(i)
            back_track=str(i)
    path+=str(s_node)
                        
        

    print("Shortest Path is : ",path[::-1])
    return A_list_current,A_list_current[graph_keys.index(e_node)]
        




def main():
    print('Djikstra Algo')

    #making Adjacency Algorithm now:
    Adj_list=[]
    for i in graph.keys():
        Adj_list.append([graph.get(i).get(keys,0) for keys in graph.keys()])
    #print(Adj_list)

    #Input without any Anomalies 
    while True:    
        start_node=input("Enter the Starting Node : ")
        if start_node not in graph.keys():
            print("Wrong Node Entered")
            continue
        break
    while True:
        end_node=input("Enter the Ending Node : ")
        if end_node not in graph.keys() or end_node==start_node:
            print("Wrong Node Entered")
            continue
        break
    shortest_path,cost=Djikstra(Adj_list,start_node,end_node)
    print(f'Shortest_path : {shortest_path} where cost to {end_node} node is {cost}',)
if __name__ == "__main__":
    main()
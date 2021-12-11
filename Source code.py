n= int(input())       
arr=[]
for i in range(0,n):
  b=[]
  a = input().split(",")
  for j in range(len(a)-1,-1,-1):
    b.append(j)
  arr.append(b)

dep=[]
for i in range(0,n):
  b = input().split(" ")
  results=[]
  for j in range(0,n):
    results.append(int(b[j]))
  dep.append(results)


m_val = []
m = int(input())
for i in range(0,m):
  a = input().split(",")
  b=[]
  for j in range(0,len(a)):
    if a[j]=='TRUE' or a[j]=='T' or a[j]=='yes' or a[j]=='YES' or a[j]=='Y' or a[j]=='True' or a[j]=='Yes':
      b.append(1)
    elif a[j]!='?':
      b.append(0)
    else:
      b.append(-1)
  m_val.append(b)

list_nodes = []
for i in range(0,n):
  arr =[]
  for j in range(0,m):
    arr.append(m_val[j][i])
  list_nodes.append(arr)

from itertools import product
comb_values=[]
comb_values = list(set(product([0,1],repeat=n)))

parent_list=[]
for i in range(0,n):
  dep_node=[]
  for j in range(0,n):
    if dep[j][i]==1:
      dep_node.append(j)
  parent_list.append(dep_node)

samples=m_val
combination=[]
for comb in comb_values:
  count=0
  for sample in samples:
    k=0
    for i, j in zip(comb, sample):
      if i==j:
        k=k+1
    if k==n:
      count=count+1
  # print(comb)
  n1=list(comb)
  n1.append(count)
  combination.append(n1)

def joint_prob(node, parents):
  values = [1,0]
  result=[]
  for node_val in values:
    given_true=0
    given_false=0
    given_tt=0
    given_tf=0
    given_ft=0
    given_ff=0
    true_count=0
    false_count=0
    if len(parents)==0:
      for val in list_nodes[node]:
        if val==1:
          true_count=true_count+1
        else:
          false_count = false_count+1
      result.append('{0:.4f}'.format(true_count/m))
      result.append('{0:.4f}'.format(false_count/m))
      break


    elif len(parents)==1:
      for n_val,p_val in zip(list_nodes[node],list_nodes[parents[0]]):
        # print(n_val,p_val)
        if n_val==node_val and p_val==1:
          given_true=given_true+1
        elif n_val==node_val and p_val==0:
          given_false = given_false+1
      result.append('{0:.4f}'.format(given_true/m))
      result.append('{0:.4f}'.format(given_false/m))
      
    elif len(parents)==2:
      for n_val,p1_val,p2_val in zip(list_nodes[node],list_nodes[parents[0]],list_nodes[parents[1]]):
        #print(p_val,n_val)
        if n_val==node_val and p1_val==1 and p2_val==1:
          given_tt=given_tt+1
        elif n_val==node_val and p1_val==1 and p2_val==0:
          given_tf=given_tf+1
        elif n_val==node_val and p1_val==0 and p2_val==1:
          given_ft=given_ft+1
        elif n_val==node_val and p1_val==0 and p2_val==0:
          given_ff=given_ff+1
       
      result.append('{0:.4f}'.format(given_tt/m))
      result.append('{0:.4f}'.format(given_tf/m))
      result.append('{0:.4f}'.format(given_ft/m))
      result.append('{0:.4f}'.format(given_ff/m))
  return result

  
    
def expect_num(node,parents,index,node_val):
  count_exp=0
  temp=list_nodes
  for k in range(0,len(temp[node])):
    if temp[node][k]==-1:
      temp[node][k]=node_val
  if len(parents)==1:
    for n_val,p1_val in zip(temp[node],temp[parents[0]]):
      if n_val==node_val and p1_val==temp[parents[0]][index]:
        count_exp=count_exp+1
    # print(count_exp/m)

  else:
    for n_val,p1_val,p2_val in zip(temp[node],temp[parents[0]],temp[parents[1]]):
      if n_val==node_val and p1_val==temp[parents[0]][index] and p2_val==temp[parents[1]][index]:
        count_exp=count_exp+1
  return count_exp/m

def expect_den(parents,index):
  count_exp=0
  temp=list_nodes
  if len(parents)==1:
    for n_val in (temp[parents[0]]):
      if n_val==temp[parents[0]][index]:
        count_exp=count_exp+1
  else:
    for n_val,p_val in zip(temp[parents[0]],temp[parents[1]]):
      if n_val==temp[parents[0]][index] and p_val==temp[parents[1]][index]:
        count_exp=count_exp+1
  return count_exp/m

def cond_prob():
  for i,parent in enumerate(parent_list):
    if -1 not in list_nodes[i]:
      if len(parent)==0:
        result_num=joint_prob(i,parent)
        for j in range(0,len(result_num)):
          print(result_num[j],end=" ")
        print("")

      elif len(parent)==1:
        result_num=joint_prob(i,parent)
        result_den=joint_prob(parent[0],[])
        for i in range(0,2):
          for j in range(0,2):
            if float(result_num[j+i])==0:
              print(result_num[j+i],end=" ")
            else:
              print('{0:.4f}'.format(float(result_num[j+2*i])/float(result_den[j])),end=" ")
      else:
        result_num=joint_prob(i,parent)
        result_den=joint_prob(parent[0],parent[1:])
        for i in range(0,2):
          for j in range(0,4):
            if float(result_num[j+4*i])==0:
              print(result_num[j+4*i],end=" ")
            else:
              print('{0:.4f}'.format(float(result_num[j+4*i])/float(result_den[j])),end=" ")
    else:
      parent=[]
      index = list_nodes[i].index(-1)
      for j in range(0,n):
        if j!=i:
          parent.append(j)
      num_true=expect_num(i,parent,index,1)
      num_false=expect_num(i,parent,index,0)
      denominator=expect_den(parent,index)
      n1 = num_true/denominator
      n2 = num_false/denominator
      if n1>n2:
        for k in range(0,len(list_nodes[i])):
          if list_nodes[i][k]==-1:
            list_nodes[i][k]=1
      else:
        for k in range(0,len(list_nodes[i])):
          if list_nodes[i][k]==-1:
            list_nodes[i][k]=0
            
      result_num=joint_prob(i,parent)
      result_den=joint_prob(parent[0],parent[1:])
      if len(parent)==1:
        for i in range(0,2):
          for j in range(0,2):
            if float(result_num[j+2*i])==0:
                print(result_num[j+2*i],end=" ")
            else:
                print('{0:.4f}'.format(float(result_num[j+2*i])/float(result_den[j])),end=" ")
      else:
        for i in range(0,2):
          for j in range(0,4):
              if float(result_num[j+4*i])==0:
                  print(result_num[j+4*i],end=" ")
              else:
                  print('{0:.4f}'.format(float(result_num[j+4*i])/float(result_den[j])),end=" ")
    

cond_prob()

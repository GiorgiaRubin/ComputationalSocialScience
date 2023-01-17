#General info about the network graph
info=nx.info(network_tweets)
cliq=nx.find_cliques(network_tweets)
cliqes=len(list(cliq))
print(info)
print("Network Cliques:", cliqes)
print("Network Density:", nx.density(network_tweets))
print("Network Diameter:",nx.diameter(network_tweets))

#Degrees for node
user = [node for (node, val) in network_tweets.degree()]
degrees = [val for (node, val) in network_tweets.degree()]
degree_df=pd.DataFrame({"node":user, "degrees":degrees})
degree_df.iloc[np.argsort(degree_df["degrees"])]

#Visualization of the most connected nodes into the network
degree_top=degree_df.loc[degree_df.degrees.nlargest(6).index]
degree_top.plot(x="node", y="degrees", kind="bar", color = "#FF9933")

#Degree centrality 
degree_centrality=nxa.degree_centrality(network_tweets) 
degree_centrality_df=pd.DataFrame({"degree_centrality":degree_centrality})
degree_centrality_df.iloc[np.argsort(degree_centrality_df["degree_centrality"])]

#Betweenness centrality
betweeness=nx.betweenness_centrality(network_tweets)
betweeness_df=pd.DataFrame({"betweeness":betweeness})
betweeness_df.iloc[np.argsort(betweeness_df["betweeness"])]

#Closeness centrality 
closeness=nxa.closeness_centrality(network_tweets)
closeness_df=pd.DataFrame({"closeness":closeness})
closeness_df.iloc[np.argsort(closeness_df["closeness"])]

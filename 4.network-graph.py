import networkx as nx
import networkx.algorithms as nxa
import numpy as np

#Creation of preselected Keywords lists and dataframes
#LIST ETH
eth_user_list = []
eth_tweet_list = []
kw_1 = 'eth'
for tweet in user_tweet:
  if kw_1 in tweet[1]:
    eth_user_list.append(tweet[0])
    eth_tweet_list.append(tweet[1])
  else:
    pass
eth_list_tab = pd.DataFrame ({'User':eth_user_list, "Tweet":eth_tweet_list, 'Tag': kw_1})

#LIST PRICE
price_user_list = []
price_tweet_list = []
kw_2 = 'price'
for tweet in user_tweet:
  if kw_2 in tweet[1]:
    price_user_list.append(tweet[0])
    price_tweet_list.append(tweet[1])
  else:
    pass
price_list_tab = pd.DataFrame ({'User':price_user_list, "Tweet":price_tweet_list, 'Tag': kw_2})

#LIST SOLD
sold_user_list = []
sold_tweet_list = []
kw_3 = 'sold'
for tweet in user_tweet:
  if kw_3 in tweet[1]:
    sold_user_list.append(tweet[0])
    sold_tweet_list.append(tweet[1])
  else:
    pass
sold_list_tab = pd.DataFrame ({'User':sold_user_list, "Tweet":sold_tweet_list, 'Tag': kw_3})

#LIST ART
art_user_list = []
art_tweet_list = []
kw_4 = 'art'
for tweet in user_tweet:
  if kw_4 in tweet[1]:
    art_user_list.append(tweet[0])
    art_tweet_list.append(tweet[1])
  else:
    pass
art_list_tab = pd.DataFrame ({'User':art_user_list, "Tweet":art_tweet_list, 'Tag': kw_4})

#LIST NFTART
nftart_user_list = []
nftart_tweet_list = []
kw_5 = 'nftart'
for tweet in user_tweet:
  if kw_5 in tweet[1]:
    nftart_user_list.append(tweet[0])
    nftart_tweet_list.append(tweet[1])
  else:
    pass
nftart_list_tab = pd.DataFrame ({'User':nftart_user_list, "Tweet":nftart_tweet_list, 'Tag': kw_5})

#LIST NFTARTIST
nftartist_user_list = []
nftartist_tweet_list = []
kw_6 = 'nftartist'
for tweet in user_tweet:
  if kw_6 in tweet[1]:
    nftartist_user_list.append(tweet[0])
    nftartist_tweet_list.append(tweet[1])
  else:
    pass
nftartist_list_tab = pd.DataFrame ({'User':nftartist_user_list, "Tweet":nftartist_tweet_list, 'Tag': kw_6})

#Joining together the dataframes
tag_tot_list = pd.concat([eth_list_tab, price_list_tab, sold_list_tab, art_list_tab, nftart_list_tab, nftartist_list_tab])

#Creation of the network graph 
network_tweets= nx.from_pandas_edgelist(tag_tot_list, source="Tag",target="User")
plt.figure(figsize=(20,20))
pos = nx.spring_layout(network_tweets, k=0.80,)  
nx.draw(network_tweets, with_labels=True, node_color="#FF9933", edge_color='#023047')
plt.show()

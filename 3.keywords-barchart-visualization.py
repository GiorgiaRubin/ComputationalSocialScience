import seaborn as sns

#Keyword search results --> art: 261 , eth: 128 , sold: 123 , price: 119 , nftart: 69 , nftartist: 29

#Creation of the function needed for the implementation of the seaborn plot
uniq_el_13 = [('art', 261), ('eth', 128), ('sold', 123), ('price', 119), ('nftart', 69), ('nftartist', 29)]
uniq_tab_13 = pd.DataFrame(uniq_el_13, columns = ['word', 'count'])

def field_info_13(field_name):
  word = uniq_tab_13['word']
  count = uniq_tab_13['count']
  return(word, count)

#visualize words-count in bar plot
sns.set_theme(style="whitegrid", palette= 'dark', font_scale=3)
fig, ax = plt.subplots(figsize=(50, 20))

#plot horizontal bar graph
ax = sns.barplot(y=field_info_13(uniq_tab_13)[0], x=field_info_13(uniq_tab_13)[1])

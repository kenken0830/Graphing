#変数の箱ひげ図を描く
plt.figure(figsize=(14,10))
for i in np.arange((df_california.shape[1])):
    plt.subplot(3,3,i+1)
    plt.boxplot(df_california.dropna().iloc[:,i])
    plt.title(df_california.columns[i])

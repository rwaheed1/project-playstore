import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

class visualization:
    def __init__(self,data):
        self.df=data
    def showTopCategories(self):
        print("\n\n*************clean data Visualization")
        sns.set_style('darkgrid')
        matplotlib.rcParams['font.size'] = 14
        matplotlib.rcParams['figure.figsize'] = (9, 5)
        matplotlib.rcParams['figure.facecolor'] = '#00000000'
        self.df['Category'].value_counts()
        #plot data 
        y = self.df['Category'].value_counts().index
        x = self.df['Category'].value_counts()
        xsis = []
        ysis = []
        for i in range(len(x)):
            xsis.append(x[i])
            ysis.append(y[i])
        plt.figure(figsize=(18,13))
        plt.xlabel("Count")
        plt.ylabel("Category")

        graph = sns.barplot(x = xsis, y = ysis, palette= "ocean_r")
        graph.set_title("Top categories on Google Playstore", fontsize = 25);
    def showContentRating(self):
        self.df['Rating'].describe()
        sns.set_style('whitegrid')
        plt.figure(figsize=(15,9))
        plt.xlabel("Rating")
        plt.ylabel("Frequency")
        graph = sns.kdeplot(self.df.Rating, color="orange", shade = True)
        plt.title('Distribution of Rating',size = 18);
    def findtopAppsInstalled(self,str):
        str = str.upper()
        top10 = self.df[self.df['Category'] == str]
        top10apps = top10.sort_values(by='Installs', ascending=False).head(10)
        
        plt.figure(figsize=(15,12))
        plt.title('Top  '+str+ '  Installed Apps',size = 18); 
       
        graph = sns.barplot(x = top10apps.App, y = top10apps.Installs)
        sns.color_palette("crest", as_cmap=True)
        graph.set_xticklabels(graph.get_xticklabels(), rotation= 45, horizontalalignment='right');
    def showMostExpensive(self):
        topPaidApps = self.df[self.df['Type'] == 'Paid'].sort_values(by='Price', ascending=False).head(11)
        topPaidApps_df = topPaidApps[['App', 'Installs']].drop(9934)
        plt.figure(figsize=(15,12));
        plt.pie(topPaidApps_df.Installs, explode=None, labels=topPaidApps_df.App, autopct='%1.1f%%', startangle=0);
        plt.title('Most Expensive Apps Distribution',size = 20);
        plt.legend(topPaidApps_df.App, 
           loc="lower right",
           title="Apps",
           fontsize = "xx-small"
          );

        
# Importing Libraries
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
import pandas as pd
import os

l1 = ['Concealing of internet use', 'Inability to prioritize', 'No sense of time',
      'Feeling of Euphoria', 'Anger', 'Restlessness', 'Sleeping problem', 'Anxious'
    , 'Unfocused', 'Stressed', 'Social isolation', 'Low self esteem', 'Feeling of guilt',
      'Memory impairment', 'Mood Swing', 'Poor Concentration', 'Lying about internet use',
      'Boredom', 'Headache', 'Depression']
# List of the Disorders is listed in list called disease

disease = ['Net Compulsion', 'Information Overload', 'Cyber Relationship']
# disease = [df['prognosis'].unique()]
# print(disease)

l2 = []
for i in range(0, len(l1)):
    l2.append(0)
print(l2)

df = pd.read_csv("Training.csv")
DF = pd.read_csv('Training.csv', index_col='prognosis')
# Replace the values in the imported file by pandas by the inbuilt function replace in pandas.

df.replace({'prognosis': {'Net Compulsion': 0, 'Information Overload': 1, 'Cyber Relationship': 2}}, inplace=True)

DF.head()

'''
def plotPerColumnDistribution(df1, nGraphShown, nGraphPerRow):
    nunique = df1.nunique()
    df1 = df1[[col for col in df if nunique[col] > 1 and nunique[col] < 50]]
    # for Displaying purposes
    nRow, nCol = df1.shape
    columnNames = list(df1)
    nGraphRow = (nCol + nGraphPerRow - 1) / nGraphPerRow
    plt.figure(num=None, figsize=(6 * nGraphPerRow, 8 * nGraphRow), dpi=80, facecolor='w', edgecolor='k')
    for i in range(min(nCol, nGraphShown)):
        plt.subplot(nGraphRow, nGraphPerRow, i + 1)
        columnDf = df.iloc[:, i]
        if (not np.issubdtype(type(columnDf.iloc[0]), np.number)):
            valueCounts = columnDf.value_counts()
            valueCounts.plot.bar()
        else:
            columnDf.hist()
        plt.ylabel('counts')
        plt.xticks(rotation=90)
        plt.title(f'{columnNames[i]} (column {i})')
    plt.tight_layout(pad=1.0, w_pad=1.0, h_pad=1.0)
    plt.show()


# Scatter and density plots

def plotScatterMatrix(df1, plotSize, textSize):
    df1 = df1.select_dtypes(include=[np.number])  # keep only numerical columns
    # Remove rows and columns that would lead to df being singular

    df1 = df1.dropna('columns')
    df1 = df1[[col for col in df if df[col].nunique() > 1]]
    columnNames = list(df)
    if len(columnNames) < 10:
        columnNames = columnNames[:10]
    df1 = df1[columnNames]
    ax = pd.plotting.scatter_matrix(df1, alpha=0.75, figsize=[plotSize, plotSize], diagonal='kde')
    corrs = df1.corr().values
    for i, j in zip(*plt.np.triu_indices_from(ax, k=1)):
        ax[i, j].annotate('Corr.coef = %.3f' % corrs[i, j], (0.8, 0.2), xycoords='axes fraction', ha='center',
                          size=textSize)
        plt.suptitle('Scatter and Density Plot')
        plt.show()

'''
# plotPerColumnDistribution(df,10,5)
# plotScatterMatrix(df, 20,10)
X = df[l1]
y = df[['prognosis']]
np.ravel(y)
print(X)
print(y)

# Reading the testing.csv file
tr = pd.read_csv("Testing.csv")

# using the inbuilt function replace in pandas for replacing the values

tr.replace({'prognosis': {'Net Compulsion': 0, 'Information Overload': 1, 'Cyber Relationship': 2}}, inplace=True)

tr.head()

# plotPerColumnDistribution(tr,10,5)
# plotScatterMatrix(tr,20,10)

X_test = tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)
print(X_test)
print(y_test)


# list1 = DF['prognosis'].unique()
def scatterplt(disea):
    x = ((DF.loc[disea]).sum())  # total sum of symptom reported for given disease
    x.drop(x[x == 0].index, inplace=True)  # droping symptoms with values 0
    print(x.values)
    y = x.keys()  # storing name of symptoms in y
    print(len(x))
    print(len(y))
    plt.title(disea)
    plt.scatter(y, x.values)
    plt.show()


def scatterinp(sym1, sym2, sym3, sym4, sym5):
    x = [sym1, sym2, sym3, sym4, sym5]  # storing input symptoms in y
    y = [0, 0, 0, 0, 0]  # creating and giving values to the input symptoms
    if (sym1 != 'Select Here'):
        y[0] = 1
    if (sym2 != 'Select Here'):
        y[1] = 1
    if (sym3 != 'Select Here'):
        y[2] = 1
    if (sym4 != 'Select Here'):
        y[3] = 1
    if (sym5 != 'Select Here'):
        y[4] = 1
    print(x)
    print(y)
    #plt.scatter(x, y)
    plt.show()


root = Tk()
pred1 = StringVar()


def DecisionTree():
    if len(NameEn.get()) == 0:
        pred1.set(" ")
        comp = messagebox.askokcancel("System", "Kindly Fill the Name")
        if comp:
            root.mainloop()
    elif ((Symptom1.get() == "Select Here") or (Symptom2.get() == "Select Here")):
        pred1.set(" ")
        sym = messagebox.askokcancel("System", "Kindly Fill at least first two Symptoms")
        if sym:
            root.mainloop()
    else:
        print(NameEn.get())
        from sklearn import tree

        clf3 = tree.DecisionTreeClassifier()
        clf3 = clf3.fit(X, y)

        from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
        y_pred = clf3.predict(X_test)
        print("Decision Tree")
        print("Accuracy")
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred, normalize=False))
        print("Confusion matrix")
        conf_matrix = confusion_matrix(y_test, y_pred)
        print(conf_matrix)

        psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

        for k in range(0, len(l1)):
            for z in psymptoms:
                if (z == l1[k]):
                    l2[k] = 1

        inputtest = [l2]
        predict = clf3.predict(inputtest)
        predicted = predict[0]

        h = 'no'
        for a in range(0, len(disease)):
            if (predicted == a):
                h = 'yes'
                break

        if (h == 'yes'):
            pred1.set(" ")
            pred1.set(disease[a])
        else:
            pred1.set(" ")
            pred1.set("Not Found")
        import sqlite3
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(
            "CREATE TABLE IF NOT EXISTS DecisionTree(Name StringVar,Symtom1 StringVar,Symtom2 StringVar,Symtom3 StringVar,Symtom4 TEXT,Symtom5 TEXT,Disease StringVar)")
        c.execute(
            "INSERT INTO DecisionTree(Name,Symtom1,Symtom2,Symtom3,Symtom4,Symtom5,Disease) VALUES(?,?,?,?,?,?,?)",
            (NameEn.get(), Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get(), pred1.get()))
        conn.commit()
        c.close()
        conn.close()
        # printing scatter plot of input symptoms
        # printing scatter plot of disease predicted vs its symptoms
        scatterinp(Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get())
        #scatterplt(pred1.get())


pred2 = StringVar()


def randomforest():
    if len(NameEn.get()) == 0:
        pred1.set(" ")
        comp = messagebox.askokcancel("System", "Kindly Fill the Name")
        if comp:
            root.mainloop()
    elif ((Symptom1.get() == "Select Here") or (Symptom2.get() == "Select Here")):
        pred1.set(" ")
        sym = messagebox.askokcancel("System", "Kindly Fill atleast first two Symptoms")
        if sym:
            root.mainloop()
    else:
        from sklearn.ensemble import RandomForestClassifier
        clf4 = RandomForestClassifier(n_estimators=100)
        clf4 = clf4.fit(X, np.ravel(y))

        # calculating accuracy 
        from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
        y_pred = clf4.predict(X_test)
        print("Random Forest")
        print("Accuracy")
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred, normalize=False))
        print("Confusion matrix")
        conf_matrix = confusion_matrix(y_test, y_pred)
        print(conf_matrix)

        psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

        for k in range(0, len(l1)):
            for z in psymptoms:
                if (z == l1[k]):
                    l2[k] = 1

        inputtest = [l2]
        predict = clf4.predict(inputtest)
        predicted = predict[0]

        h = 'no'
        for a in range(0, len(disease)):
            if (predicted == a):
                h = 'yes'
                break
        if (h == 'yes'):
            pred2.set(" ")
            pred2.set(disease[a])
        else:
            pred2.set(" ")
            pred2.set("Not Found")
        import sqlite3
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(
            "CREATE TABLE IF NOT EXISTS RandomForest(Name StringVar,Symtom1 StringVar,Symtom2 StringVar,Symtom3 StringVar,Symtom4 TEXT,Symtom5 TEXT,Disease StringVar)")
        c.execute(
            "INSERT INTO RandomForest(Name,Symtom1,Symtom2,Symtom3,Symtom4,Symtom5,Disease) VALUES(?,?,?,?,?,?,?)",
            (NameEn.get(), Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get(), pred2.get()))
        conn.commit()
        c.close()
        conn.close()
        # printing scatter plot of disease predicted vs its symptoms
        #scatterplt(pred2.get())


pred4 = StringVar()


def KNN():
    if len(NameEn.get()) == 0:
        pred1.set(" ")
        comp = messagebox.askokcancel("System", "Kindly Fill the Name")
        if comp:
            root.mainloop()
    elif ((Symptom1.get() == "Select Here") or (Symptom2.get() == "Select Here")):
        pred1.set(" ")
        sym = messagebox.askokcancel("System", "Kindly Fill atleast first two Symptoms")
        if sym:
            root.mainloop()
    else:
        from sklearn.neighbors import KNeighborsClassifier
        knn = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
        knn = knn.fit(X, np.ravel(y))

        from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
        y_pred = knn.predict(X_test)
        print("KNN")
        print("Accuracy")
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred, normalize=False))
        print("Confusion matrix")
        conf_matrix = confusion_matrix(y_test, y_pred)
        print(conf_matrix)

        psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

        for k in range(0, len(l1)):
            for z in psymptoms:
                if (z == l1[k]):
                    l2[k] = 1

        inputtest = [l2]
        predict = knn.predict(inputtest)
        predicted = predict[0]

        h = 'no'
        for a in range(0, len(disease)):
            if (predicted == a):
                h = 'yes'
                break

        if (h == 'yes'):
            pred4.set(" ")
            pred4.set(disease[a])
        else:
            pred4.set(" ")
            pred4.set("Not Found")
        import sqlite3
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(
            "CREATE TABLE IF NOT EXISTS KNearestNeighbour(Name StringVar,Symtom1 StringVar,Symtom2 StringVar,Symtom3 StringVar,Symtom4 TEXT,Symtom5 TEXT,Disease StringVar)")
        c.execute(
            "INSERT INTO KNearestNeighbour(Name,Symtom1,Symtom2,Symtom3,Symtom4,Symtom5,Disease) VALUES(?,?,?,?,?,?,?)",
            (NameEn.get(), Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get(), pred4.get()))
        conn.commit()
        c.close()
        conn.close()
        # printing scatter plot of disease predicted vs its symptoms
        #scatterplt(pred4.get())


pred3 = StringVar()


def NaiveBayes():
    if len(NameEn.get()) == 0:
        pred1.set(" ")
        comp = messagebox.askokcancel("System", "Kindly Fill the Name")
        if comp:
            root.mainloop()
    elif ((Symptom1.get() == "Select Here") or (Symptom2.get() == "Select Here")):
        pred1.set(" ")
        sym = messagebox.askokcancel("System", "Kindly Fill atleast first two Symptoms")
        if sym:
            root.mainloop()
    else:
        from sklearn.naive_bayes import GaussianNB
        gnb = GaussianNB()
        gnb = gnb.fit(X, np.ravel(y))

        from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
        y_pred = gnb.predict(X_test)
        print("Naive Bayes")
        print("Accuracy")
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred, normalize=False))
        print("Confusion matrix")
        conf_matrix = confusion_matrix(y_test, y_pred)
        print(conf_matrix)

        psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]
        for k in range(0, len(l1)):
            for z in psymptoms:
                if (z == l1[k]):
                    l2[k] = 1

        inputtest = [l2]
        predict = gnb.predict(inputtest)
        predicted = predict[0]

        h = 'no'
        for a in range(0, len(disease)):
            if (predicted == a):
                h = 'yes'
                break
        if (h == 'yes'):
            pred3.set(" ")
            pred3.set(disease[a])
        else:
            pred3.set(" ")
            pred3.set("Not Found")
        import sqlite3
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(
            "CREATE TABLE IF NOT EXISTS NaiveBayes(Name StringVar,Symtom1 StringVar,Symtom2 StringVar,Symtom3 StringVar,Symtom4 TEXT,Symtom5 TEXT,Disease StringVar)")
        c.execute("INSERT INTO NaiveBayes(Name,Symtom1,Symtom2,Symtom3,Symtom4,Symtom5,Disease) VALUES(?,?,?,?,?,?,?)",
                  (NameEn.get(), Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get(),
                   pred3.get()))
        conn.commit()
        c.close()
        conn.close()
        # printing scatter plot of disease predicted vs its symptoms
        #scatterplt(pred3.get())


# Tk class is used to create a root window
#root.geometry("500*500")
root.configure(background='Ivory')
root.title('Social Media Mental Disorder Predictor System')
root.resizable(0, 0)

# taking first input as symptom
Symptom1 = StringVar()
Symptom1.set("Select Here")

# taking second input as symptom
Symptom2 = StringVar()
Symptom2.set("Select Here")

# taking third input as symptom
Symptom3 = StringVar()
Symptom3.set("Select Here")

# taking fourth input as symptom
Symptom4 = StringVar()
Symptom4.set("Select Here")

# taking fifth input as symptom
Symptom5 = StringVar()
Symptom5.set("Select Here")
Name = StringVar()

# function to Reset the given inputs to initial position
prev_win = None


def Reset():
    global prev_win

    Symptom1.set("Select Here")
    Symptom2.set("Select Here")
    Symptom3.set("Select Here")
    Symptom4.set("Select Here")
    Symptom5.set("Select Here")

    NameEn.delete(first=0, last=100)

    pred1.set(" ")
    pred2.set(" ")
    pred3.set(" ")
    pred4.set(" ")
    try:
        prev_win.destroy()
        prev_win = None
    except AttributeError:
        pass


# Exit button to come out of system
from tkinter import messagebox


def Exit():
    qExit = messagebox.askyesno("System", "Do you want to exit the system")
    if qExit:
        root.destroy()
        exit()


# Headings for the GUI written at the top of GUI
w2 = Label(root, justify=LEFT, text="Social Media Mental Disorder Predictor System", fg="Red", bg="Ivory")
w2.config(font=("Times", 30, "bold italic"))
w2.grid(row=1, column=0,columnspan=10)

w2.config(font=("Times", 30, "bold italic"))
w2.grid(row=2, column=0,columnspan=10)

# Label for the name

NameLb = Label(root, text="Name of the Patient", fg="Red", bg="Ivory")
NameLb.config(font=("Times", 15, "bold italic"))
NameLb.grid(row=8, column=1)

# Creating Labels for the symtoms
S1Lb = Label(root, text="Symptom 1", fg="Black", bg="Ivory")
S1Lb.config(font=("Times", 15, "bold italic"))
S1Lb.grid(row=9,column=0)

S2Lb = Label(root, text="Symptom 2", fg="Black", bg="Ivory")
S2Lb.config(font=("Times", 15, "bold italic"))
S2Lb.grid(row=9,column=1)

S3Lb = Label(root, text="Symptom 3", fg="Black", bg="Ivory")
S3Lb.config(font=("Times", 15, "bold italic"))
S3Lb.grid(row=9,column=2)

S4Lb = Label(root, text="Symptom 4", fg="Black", bg="Ivory")
S4Lb.config(font=("Times", 15, "bold italic"))
S4Lb.grid(row=9,column=3)

S5Lb = Label(root, text="Symptom 5", fg="Black", bg="Ivory")
S5Lb.config(font=("Times", 15, "bold italic"))
S5Lb.grid(row=9,column=4)

# Labels for the different algorithms
lrLb = Label(root, text="Output", fg="white", bg="red", width=20)
lrLb.config(font=("Times", 15, "bold italic"))
lrLb.grid(row=50, column=0, pady=10, sticky=W)
'''
destreeLb = Label(root, text="RandomForest", fg="Red", bg="Orange", width=20)
destreeLb.config(font=("Times", 15, "bold italic"))
destreeLb.grid(row=17, column=0, pady=10, sticky=W)

ranfLb = Label(root, text="NaiveBayes", fg="White", bg="green", width=20)
ranfLb.config(font=("Times", 15, "bold italic"))
ranfLb.grid(row=19, column=0, pady=10, sticky=W)

knnLb = Label(root, text="kNearestNeighbour", fg="Red", bg="Sky Blue", width=20)
knnLb.config(font=("Times", 15, "bold italic"))
knnLb.grid(row=21, column=0, pady=10, sticky=W)'''
OPTIONS = sorted(l1)

# Taking name as input from user
NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=8, column=2)

# Taking Symptoms as input from the dropdown from the user
S1 = OptionMenu(root, Symptom1, *OPTIONS)
S1.grid(row=11, column=0)

S2 = OptionMenu(root, Symptom2, *OPTIONS)
S2.grid(row=11, column=1)

S3 = OptionMenu(root, Symptom3, *OPTIONS)
S3.grid(row=11, column=2)

S4 = OptionMenu(root, Symptom4, *OPTIONS)
S4.grid(row=11, column=3)

S5 = OptionMenu(root, Symptom5, *OPTIONS)
S5.grid(row=11, column=4)

# Buttons for predicting the disease using different algorithms
dst = Button(root, text="Prediction", command=DecisionTree, bg="Red", fg="yellow")
dst.config(font=("Times", 15, "bold italic"))
dst.grid(row=40,column=1)
'''
rnf = Button(root, text="Prediction 2", command=randomforest, bg="Light green", fg="red")
rnf.config(font=("Times", 15, "bold italic"))
rnf.grid(row=7, column=3, padx=10)

lr = Button(root, text="Prediction 3", command=NaiveBayes, bg="Blue", fg="white")
lr.config(font=("Times", 15, "bold italic"))
lr.grid(row=8, column=3, padx=10)

kn = Button(root, text="Prediction 4", command=KNN, bg="sky blue", fg="red")
kn.config(font=("Times", 15, "bold italic"))
kn.grid(row=9, column=3, padx=10)
'''
rs = Button(root, text="Reset Inputs", command=Reset, bg="yellow", fg="purple", width=15)
rs.config(font=("Times", 15, "bold italic"))
rs.grid(row=40, column=2)

ex = Button(root, text="Exit System", command=Exit, bg="yellow", fg="purple", width=15)
ex.config(font=("Times", 15, "bold italic"))
ex.grid(row=40, column=3)

# Showing the output of different algorithms
t1 = Label(root, font=("Times", 15, "bold italic"), text="Decision Tree", height=1, bg="Light green"
           , width=40, fg="red", textvariable=pred1, relief="sunken").grid(row=50, column=1, padx=10)
'''
t2 = Label(root, font=("Times", 15, "bold italic"), text="Random Forest", height=1, bg="Purple"
           , width=40, fg="white", textvariable=pred2, relief="sunken").grid(row=17, column=1, padx=10)

t3 = Label(root, font=("Times", 15, "bold italic"), text="Naive Bayes", height=1, bg="red"
           , width=40, fg="orange", textvariable=pred3, relief="sunken").grid(row=19, column=1, padx=10)

t4 = Label(root, font=("Times", 15, "bold italic"), text="kNearest Neighbour", height=1, bg="Blue"
           , width=40, fg="yellow", textvariable=pred4, relief="sunken").grid(row=21, column=1, padx=10)'''

# calling this function because the application is ready to run
root.mainloop()


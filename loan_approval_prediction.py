# -*- coding: utf-8 -*-
"""Loan Approval Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oX73aGQt4E5fN_sYXY9_fgQiJ4kR7Mhp
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Loading the dataset
df = pd.read_csv('loan_approval_dataset.csv')
df.head()

"""# **Data Preprocessing**"""

# Checking the shape of the dataset
df.shape

df.drop(columns='loan_id', inplace=True)

# Checking for null/missing values
df.isnull().sum()

# Checking the data types of the columns
df.dtypes

# Movable Assets
df['Movable_assets'] = df[' bank_asset_value'] + df[' luxury_assets_value']

#Immovable Assets
df['Immovable_assets'] = df[' residential_assets_value'] + df[' commercial_assets_value']

# Drop columns
df.drop(columns=[' bank_asset_value',' luxury_assets_value', ' residential_assets_value', ' commercial_assets_value' ], inplace=True)

df.describe()

df.head()

"""# **Exploratory Data Analysis(EDA)**

In the exploratory data analysis, I will be looking at the distribution of the data across the varaiables, followed by relationship between the independent and target variable and the correlation among the variables. Through the visualization, I will be able to understand the possible trends and patterns in the data and come to know about the hidden insights of the data.
"""

sns.countplot(x = ' no_of_dependents', data = df).set_title('Number of Dependents')

"""This graph shows the number of dependent indivduals on the loan applicant. There is not much difference in the number of dependents, however, there are more applicants with 4 and 3 dependents than the other categories. Since the number of dependents increases the disposable income of the applicant decreases. So I assume that that the number of applicants with 0 or 1 dependent will have higher chances of loan approval."""

fig, ax = plt.subplots(1,2,figsize=(10, 5))
sns.boxplot(x = ' education', y = ' income_annum', data = df, ax=ax[0])
sns.violinplot(x = ' education', y = ' income_annum', data = df, ax=ax[1])

"""These two graphs - boxplot and violinplot visualizes the education of applicants along with their annual income. The boxplot shows some interesting fact that both the graduates and non-graduates have nearly same median income with very small increase in income of graduates. Moreover the violinplot shows the distribution of income among the graduates and non graduate applicants, where we can see that non graduate applicants have a even distribution between income 2000000 and 8000000, whereas there is a uneven distribution among the graduates with more applicants having income between 6000000 and 8000000. Since there is not much change in annual income of graduates and non graduates, I assume that education does not play a major role in the approval of loan"""

sns.countplot(x=' self_employed', data = df, hue = ' education').set_title('Self Employed')

"""This graph shows the number of self employed applicants along with their education. From the educational prepespective the majority of the graducate applicants are not self employed wheareas majority of the non-graduates are self employed. This means that graduates applicants are more likely to be salaried employees and non-graduates are more likely to be self employed. This could be a determining factor in loan approval because salaried employees are more likely to have a stable income and hence are more likely to pay back the loan as compared to self employed applicants whose income may not be stable. But this could also be possible that the self employed applicants are earning more than the salaried employees and hence are more likely to pay back the loan. This is a very important factor to consider while predicting the loan approval."""

sns.lineplot(x = ' loan_term', y = ' loan_amount', data = df).set_title('Loan Amount vs. Loan Term')

"""This line plot shows the trend between the loan amount and the loan tenure. Between the loan tenure of 2.5 - 7.5 years the loan amount is between 1400000 - 15500000. However the loan amount is significantly higher for the loan tenure of 10 years."""

sns.histplot(df[' cibil_score'], bins = 30, kde = True, color = 'red')

"""Before looking at the cibil score, lets have a look at the cibil score ranges and their meaning.

                       Cibil Score	Meaning
                            300-549	Poor
                            550-649	Fair
                            650-749	Good
                            750-799	Very Good
                            800-900	Excellent
Taking the above table as a reference for the cibil score quality, majority of the customers have cibil score below 649, which affects their loan application. However there are many applicants with cibil score above 649, which is a good sign for the bank. The bank can target these customers and provide them with priority services. The bank can also provide them with special offers and discounts to attract them to take loans from the bank. From this, I build a hypothesis that the customers with cibil score above 649 are more likely to get their loan approved.
"""

#asset distribution
fig, ax = plt.subplots(1,2,figsize=(10,5))
sns.histplot(df['Movable_assets'], ax=ax[0], color='red')
sns.histplot(df['Immovable_assets'], ax=ax[1], color='blue')

"""Assets play a major role in loan application. They provides a security to the bank that the person will repay the loan. Looking at the assets, as eralier mentionedI have categorized them in movable and immovable assets. The above graphs shows the distribution of movable and immovable assets in the dataset.

Looking at the movable assets which include bank assets and luxury assets, majority of the applicants have less than 30 million and there is a slight trend of decreasing number of applicants as the movable assets increases. Coming to the immovable assets, which include residential assets and commercial assets, majority of the applicants have less than 15 million of immovable assets and there is a strong trend of decreasing number of applicants as the immovable assets increases after 20 million.

Till now in the EDA, I have explored the distribution of data across the various features as well as relationship between the some of the variables as well and made some assumptions and hypothesis. Now, in order to prove my assumptions and hypothesis I will be looking at the visualization of the relation between the independent variables and the target variable.
"""

sns.countplot(x = ' no_of_dependents', data = df, hue = ' loan_status')

"""My hypothesis regarding the loan approval based on number of dependents has mixed results. First the hypothesis was somewhat true regarding the rejection chances, the number of loan rejection increases with increase in number of dependents. But the hypothesis was not true regarding the approval chances, the number of loan approval decreases with increase in number of dependents as per my hypothesis. But according to this graph, there has been no major change in the loan approval count with increase in number of dependents. So, my hypothesis regarding the loan approval based on number of dependents is not true."""

sns.countplot(x = ' education', hue = ' loan_status', data = df).set_title('Loan Status by Education')

"""My hypothesis regarding the education not being factor in loan approval was right. The graph shows very minor difference between loan approval and rejection count for the graduate and non graduate applicants. The difference is not significant enough."""

sns.violinplot(x=' loan_status', y=' income_annum', data=df)

"""On the whole, there has been no major difference between the annual incomes of the applicant with approved or rejected loan. But still, the approved loan applicants tend to have a higher annual income than the rejected loan applicants which is visible from the violin plot where the approved loan applicants have a higher density in the annual income near 8 miilion annual income."""

sns.lineplot(x=' loan_term', y=' loan_amount', data=df, hue=' loan_status')

"""This graph shows the relation between loan amount, loan tenure and loan status. Generally, the approved loans tend have higher amount and shorter repayment tenure. The rejected loans tend to have lower amount and longer repayment tenure. This could be a result of the bank's policy to reject loans with longer repayment tenure. The bank may also reject loans with lower amount as they may not be profitable for the bank."""

sns.violinplot(x=' loan_status', y=' cibil_score', data=df)

"""My hypothesis regarding the cibil score and loan approval is absolutely correct. It is evident through the violinplot, where the there is a high distribution above 600 cibil score from the loan approved category. The distribution of the loan not approved category is more spread out and has cibil score less than 550. This also proves my assumption that majority of the applicants have a poor/fair cibil score which affects their loan approval. Hence, having a high cibil score particularly grater than 600 would definitely increase the chances of loan approval."""

fig, ax = plt.subplots(1,2,figsize=(10,5))
sns.histplot(x  = 'Movable_assets', data = df, ax=ax[0], hue = ' loan_status', multiple='stack')
sns.histplot(x =  'Immovable_assets', data = df, ax=ax[1], hue  = ' loan_status', multiple='stack')

"""Assets provide security to the bank against which the loan is issued. These two graph visualizes the relation between the movable and immovable assets along with the loan status. The both graph shows that, with increase in the assets the chances of loan approval increases and rejection decreases. The graph also shows that, the movable assets are more than the immovable assets.

# **Data Preprocessing**

**Label Encoding the categorical variables**
"""

# Label Encoding
df[' education'] = df[' education'].map({' Not Graduate':0, ' Graduate':1})
df[' self_employed'] = df[' self_employed'].map({' No':0, ' Yes':1})
df[' loan_status'] = df[' loan_status'].map({' Rejected':0, ' Approved':1})

df.head()

"""**Coorelation Matrix using Heatmap**"""

plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),annot = True,cmap='coolwarm')

"""This coorelation matrix heatmap has the folowing strong correlations:

1. Movable Assets and Immovable Assets
2. Income and Movable Assets
3. Income and Immovable Assets
4. Movable Assets and Loan Amount
5. Immovable Assets and Loan Amount
6. Loan Status and Cibil Score
7. Loan Amount and Income

The coorelation between the movable and immovable assets is justified because both come under assets and its obvious that person with more movable assets will have more immovable assets and vice versa. Same is with Income and Movables and Immovale assets. The person with greater income will have greater assets.

Now, I will be exploring the coorleation between Assets and Loan Amount, and also between Income and Loan Amount. The relation between the loan status and cibil score is already explored in the previous section.
"""

#assets vs loan amount
fig, ax = plt.subplots(1,2,figsize=(10, 5))
sns.scatterplot(x='Movable_assets', y = ' loan_amount', data = df, ax=ax[0]).set_title('Movable_assets vs loan_amount')
sns.scatterplot(x='Immovable_assets', y = ' loan_amount', data = df, ax=ax[1]).set_title('Immovable_assets vs loan_amount')

"""The loan amount has positive relation with movable and immovable assets. The more the assets, the more the loan amount issued by the bank."""

#loan amount vs income
sns.scatterplot(x=' income_annum', y = ' loan_amount', data = df)

"""The loan amount and applicant's annual income have a very direct relation between them. The higher the income, the higher the loan amount. This is because the applicant's income is the main factor in deciding the how much loan needed.

# **spliting the data**
"""

X = df.drop(' loan_status', axis=1)
y =  df[' loan_status']

#Train Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42)

"""# **Model Building**

I will be using the following machine learning models to predcit the loan approval status:

                      1. Decision Tree Classifier
                      2. Random Forest Classifier
"""

#Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier

# Create decision tree object
dtree = DecisionTreeClassifier()

# Trainign the model using the training data
dtree.fit(X_train, y_train)

# Training Accuracy
#dtree.score(X_train, y_train)
from sklearn.metrics import accuracy_score, f1_score
#we compute the eval metric on test/validation set only primarily

# Predict test set labels
y_pred = dtree.predict(X_test) # Model's predictions

# Compute test set accuracy
acc = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
print("Test set accuracy: {:.2f}".format(acc))
print("Test set f1-score: {:.2f}".format(f1))

# Predicting the Loan Approval Status
dtree_pred = dtree.predict(X_test)
dtree_pred

##there are 1 param to play with - max depth - to choose the best parameter, I will try different combinations and hoose the one which has the best accuracy/auc/any eval metric on cross-validation or test data-set
from sklearn.model_selection import cross_val_score #this will help me to do cross- validation
import numpy as np

for depth in [1,2,3,4,5,6,7,8,9,10,20,25,30,40,50]:
  dtree = DecisionTreeClassifier(max_depth=depth) # will tell the DT to not grow past the given threhsold
  # Fit dt to the training set
  dtree.fit(X_train, y_train) # the model is trained
  trainAccuracy = accuracy_score(y_train, dtree.predict(X_train)) # this is useless information - i am showing to prove a point
  dt = DecisionTreeClassifier(max_depth=depth) # a fresh model which is not trained yet
  valAccuracy = cross_val_score(dt, X_train, y_train, cv=10) # syntax : cross_val_Score(freshModel,fts, target, cv= 10/5)
  print("Depth  : ", depth, " Training Accuracy : ", trainAccuracy, " Cross val score : " ,np.mean(valAccuracy))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 7)

from matplotlib import pyplot
dtree = DecisionTreeClassifier(max_depth = 5)
# Fit dt to the training set
dtree.fit(X_train, y_train)
importance = dtree.feature_importances_
#pyplot.bar([x for x in range(len(importance))], importance)
list(zip(importance,X_test.columns)) # it calculates the feature importances based on IG

from sklearn import tree
tree.plot_tree(dtree) # dt is the decison tree that I have learnt

import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=300)
tree.plot_tree(dtree,
               feature_names = X_test.columns,
               filled = True);
fig.savefig('imagename.png')

#Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier

# Create a random forest classifier
rfc = RandomForestClassifier()

# Training the model using the training data
rfc.fit(X_train, y_train)

# Training Accuracy
rfc.score(X_train, y_train)

# Training Accuracy
#dtree.score(X_train, y_train)
from sklearn.metrics import accuracy_score, f1_score
#we compute the eval metric on test/validation set only primarily

# Predict test set labels
y_pred = rfc.predict(X_test) # Model's predictions

# Compute test set accuracy
acc = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
print("Test set accuracy: {:.2f}".format(acc))
print("Test set f1-score: {:.2f}".format(f1))

# Predicting the Loan Approval Status
rfc_pred = rfc.predict(X_test)

"""# **Model Evalution**"""

from sklearn.metrics import confusion_matrix

fig, ax = plt.subplots(1,2,figsize=(10,4))
sns.heatmap(confusion_matrix(y_test, dtree_pred), annot=True, ax=ax[0]).set_title('Decision Tree')
ax[0].set_xlabel('Predicted')
ax[0].set_ylabel('Actual')
sns.heatmap(confusion_matrix(y_test, rfc_pred), annot=True, ax=ax[1]).set_title('Random Forest')
ax[1].set_xlabel('Predicted')
ax[1].set_ylabel('Actual')

"""The above confusion matrix heatmap visualizes the the true positive and true negative value counts in both the machine learning models. The decision tree classfier has only 17 false positve and negative valyes where has random forest classifier has 21 false postive and negative values. The decision tree classifier has a better accuracy compared to random forest classifier."""

#distribution plot

ax = sns.distplot( x = y_test, hist = False, color = "r", label = "Actual Value")
sns.distplot( x = dtree_pred, hist = False, color = "b", label = "Fitted Values", ax = ax)
plt.title('Actual vs Fitted Values for Decsion Tree Classfier')

ax = sns.distplot( x = y_test, hist = False, color = "r", label = "Actual Value")
sns.distplot( x = rfc_pred, hist = False, color = "b", label = "Fitted Values", ax = ax)
plt.title('Actual vs Fitted Values for Random Forest Classfier')

"""# classification"""

from sklearn.metrics import classification_report

print(classification_report(y_test, dtree_pred))
print(classification_report(y_test, rfc_pred))

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

# Assuming y_test, dtree_pred, and rfc_pred are your true labels and predicted labels for the classification task

# Decision Tree Classifier
print('Accuracy Score (Decision Tree): ', accuracy_score(y_test, dtree_pred))
print('Precision Score (Decision Tree): ', precision_score(y_test, dtree_pred))
print('Recall Score (Decision Tree): ', recall_score(y_test, dtree_pred))
print('F1 Score (Decision Tree): ', f1_score(y_test, dtree_pred))
print('ROC AUC Score (Decision Tree): ', roc_auc_score(y_test, dtree_pred))
print('Confusion Matrix (Decision Tree):\n', confusion_matrix(y_test, dtree_pred))
print('\n')

# Random Forest Classifier
print('Accuracy Score (Random Forest): ', accuracy_score(y_test, rfc_pred))
print('Precision Score (Random Forest): ', precision_score(y_test, rfc_pred))
print('Recall Score (Random Forest): ', recall_score(y_test, rfc_pred))
print('F1 Score (Random Forest): ', f1_score(y_test, rfc_pred))
print('ROC AUC Score (Random Forest): ', roc_auc_score(y_test, rfc_pred))
print('Confusion Matrix (Random Forest):\n', confusion_matrix(y_test, rfc_pred))

"""# **Feature Importance**"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 7)

from matplotlib import pyplot
dtree = DecisionTreeClassifier(max_depth = 5)
# Fit dt to the training set
dtree.fit(X_train, y_train)
importance = dtree.feature_importances_
#pyplot.bar([x for x in range(len(importance))], importance)
list(zip(importance,X_test.columns)) # it calculates the feature importances based on IG

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 7)

from matplotlib import pyplot
rfc = RandomForestClassifier(max_depth = 5)
# Fit dt to the training set
rfc.fit(X_train, y_train)
importance = rfc.feature_importances_
#pyplot.bar([x for x in range(len(importance))], importance)
list(zip(importance,X_test.columns)) # it calculates the feature importances based on IG

"""# **conclusion**

From the exploratory data analysis, we can conclude that the following factors are important for the approval of loan:

                        CIBIL Score: People with higher CIBIL score have higher chances of loan approval
                        Number of Dependents: People with more number of dependents have less chances of loan approval
                        Assets: People with more assets ( including movable and immovable) have higher chances of loan approval
                        Loan Amount and Tenure: People with higher loan amount and lower tenure have more chances of loan approval
Coming to the machine learning models, I have used Decision Tree Classifier and Random Forest Classifier. Both the models have given results having ROC AUC Score - 53.3 % and 98.3 % repectively. But the decision tree classifier has yielded better results than the random forest classifier.
"""
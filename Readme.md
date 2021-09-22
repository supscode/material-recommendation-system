# Capstone Project - Recommendation System for a Fashion Supply Chain Marketplace

## Problem Statement

Fabric Central is a digital sourcing platform that connects apparel brands and fabric suppliers in the most efficient, accessible and transparent marketplace. Suppliers can display their materials on the platforms and Brand users can easily find the materials from various suppliers in one place. 

Fabric Central has onboarded around 78 suppliers with around 200 materials so far and has around 358 brands registered brands. However it would now like to focus on increasing their sales and engage better with their users. 

We will build a recommendation system for Fabric Central which will recommend relevant materials to the customer at various touchpoints on the platform. By showing relevant materials and helping the users fnd the right matrials for their needs, we hope to increase customer engagement and conversion rate. 

We will build two types of recommendations, 
1. Content Based:<br>
    This will recommend similar materials to the one the customer is viewing, this can be displayed on the material search page, possible under a section called "You may also like..." or "More like these..." 
2. Item based Collaborative Filtering:<br>
    This will recommend materials depending on the gabric request history of this material by other users. This can be displayed on the order confirmation page, possibly under a section called "Users who bought this also bought..."
3. Hybrid recommendations:<br>
    The fabric request data is found to be very sparse and is not available for all materials. To tackle this cold start problem, we will also provide hybrid recomendations. Here the collborative filtering related recommendations (which need fabric request data) will be generated first, and will be supplemented by the content based materials. 

## Data Cleaning
- Handling Null Values
    - Drop columns with too many null values
    - Impute values for fabric weight for leather fabrics as 500 g/m-sq. 
    - Impute values for other weight values as mean of the fabric blend. 
- Replace null values for categorical variables
    - Many materials had missing values for categorical variables such as fabric_weave, fabric_blend etc. Instead of dropping these, the values were replaced with "blank" values. 
- Remove invalid materials
    - Materials which were archived by the suppliers
    - Marked with Published = False were removed
    - Price = 0
- Drop fabric requests made by demo users
    - Many fabric requests were initiate by Fabric Central staff, these couldn't be used as they would have skewed the recommendations. 

## EDA 
Histograms for numerical features and countplots for categorical featires were done, to understand the features. Features which can be used should have few blank or zero values. 


## Feature Engineering & Feature Selection
- Combine properties & End-Uses
    Properties and EndUses were split across multiple columns e.g. end_use/0, end_use/1 etc. These were combined into properties and end_use coumns
- Select best features based on EDA and client inputs
- Assign higher weight for Sample fabric requests compared to Swatch for Collaborative Filtering

## Content Based recommendations
Content Based recommendation systems work by recommending materials similar to the materials that a user likes. In case of Fabric Central we don't have data that a user likes, so instead we will recommend materials similar to the materials the user is viewing. 

### Clustering
Unsupervised clustering methods were implemented to try and cluster similar materials and recommend materials from the same cluster as the input material. The following clustering methods were tried: 

#### KMeans
#### DBSCAN
#### Hierarchical Clustering

**Conclusion for clustering**: After trying various methods of clustering we infer that materials data is naturally not separated in clusters. This could be becuase in terms of the significant features, many materials have more or less similar values. We conclude that clustering is not the best method for getting recommendations in our case. We will proceed to see the other method below. In addition, we will still consider using hierarchical clustering in conjunction with the next method. 

### Similarity Based Recommendations
We used pairwise similarity metrics to create a similarity matrix of all the materials with the rest of the materials. Then we find the top 10 materials with the highest similarity with the requester material. 

Following combinations were tried:
1. First we used the materials from a cluster formed earlier using hierarchical clustering. Here we will use pairwise similarity metrics within the cluster to find recommendations and observe the results. Next we use pairwise similarity metrics on the whole dataset. 
2. We used both scaled and unscaled data to see the difference.
3. We used Cosine Simlarity and Sigmoid Kernel

Following pairwaise similaruty metrics were used: 
#### Cosine Similarity
#### Sigmoid Kernel

**Conclusion for Similarity Based Recommendations**:

From observations, we find that scaling gives much better recommendations using both cosine similarity and sigmoid kernel. 

We also find that similarity based recommendations, with and without clustering gives approximately the same recommendations. To reduce restrictions on recommendations due to materials being separated in clusters we will go with non-clustered cosine similarity for now, but we will keep the option open to use cosine similarity with hierarchical clustering in the future. 

Cosine similarity and Sigmoid kernel also give approximately same results. We go ahead with Cosine Similarity as it is the more popular method for finding similarity in multi-dimensional data points. In the future, we may try different combinations and compare results for A/B testing.

## Item Based Collaborative Filtering recommendations
Collaborative filtering filters information by using the interactions and data collected by the system from other users. We use Item Based collaborative filtering which measures the similarity between the items that the users rate or interact with and other items. Since Fabric Central doesn't have user clicks or ratings data, our system will find similar materials based on the fabric requests made by users.

### Nearest Neighbours
We use nearest neighbours unsupervised method to find the nearest materials matching based on user requests. Nearest Neighbours is an unsupervised learning algorithm which takes a sparse matrix with m samples and n features and finds nearest samples based on the features.

## Evaluation

- Evaluation using domain Knowledge<br>
Recommendation systems with unlabelled data are difficult to evaluate before they are deployed. In this case we used the domain knowledge of experts to assess the recommendations made by our system.  Recommendations (both Content Based and Collaborative) for all materials in the database were outputted to csv files. These were made user friendly for the users by providing hyperlinks in the file to enable them to click on the recommended materials and view the features of the recommended materials. 

After the system is deployed we can use following methods for evaluation:
- Tracking User clicks<br>
    Tracking user clicks from specific web pages to measure metrics such as Click Through Rate, Conversion Rate etc.
- A/B testing<br>
Comparing recommendations from various methods by using A/B testing.


## Conclusion & Recommendations
Recommendation Systems have many benefits such as improving customer engagement, customer conversion rate and in turn the revenue of e-commece websites. Our project finds that both Content Based (CB) and item based Collaborative Filtering (CF) are possible using the existing data that Fabric Central has. Initial evaluation by domain experts, shows accurate recommendations for both CB and CF Filtering. 

The actual performance of the recommendation system can evaluated after it is deployed on the website. In conclusion the recommendation system can be integrated and deployed on the website, to help improve the customer satisfaction as well as sales for Fabric Central. 

#### Where should the recommendations be displayed?

- Content Based Materials should be displayed on Material Search page as here users are searching for specific kind of materials.

- Hybrid Recommendations should be displayed on the Materials Detail page. So users can see what other users who requested the given material also requested, in addition where such recommendations are not possible, they will be shown content based (similar) materials are the one they are viewing. 

- Optionally, Collaborative Filtering recommendations should be displayed on Order Completion page. As here the user will only like to see complementary materials to the one they bought, which can be the other materials that other users who bought the given material also bought. 

#### Other Recommendations 
1. User clicks from recommendations, should be tracked upon deployment of the recommendation system. This can help to evaluate the percentange of users that are clicking on the recommended materials. 

2. A/B testing should be performed to compare user behaviour with the various recommendation methods. 

3. Implement explicit user feedback such as reviews/ratings should be implemented for materials, to get more accurate recommendations for users. 

4. More user attributes should be gathered when signing up users. This will enable us to implement user based collaborative filtering. 


# Future Steps

- Integration & Deployment of the recommendation system to integrate with existing web application

- User Based Collaborative Filtering, based on similarity of user attributes

- Explore other algorithms for item based collaborative filtering like Matrix Factorization, Deep Learning

- Implement A/B testing to assess relative performance of various models

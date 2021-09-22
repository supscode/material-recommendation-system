# Capstone Project - Recommendation System for a Fashion Supply Chain Marketplace

## Problem Statement

Fabric Central is a digital sourcing platform that connects apparel brands and fabric suppliers in the most efficient, accessible and transparent marketplace. Suppliers can display their materials on the platforms and Brand users can easily find the materials from various suppliers in one place. 

Fabric Central has onboarded around 78 suppliers with around 200 materials so far and has around 358 brands registered brands. However it would now like to focus on increasing their sales and engage better with their users. 

We will build a recommendation system for Fabric Central which will recommend relevant materials to the customer at various touchpoints on the platform. By showing relevant materials and helping the users fnd the right matrials for their needs, we hope to increase customer engagement and conversion rate. 

We will build two types of recommendations, 
1. Content Based
    This will recommend similar materials to the one the customer is viewing, this can be displayed on the material search page, possible under a section called "You may also like..." or "More like these..." 
2. Item based Collaborative Filtering
    This will recommend materials depending on the gabric request history of this material by other users. This can be displayed on the order confirmation page, possibly under a section called "Users who bought this also bought..."
3. Hybrid recommendations
    The fabric request data is found to be very sparse and is not available for all materials. To tackle this cold start problem, we will also provide hybrid recomendations. Here the collborative filtering related recommendations (which need fabric request data) will be generated first, and will be supplemented by the content based materials. 
    
## Data Dictionary
There are two main tabels used on this project 
- Materials for Content Based filtering <br>

| Feature                             | Dtype   | Dataset   | Descripion                                                                                   |
| ----------------------------------- | ------- | --------- | -------------------------------------------------------------------------------------------- |
| id                                  | int64   | Materials | Uniquie id of the material                                                                   |
| created\_at                         | object  | Materials | Datetime at which the material was created at                                                |
| updated\_at                         | object  | Materials | Datetime at which the material was updated at                                                |
| code                                | object  | Materials | Unique code of the material                                                                  |
| fabric\_weave                       | object  | Materials | Weave of the fabric                                                                          |
| currency                            | object  | Materials | Currency in which the price is expressed                                                     |
| supplier\_id                        | int64   | Materials | Id of the Supplier who is selling this material                                              |
| price                               | float64 | Materials | Price of the material                                                                        |
| name                                | object  | Materials | Name of the material                                                                         |
| fabric\_blend\_one                  | object  | Materials | The first blend/content used in the material                                                 |
| fabric\_blend\_one\_percent         | float64 | Materials | % of the first fabric blend in the material                                                  |
| fabric\_blend\_two                  | object  | Materials | The second blend/content used in the material                                                |
| fabric\_blend\_two\_percent         | float64 | Materials | % of the second fabric blend in the material                                                 |
| fabric\_blend\_three                | object  | Materials | The third blend/content used in the material                                                 |
| fabric\_blend\_three\_percent       | float64 | Materials | % of the third fabric blend in the material                                                  |
| weight                              | float64 | Materials | Weight of the fabric usually expressed in gm/meter squared                                   |
| weight\_unit                        | object  | Materials | Unit in which weight is expressed usually  gm/meter squared                                  |
| end\_use/0                          | object  | Materials | End Uses for the material. This is stored as separate columns for each end use               |
| end\_use/1                          | object  | Materials | End Uses for the material. This is stored as separate columns for each end use               |
| end\_use/2                          | object  | Materials | End Uses for the material. This is stored as separate columns for each end use               |
| fabric\_type                        | object  | Materials | A borad categorisation of the type of fabric                                                 |
| price\_unit                         | object  | Materials | Unit for which the price is being displayed e.g. meters                                      |
| status                              | object  | Materials | Status of the fabric - public / private. Private materials are only available for few brands |
| deleted\_at                         | float64 | Materials | Datetime at which the material was deleted at                                                |
| only\_for\_brands/0                 | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| published                           | bool    | Materials | Whether the material is published                                                            |
| description                         | object  | Materials | Descripion of the material                                                                   |
| dispatch\_time\_sample              | object  | Materials | No of days in which a sample of the material can be dispatched                               |
| factory\_location                   | object  | Materials | Factory location of the material                                                             |
| construction                        | object  | Materials | Construction of the material (derived from fabric blends)                                    |
| width                               | float64 | Materials | Width of the material as sold (length is as per order, width is usually fixed)               |
| width\_unit                         | object  | Materials | Unit in which width is expressed usually metre                                               |
| finishing                           | object  | Materials | Finishing of the material (free text entered by supplier)                                    |
| properties/0                        | object  | Materials | Additional properties of the material. This is stored as separate columns for each property. |
| dispatch\_time\_mass\_quantity\_min | float64 | Materials | Minimum dispatch time for mass quantity                                                      |
| dispatch\_time\_mass\_quantity\_max | float64 | Materials | Maximum dispatch time for mass quantity                                                      |
| origin                              | object  | Materials | Origin/source of the material in the system                                                  |
| colour                              | object  | Materials | Colour of the material                                                                       |
| tsa\_stamps                         | object  | Materials | Field used for external integration with another system                                      |
| minimal\_order\_quantity            | float64 | Materials | Minimal order quantity for orders                                                            |
| crowd\_source\_available            | object  | Materials | Whether crowd sourcing is available (Currently not used)                                     |
| moq\_details                        | object  | Materials | Text describing moq conditions                                                               |
| uuid                                | object  | Materials | unique uuid generated for internal use                                                       |
| notify\_fc\_team             | bool    | Materials | Whether textile team can be notified if user wants to request the material                   |
| moq                                 | float64 | Materials | NA                                                                                           |
| swatch\_price                       | int64   | Materials | Price of the swatch (currently 2$ for all)                                                   |
| swatch\_quantity                    | float64 | Materials | Available swatch quantity                                                                    |
| archived\_at                        | object  | Materials | Datetime at which the material was archived at                                               |
| end\_use/3                          | object  | Materials | End Uses for the material. This is stored as separate columns for each end use               |
| end\_use/4                          | object  | Materials | End Uses for the material. This is stored as separate columns for each end use               |
| only\_for\_brands/1                 | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| properties/1                        | object  | Materials | Additional properties of the material. This is stored as separate columns for each property. |
| properties/2                        | object  | Materials | Additional properties of the material. This is stored as separate columns for each property. |
| properties/3                        | object  | Materials | Additional properties of the material. This is stored as separate columns for each property. |
| properties/4                        | object  | Materials | Additional properties of the material. This is stored as separate columns for each property. |
| properties/5                        | object  | Materials | Additional properties of the material. This is stored as separate columns for each property. |
| properties/6                        | object  | Materials | Additional properties of the material. This is stored as separate columns for each property. |
| properties/7                        | object  | Materials | Additional properties of the material. This is stored as separate columns for each property. |
| only\_for\_brands/2                 | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| end\_use/5                          | object  | Materials | End Uses for the material. This is stored as separate columns for each end use               |
| properties/8                        | object  | Materials | Additional properties of the material. This is stored as separate columns for each property. |
| only\_for\_brands/3                 | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| only\_for\_brands/4                 | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| only\_for\_brands/5                 | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| only\_for\_brands/6                 | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| only\_for\_brands/7                 | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| end\_use/6                          | object  | Materials | End Uses for the material. This is stored as separate columns for each end use               |
| end\_use/7                          | object  | Materials | End Uses for the material. This is stored as separate columns for each end use               |
| only\_for\_brands/8                 | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| only\_for\_brands/9                 | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| only\_for\_brands/10                | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| only\_for\_brands/11                | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| only\_for\_brands/12                | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| only\_for\_brands/13                | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| only\_for\_brands/14                | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| only\_for\_brands/15                | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| only\_for\_brands/16                | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| only\_for\_brands/17                | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| only\_for\_brands/18                | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| only\_for\_brands/19                | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| only\_for\_brands/20                | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| only\_for\_brands/21                | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |
| only\_for\_brands/22                | object  | Materials | Brands which can view a private material. This is stored as separate columns for each brand  |

- Fabric requests for Collaborative Filtering<br>

| Feature          | Dtype   | Dataset         | Descripion                                                                                                        |
| ---------------- | ------- | --------------- | ----------------------------------------------------------------------------------------------------------------- |
| id               | int64   | Fabric Requests | Id of the Fabric Request                                                                                          |
| status           | object  | Fabric Requests | Status of the Fabric request e.g. initial, delivered, delayed etc                                                 |
| type             | object  | Fabric Requests | Swatch (small piece) or Sample (by metre)                                                                         |
| quantity         | float64 | Fabric Requests | Quantity requested                                                                                                |
| requested\_at    | object  | Fabric Requests | Datetime at which the fabric request was made                                                                     |
| closed\_at       | object  | Fabric Requests | Datetime at which the fabric request was closed i.e. ordered                                                      |
| delay\_days      | float64 | Fabric Requests | No of days supplier will take to dispatch the order                                                               |
| delay\_note      | object  | Fabric Requests | Free text entered by supplier                                                                                     |
| material\_id     | int64   | Fabric Requests | id of the material requested                                                                                      |
| user\_id         | int64   | Fabric Requests | id of the user who madet he request                                                                               |
| project\_id      | float64 | Fabric Requests | id of the project the material is a part (projects are sued by users to organise, but not fully in use right now) |
| created\_at      | object  | Fabric Requests | Datetime at which the fabric request was created at                                                               |
| updated\_at      | object  | Fabric Requests | Datetime at which the fabric request was updated at                                                               |
| order\_id        | float64 | Fabric Requests | If fabric request was converted to an order then the id of the order                                              |
| price            | float64 | Fabric Requests | price of the material when requested                                                                              |
| price\_unit      | object  | Fabric Requests | unit of the price                                                                                                 |
| surcharge        | float64 | Fabric Requests | Surcharge specified by the supplier for the request (if below moq)                                                |
| accepted\_at     | object  | Fabric Requests | Datetime at which the fabric request was accepted by the user                                                     |
| deleted\_at      | float64 | Fabric Requests | Datetime at which the fabric request was deleted                                                                  |
| origin\_quantity | float64 | Fabric Requests | Original qunatity if the quantity is changed                                                                      |
| variant\_id      | int64   | Fabric Requests | Id of the variant if ordering a variant of the material                                                           |
| currency         | object  | Fabric Requests | Currency of the proce                                                                                             |
| bought\_price    | float64 | Fabric Requests | Price at which the material was bought at                                                                         |


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

**Conclusion for clustering**: By seeing various methods of clusterin we conclude that materials data is naturally not separated in clusters. This could be becuase in terms of the significant features, many materials have more or less similar values. We conclude that clustering is not the best method for getting recommendations in our case. We will proceed to see the other method below. In addition, we will still consider using hierarchical clustering in conjunction with the next method. 

### Similarity Based Recommendations
We used pairwise similarity metrics to create a similarity matrix of all the materials with the rest of the materials. Then we find the top 10 materials with the highest similarity with the requester material. 

Following combinations were tried:
1. First we used the materials from a cluster formed earlier using hierarchical clustering. Here we will use pairwise similarity metrics within the cluster to find recomemndations and observe the results. Next we use pairwise similarity metrics on the whole dataset. 
2. We used both scaled and unscaled data to see the difference.
3. We used Cosine Simlarity and Sigmoid Kernel

Following pairwaise similaruty metrics were used: 
#### Cosine Similarity
#### Sigmoid Kernel

**Conclusion for Similarity Based Recommendations**:

From observations, we find that scaling gives much better recommendations using both cosine similarity and sigmoid kernel. 

We also find that similarity based recommendations, with and without clustering gives approximately the same recommendations. To reduce restrsictions on recommendations due to clustering we will go with non clustered cosine similarity for now, but we will keep the option open to use cosone similarity with hierarchical clusteing in the future. 

Cosine similarity and Sigmoid kernel also give approximately same results. We go ahead with Cosine Similarity as it is the more popular method for finding similarity in multi-dimensional data points. In the future, we may try different combinations and compare results for A/B testing.

## Item Based Collaborative Filtering recommendations
Collaborative filtering filters information by using the interactions and data collected by the system from other users. We use Item Based collaborative filtering which measures the similarity between the items that the users rate or interact with and other items. Since Fabric Central doesn't have user clicks or ratings data, our system will find similar materials based on the fabric requests made by users.

### Nearest Neighbours
We use nearest neighbours unsupervised method to find the nearest materials matching based on user requests. Nearest Neighbours is an unsupervised learning algorithm which takes a sparse matrix with m samples and n features and finds nearest samples based on the features.

## Evaluation

- Evaluation using domain Knowledge
Recommendation systems with unlabelled data are difficult to evaluate before they are deployed. In this case we used the domain knowledge of experts to assess the recommendations made by our system.  Recommendations (both Content Based and Collaborative) for all materials in the database were outputted to csv files. These were made user friendly for the users by providing hyperlinks in the file to enable them to click on the recommended materials and view the features of the recommended materials. 

After the system is deployed we can use following methods for evaluation:
- Tracking User clicks
    Tracking user clicks from specific web pages to measure metrics such as Click Through Rate, Conversion Rate etc.
- A/B testing
Comparing recommendations from various methods by using A/B testing.


## Conclusion & Recommendations
Recommendation Systems have been many benefits such as improving customer engagement, customer conversion rate and in turn the revenue of ecommece websites. Our project find that both Content Based (CB) and item based Collaborative Filtering (CF)is possible using the existing data that Fabric Central has. Initial evaluation by domain experts, shows accurate recommendations for both CB and CF FIltering. 

The actual performance of the recommendation system can evaluated after it is deployed on the website. In conclusion the recommendation system can be integrated and deployed on the website, to help improve the customer satisfaction as well as sales for Fabric Central. 

#### Where should the recommendations be displayed?

- Content Based Materials should be displayed on Material Search page

- Hybrid Recommendations should be displayed on the materials details page

- Optionally, Collaborative Filtering recommendations should be displayed on Order Completion page

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

import numpy as np
import pandas as pd

def get_recommendations(full_dataset, similarity_matrix, name="", mat_id=0, n=10, user_based_results=None):

    if(name != ""):
        orig_material = full_dataset.loc[full_dataset["name"] == name]
        mat_id = orig_material["id"]
    elif mat_id != 0:
        orig_material = full_dataset.loc[full_dataset["id"] == mat_id]

    # Get the pairwsie similarity scores of all materials with the given material
    df_sim_scores = similarity_matrix.loc[mat_id]
    df_sim_scores.index = pd.to_numeric(df_sim_scores.index, errors='coerce')

    # Remove recommendations matching the user based material ids
    if((user_based_results is not None) and len(user_based_results) > 0):
        user_based_mat_ids = list(user_based_results["id"])
        df_sim_scores = df_sim_scores.loc[df_sim_scores.index.isin(user_based_mat_ids) == False]

    # Remove the recommendation of the original material id itself
    # and sort the materials based on the similarity score in descending order
    df_sim_scores = df_sim_scores.loc[df_sim_scores.index != mat_id].sort_values(ascending=False)

    # Get the scores of the n most similar materials
    df_sim_scores = df_sim_scores[0:n]

    # Return the top 10 most similar materials
    results = full_dataset.loc[full_dataset["id"].isin(df_sim_scores.index)]

    #Order the results as per the order in the similarity_matrix
    results = results.iloc[pd.Categorical(results.id, df_sim_scores.index).argsort()]

    return results, orig_material

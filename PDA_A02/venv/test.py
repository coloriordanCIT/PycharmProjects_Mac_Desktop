# import modules


import numpy as np
import pandas as pd


def main():

    # get user limit input, with data validation
    # i.e. num no greater than number of actors
    # limit = get_num_input(1, (get_num_actors() + 1), False)

    # create data frame from our data set
    df = pd.read_csv("/Users/colinoriordan/PycharmProjects/PDA_A02/venv/movie_metadata.csv")

    df.to_csv('/Users/colinoriordan/PycharmProjects/PDA_A02/venv/movie_metadata.csv', na_rep='NULL')

    # create data frames from desired columns
    df_actor1 = df[["actor_1_name"]]
    df_actor2 = df[["actor_2_name"]]
    df_actor3 = df[["actor_3_name"]]
    df_gross = df[["gross"]]

    df_actor1_gross = pd.DataFrame({'actor_name': [df_actor1], 'gross': [df_gross]})
    df_actor2_gross = pd.DataFrame({'actor_name': [df_actor2], 'gross': [df_gross]})
    df_actor3_gross = pd.DataFrame({'actor_name': [df_actor3], 'gross': [df_gross]})

    # merge the data frames
    merged_df = pd.merge(df_actor1_gross, df_actor2_gross, on='actor_name', how='outer')

    print(merged_df)


main()

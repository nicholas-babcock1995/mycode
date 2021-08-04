#!/usr/bin/env python3

import pandas as pd
def main():

    excel_file = 'movies.xls'

    movies = pd.read_excel(excel_file)
    
    print(movies.head())

    movie_sheet_by_title = pd.read_excel(excel_file,sheet_name=0,index_col=0)
    print(movie_sheet_by_title.head())
    
    # index by the IMDB rating
    movie_sheet_by_rating = pd.read_excel(excel_file,sheet_name=1,index_col=24)
    print(movie_sheet_by_rating.head())

    #Lets print out both of these to their own files

    movie_sheet_by_title.to_excel("moviesByTitle.xlsx")
    movie_sheet_by_rating.to_excel("moviesByRating.xlsx")

if __name__ == "__main__":
    main()

import media
import fresh_tomatoes


# This section is used to initialize the values in the Movie Class for each
# movie

titanic = media.Movie("Titanic",
                      "A seventeen-year-old aristocrat falls in love with a "
                      "kind but poor artist aboard the luxurious, ill-fated "
                      "R.M.S. Titanic",
                      "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",  # noqa
                      "https://www.youtube.com/watch?v=ZQ6klONCq4s")


walk_to_remember = media.Movie("A Walk to Remember",
                               "The story of two North Carolina teens who are "
                               "thrown together after Landon gets into trouble"
                               " and is made to do community service.",
                               "https://upload.wikimedia.org/wikipedia/en/d/dc/A_Walk_to_Remember_Poster.jpg",  # noqa
                               "https://www.youtube.com/watch?v=k3B2XBcp7vA")


the_notebook = media.Movie("The Notebook",
                           "A poor yet passionate young man falls in love with"
                           " a rich young woman but they are soon separated "
                           "because of their social differences.",
                           "https://upload.wikimedia.org/wikipedia/en/8/86/Posternotebook.jpg",  # noqa
                           "https://www.youtube.com/watch?v=4M7LIcH8C9U")


serendipity = media.Movie("Serendipity",
                          "A couple search for each other years after the "
                          "night they first met",
                          "https://upload.wikimedia.org/wikipedia/en/a/a5/Serendipity_poster.jpg",  # noqa
                          "https://www.youtube.com/watch?v=ePU2Ux9JIMM")


the_devil_wears_prada = media.Movie("The Devil Wears Prada",
                                    "A smart but sensible new graduate lands a"
                                    " job as an assistant to the demanding "
                                    "editor-in-chief of a high fashion "
                                    "magazine",
                                    "https://upload.wikimedia.org/wikipedia/en/e/e7/The_Devil_Wears_Prada_main_onesheet.jpg",  # noqa
                                    "https://www.youtube.com/watch?v=XTDSwAxlNhc")  # noqa


life_is_beautiful = media.Movie("Life is Beautiful",
                                "When an open-minded Jewish librarian and his"
                                "son become victims of the Holocaust, he uses"
                                "a perfect mixture of will and humour to"
                                "protect his son from the dangers around"
                                "their camp.",
                                "https://upload.wikimedia.org/wikipedia/en/7/7c/Vitaebella.jpg",  # noqa
                                "https://www.youtube.com/watch?v=pAYEQP8gx3w")


# The list of array of movies is created to pass on to the function
# "open_movie_page" in fresh_tomatoes.py

movies = [titanic, walk_to_remember, the_notebook,
          serendipity, the_devil_wears_prada, life_is_beautiful]

# The below section calls the fresh_tomatoes.py which turns this code into
# a movie website by using the function "open_movies_page"

fresh_tomatoes.open_movies_page(movies)

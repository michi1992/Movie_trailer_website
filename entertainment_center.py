import media
import fresh_tomatoes

#create some movies
forrest_gump = media.Movie("Forrest Gump",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,757,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=uPIEn0M8su0")
avengers = media.Movie("Avengers",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")
into_the_wild = media.Movie("Into the Wild",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAwNDEyODU1MjheQTJeQWpwZ15BbWU2MDc3NDQwNw@@._V1_.jpg",
                            "https://www.youtube.com/watch?v=2LAuzT_x8Ek")
captain_fantastic = media.Movie("Captain Fantastic",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE5OTM0OTY5NF5BMl5BanBnXkFtZTgwMDcxOTQ3ODE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                                "https://www.youtube.com/watch?v=D1kH4OMIOMc")
#group the movies in a list
movies = [forrest_gump, avengers, into_the_wild, captain_fantastic]
fresh_tomatoes.open_movies_page(movies)     #this line does the magic and shows the website

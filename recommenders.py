"""
In this script we define functions for the recommender web
application
"""

# from Automated_Testing.utils import MOVIES
import random
from shutil import move
from utils import MOVIES, nmf_model


def nmf_recommender(query, nmf_model, titles, k=10):
    """This is an nmf-based recommender"""
    return NotImplementedError


def cos_sim_recommender(query, cos_sim_model, titles, k=10):
    """This is an cosine-similarity-based recommender"""
    return NotImplementedError


def random_recommender(k=2):
    if k > len(MOVIES):
        print(f"exceeded allowed numbers of movies : {len(MOVIES)}")
        return []
    else:
        random.shuffle(MOVIES)
        top_k = MOVIES[:k]
        return top_k


if __name__ == "__main__":
    top2 = random_recommender()
    print(top2)

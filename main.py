# main.py

from youtube_search import youtube_search
from display_results import display_results

def main():
    query = input("Enter a search query: ")
    results = youtube_search(query)
    display_results(results)

if __name__ == '__main__':
    main()
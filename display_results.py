# display_results.py

def display_results(results):
    if results and 'items' in results:
        for index, item in enumerate(results['items']):
            video_title = item['snippet']['title']
            video_description = item['snippet']['description']
            video_id = item['id']['videoId']
            video_url = f"https://www.youtube.com/watch?v={video_id}"

            print(f"\nResult {index+1}:")
            print(f"Title: {video_title}")
            print(f"Description: {video_description}")
            print(f"Watch here: {video_url}")
    else:
        print("No results found.")
        
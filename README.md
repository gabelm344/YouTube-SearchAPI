# YouTube-SearchAPI
Uses a YouTube API key to search for specific details on videos.
## Issues

1. **API Documentation Struggles**:
   - I initially had difficulty with the documentation used for working with APIs. There was a pretty big learning curve, especially when it came to structuring the API integration properly.

2. **Mistake with .env File**:
   - I accidentally created the .env file as a .py file, thinking I could combine everything into one file. While it might have been possible, I decided to separate them to avoid any potential future issues.

3. **API Key Loading Issue**:
   - I encountered an issue with the API key not loading correctly, which prevented the YouTube search functionality from working. The problem started from how the I input the only line in the .env file. I thought I had fixed it when switching my code format, but I hadn't and didn't realize until testing.

4. **No Search Results**:
   - After fixing the API key loading issue, I ran into another problem: the YouTube API returned "No results found" for my search queries. This happened because the API key was initially disabled. I had to go into the Google Cloud Console to enable it.

5. **Mistake When Changing the Format of My Code**:
   - While changing the format of my code into three separate .py files for better organization, I made an messed up when transferring the API key between the .env file and youtube_search.py. This caused issues with loading the API key properly until I was able to fix it as I said above.



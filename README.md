# Automotive Solution Tool 

This web application uses [The NHTSA](https://www.nhtsa.gov/nhtsa-datasets-and-apis#recalls/) API, [Flickr]( https://www.flickr.com/services/developer/api/) API, [Yelp]( https://docs.developer.yelp.com/reference/v3_business_search) API, and the [YouTube](https://developers.google.com/youtube/v3/quickstart/python) API to help users make informed decisions on a car they plan to purchase. 


## Description

This application will get recall information from the NTSHA website base on the Year, Make, and Model of a car. It will then show three pictures of that car along with YouTube videos regarding the car’s recall(s) and finally, shows the top rated auto shops on yelp that can fix those recall issues. 


## To install and run

* Clone our repository at: Mr-3rd/MCTC_ITEC2905_fall2023_proj3_team03_Justin_Amy_Peng (github.com)
* You will need to create your [Flickr API key]( https://www.flickr.com/services/developer/api/). 
* You will need to create your [Yelp API key]( https://docs.developer.yelp.com/reference/v3_business_search). 
* You will need to create your [YouTube API key](https://developers.google.com/youtube/registering_an_application). You will need just the API key, you can disregard the OAuth credentials.  
* Create an environment variable **FLICKR_API ** holding your Flickr API key.
* Create an environment variable **YELP_API ** holding your Yelp API key.
* Create an environment variable **YOUTUBE_API ** holding your YouTube API key.

* Create and activate virtual environment using Python
* `pip install -r requirements.txt`
* `python app.py`

Your App will run on http://127.0.0.1:5000

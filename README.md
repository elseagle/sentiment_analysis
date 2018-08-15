# Twitter Sentiment API
An api that helps to get sentiments about companies and celebrities

## How to Use

url = "https://api-devclan.herokuapp.com/api_server/sentiment"

payload = {'Sentiment': **'name_of_celebrity_or_company'**, 'Number': **no_of _tweet**} `limit=400`

r = request.post(url, data=payload)

sentiments = r.json()

### Response Format

{"percentages": 
                    {
                    "positive": 80 ,
                    "negative": 10, 
                    "neutral": 10
                    },
                "time" : "Wed, 15 Aug 2018 07:37:33 GMT"
                }

------------------------------------------------------------------------------------------
 where '**'name_of_celebrity_or_company'** is the exact name of brand or celebrity you'll like to fetch sentiment data on.

 To test with a UI, [click here](https://api-devclan.herokuapp.com/)



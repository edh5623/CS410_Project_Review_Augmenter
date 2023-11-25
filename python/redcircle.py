import json
import nlp
import requests
from config import api_key


def get_top_reviews_and_ratings(query, url):
    reviews_json = get_reviews(url)

    (five_star_rating, sentiment_rating) = get_ratings(reviews_json)
    reviews = parse_reviews(reviews_json)

    ranked = nlp.rank(query, docs=reviews)

    return {"five_star_rating" : five_star_rating, "sentiment_rating" : sentiment_rating, "ranked_reviews" : ranked}


def get_ratings(reviews_json):
    five_star = reviews_json["summary"]["rating"]

    # average sentiment score of every review
    sentiment_rating_sum = 0
    for review in reviews_json["reviews"]:
        sentiment_rating_sum += nlp.sentiment(review["body"])
    num_reviews = len(reviews_json["reviews"])

    return five_star, round(sentiment_rating_sum / num_reviews, 2)


def parse_reviews(reviews_json):
    return [review["body"] for review in reviews_json["reviews"]]


def get_reviews(url):
    params = {
        'api_key': api_key,
        'type': 'reviews',
        'url': url
    }

    # make the http GET request to RedCircle API
    api_result = requests.get('https://api.redcircleapi.com/request', params)

    # print the JSON response from RedCircle API
    json_result = api_result.json()
    print(json.dumps(json_result))
    return json_result


def get_sample_reviews_json():
    sample = """
    {
      "request_info": {
        "success": true,
        "credits_used": 1,
        "credits_remaining": 999
      },
      "request_metadata": {
        "created_at": "2022-01-01T00:00:00.000Z",
        "processed_at": "2022-01-01T00:00:00.001Z",
        "total_time_taken": 0.1
      },
      "request_parameters": {
        "type": "reviews",
        "tcin": "78025470"
      },
      "reviews": [
        {
          "position": 1,
          "id": "c6d8c3a7-2540-42ff-bc97-8cc6540a09a9",
          "title": "Awesome",
          "body": "Bright and last a long time. My kids use them as regular markers and they hold up.",
          "date": "2021-03-10T17:22:50.000Z",
          "rating": 5,
          "positive_feedback": 1,
          "source": {
            "is_external_source": false,
            "author_name": "SnakeDork",
            "author_id": "1413799033",
            "verified_purchase": true
          }
        },
        {
          "position": 2,
          "id": "7b88d6d0-e9f2-4fe0-818c-334de2c6c9bb",
          "title": "Work great",
          "body": "[This review was collected as part of a promotion.] I use these highlighters on a daily basis and they’re still going strong. I went for this bigger pack because I have two desks at home so I can have the same colored highlighters at either spot without having to fetch from the other desk. These markers are always super vibrant and don’t bleed through regular copy paper.",
          "date": "2021-02-10T15:22:27.000Z",
          "rating": 5,
          "source": {
            "is_external_source": true,
            "external_source": "Sharpie",
            "syndication_source": "bazaarvoice",
            "author_name": "Lishglam",
            "author_id": "a931cbf1-c434-5ce4-8678-a7a49ce2a50c",
            "verified_purchase": false
          }
        },
        {
          "position": 3,
          "id": "9e674484-9e1f-4033-93b5-5f39f9773a85",
          "title": "Works great!",
          "body": "[This review was collected as part of a promotion.] I use highlighters all the time for my bills and my child uses them for school work and a lot of them run out or fade quickly. So far using the Sharpie highlighters they have worked great. The quality has been superb and I have been extremely happy with them. I have used all of them consistently throughout the month and they are all still as bright as they were in the beginning.",
          "date": "2021-02-08T17:19:03.000Z",
          "rating": 5,
          "source": {
            "is_external_source": true,
            "external_source": "Sharpie",
            "syndication_source": "bazaarvoice",
            "author_name": "CresantM",
            "author_id": "e4cbd19b-17a8-5187-acfc-7a32e1c8d8d4",
            "verified_purchase": false
          }
        },
        {
          "position": 4,
          "id": "6314329b-7d67-4d20-ad88-cab5a61849c9",
          "title": "Dissapointed",
          "body": "Two of the highlighters “tips” broke off while I was using them to highlight my school notes. Highlighters only lasted 1 week.",
          "date": "2021-02-05T20:35:11.000Z",
          "rating": 1,
          "source": {
            "is_external_source": false,
            "author_name": "EBBEAN",
            "author_id": "7975913997",
            "verified_purchase": false
          },
          "main_image": "https://target.scene7.com/is/image/Target/GUEST_1e4f2325-3e56-4e88-a57d-5dab05b0f29c"
        },
        {
          "position": 5,
          "id": "4ea0d9ba-df06-4542-9eed-783663a2ddc0",
          "title": "Bright and Vibrant!!!",
          "body": "[This review was collected as part of a promotion.] I love these Sharpie highlighters. The colors are bright and vibrant. It’s easy to see the wording through the highlight. They are slimmer and easy to hold. With a few different colors, I can take notes and highlight according to importance. I love using them.",
          "date": "2021-02-01T21:03:54.000Z",
          "rating": 5,
          "source": {
            "is_external_source": true,
            "external_source": "Sharpie",
            "syndication_source": "bazaarvoice",
            "author_name": "aja3ez",
            "author_id": "8b9d4fd8-870e-519c-88f5-f30e39b31e64",
            "verified_purchase": false
          }
        },
        {
          "position": 6,
          "id": "70772581-4d6f-4466-91f8-bc318531fc38",
          "title": "Sharpie highlighter",
          "body": "The price for this 4 pack is unbeatable. And they last long.",
          "date": "2021-01-31T20:44:03.000Z",
          "rating": 5,
          "positive_feedback": 1,
          "source": {
            "is_external_source": false,
            "author_name": "MamaT",
            "author_id": "7981599482",
            "verified_purchase": true
          }
        },
        {
          "position": 7,
          "id": "b597d54c-93e8-4b2e-8a00-2e2a8106ed25",
          "title": "Great",
          "body": "Perfect for school! Exactly what my child needed.",
          "date": "2021-01-30T21:46:44.000Z",
          "rating": 5,
          "source": {
            "is_external_source": false,
            "author_name": "Target Fan",
            "author_id": "433859762",
            "verified_purchase": false
          }
        },
        {
          "position": 8,
          "id": "ba962e3b-5311-4ce1-80cf-069f2f3830e0",
          "title": "Bright colors !",
          "body": "[This review was collected as part of a promotion.] The colors of these sharpies are very bright and really stand out. I like that they have the smear guard because it doesn't look messy. I also like that these highlighters are easier to hold than those bigger rounder highlighters.",
          "date": "2021-01-29T17:47:13.000Z",
          "rating": 5,
          "source": {
            "is_external_source": true,
            "external_source": "Sharpie",
            "syndication_source": "bazaarvoice",
            "author_name": "Danieljoshua",
            "author_id": "34f104bf-7b60-575a-8986-2ab85bf1b67c",
            "verified_purchase": false
          }
        },
        {
          "position": 9,
          "id": "8c43f345-6c87-44e4-9816-208412a7418b",
          "title": "perfect colors",
          "body": "[This review was collected as part of a promotion.] Sharpies have always been my favorite and I have that this pack comes with so many colors to use! It year helps when highlighting notes to study. These seem to work forever and never dry out. I love that they are also no smear.",
          "date": "2021-01-27T02:47:08.000Z",
          "rating": 5,
          "source": {
            "is_external_source": true,
            "external_source": "Sharpie",
            "syndication_source": "bazaarvoice",
            "author_name": "ScottN",
            "author_id": "5d867097-5767-52c7-9586-2fa7220f92ab",
            "verified_purchase": false
          }
        },
        {
          "position": 10,
          "id": "6eef1c79-3904-4399-a128-6735f93c5849",
          "title": "Great colors!",
          "body": "[This review was collected as part of a promotion.] These colors were a big hit in the office. We love yellow but we want COLOR. Quality Sharpie design! This set of highlighters is perfect for school, work or bible study. I will definitely buy these again!",
          "date": "2021-01-26T21:56:36.000Z",
          "rating": 5,
          "source": {
            "is_external_source": true,
            "external_source": "Sharpie",
            "syndication_source": "bazaarvoice",
            "author_name": "itygfma",
            "author_id": "cbcbdcf0-a272-59de-8b4f-f12840d13a29",
            "verified_purchase": false
          }
        }
      ],
      "summary": {
        "rating": 4.7,
        "ratings_total": 77,
        "recommended_percentage": 87,
        "rating_breakdown": {
          "one_star": 6,
          "two_star": 4,
          "three_star": 6,
          "four_star": 25,
          "five_star": 200
        }
      },
      "pagination": {
        "current_page": 1,
        "total_pages": 8,
        "next_page": 2
      }
    }
    """
    return json.loads(sample)

def bbal():
    js = """
    {
  "pagination": {
    "total_pages": 1,
    "current_page": 1
  },
  "request_parameters": {
    "type": "reviews",
    "url": "https://www.target.com/p/wilson-nba-forge-size-6-basketball/-/A-82153637#lnk=sametab"
  },
  "request_metadata": {
    "total_time_taken": 0.77,
    "target_url": "https://www.target.com/p/-/A-82153637",
    "created_at": "2023-11-12T22:20:07.127Z",
    "processed_at": "2023-11-12T22:20:07.900Z"
  },
  "reviews": [
    {
      "date": "2023-02-28T20:53:25.000Z",
      "source": {
        "author_name": "Kat",
        "author_id": "568543942",
        "verified_purchase": true,
        "is_external_source": false
      },
      "title": "NBA basketball",
      "rating": 5,
      "position": 1,
      "id": "5f47d95a-7e1d-49f6-a5f4-59d0972e6a5c",
      "body": "Great basketball for the price."
    },
    {
      "date": "2022-12-07T03:20:49.000Z",
      "source": {
        "author_name": "AD",
        "author_id": "10008321582",
        "verified_purchase": true,
        "is_external_source": false
      },
      "title": "Zero stars",
      "rating": 1,
      "position": 2,
      "id": "05f31c15-c6b7-49b4-a09b-dc81186b241a",
      "body": "I ordered these as a donation for our school basketball teams. More than half of them won\u2019t hold air!! What a hassle!!",
      "positive_feedback": 1
    },
    {
      "date": "2022-08-14T00:20:59.000Z",
      "source": {
        "author_name": "Nana33",
        "syndication_source": "bazaarvoice",
        "is_external_source": true,
        "external_source": "wilson.com",
        "verified_purchase": false,
        "author_id": "35557073-ee9f-5d0b-b20d-fd6409aa5a34"
      },
      "title": "Great quality.",
      "rating": 5,
      "position": 3,
      "id": "dc40ecac-08ab-4ac5-9e9e-6b28eb14cf5c",
      "body": "This was a replacement for a replacement basketball that was not holding air. So far, so good\u2026happy granddaughter\u2026",
      "positive_feedback": 1
    },
    {
      "date": "2022-01-09T13:58:27.000Z",
      "source": {
        "author_name": "bballjunkie",
        "author_id": "1132061675",
        "verified_purchase": false,
        "is_external_source": false
      },
      "title": "Pass the rock, literally.",
      "rating": 3,
      "position": 4,
      "negative_feedback": 1,
      "id": "60c3b84b-981f-4235-8a80-d16081ec8c4f",
      "body": "I like that the ball seems durable and seems told air well. What I don't like is how hard and heavy it feels. Feels like your tossing a brick around. Everybody that played with it was so fearful of getting hit in the face with it. Nothing compares to the evolution ball.",
      "positive_feedback": 1
    },
    {
      "date": "2022-01-07T16:01:26.000Z",
      "source": {
        "author_name": "Flyrod",
        "author_id": "722408228",
        "verified_purchase": true,
        "is_external_source": false
      },
      "title": "Basketball",
      "rating": 5,
      "position": 5,
      "id": "b95fd5b8-ccb4-40dd-aedf-47bd468f820b",
      "body": "Good value for the cost",
      "positive_feedback": 2
    }
  ],
  "summary": {
    "recommended_percentage": 50,
    "rating_breakdown": {
      "five_star": 15,
      "four_star": 1,
      "one_star": 1,
      "two_star": 0,
      "three_star": 1
    },
    "ratings_total": 5,
    "rating": 4.61
  },
  "request_info": {
    "credits_used": 1,
    "credits_used_this_request": 1,
    "success": true,
    "credits_remaining": 99
  }
}
    """
    return json.loads(js)

# parse_reviews(get_sample_reviews_json())

# print(get_top_reviews("does it gold air?", ""))
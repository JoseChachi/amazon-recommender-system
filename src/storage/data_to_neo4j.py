

import json

itemsFile = open("../../data/raw/itemsprueba1.jsonl", encoding="utf-8")
file = open("load_items.cypher", "w", encoding="utf-8")

file.write("CREATE\n")

#(russell:PLAYER{name:"Russell Westbrook", age: 33, number: 0, height: 1.91, weight: 91}),
while True:
    itemLine = itemsFile.readline()

    if not itemLine:
        break

    itemJson = json.loads(itemLine)

    prettyItemJson = json.dumps(itemJson, indent=4)

    # print(prettyItemJson)
    itemStr = formatted_string = f"""({itemJson["parent_asin"]}:ITEM{{
    main_category: "{itemJson.get("main_category", "null")}",
    title: "{itemJson.get("title", "null").replace('"', " ")}",
    average_rating: {itemJson.get("average_rating", "null")},
    rating_number: {itemJson.get("rating_number", "null")},
    features: "{", ".join(itemJson.get("features", [])).replace('"', " ")}",
    description: "{", ".join(itemJson.get("description", [])).replace('"'," ")}",
    price: {str(itemJson.get("price", "null")).replace("None","null")},
    images: "{len(itemJson.get("images", []))} images",
    videos: "{len(itemJson.get("videos", []))} videos",
    store: "{itemJson.get("store", "null")}",
    categories: "{", ".join(itemJson.get("categories", []))}",
    details: "{", ".join(itemJson.get("details", "null"))}",
    parent_asin: "{itemJson.get("parent_asin", "null").replace("None","null")}",
    bought_together: {str(itemJson.get("bought_together", "null")).replace("None","null")}
    }}),\n"""

    file.write(itemStr)
    # Accessing a specific key
    
    # print(data_json["title"])

reviewsFile = open("../../data/raw/reviewsprueba1.jsonl", encoding="utf-8")


# Lista de reviews y los items a los que hacen referencia
reviews = [

]



while True:
    reviewLine = reviewsFile.readline()

    if not reviewLine:
        file.write("\n")
        break
    
    reviewJson = json.loads(reviewLine)

    prettyreviewJson = json.dumps(reviewJson, indent=4)

    # print(prettyreviewJson)
    reviewid = str(reviewJson.get("user_id", "null"))+str(reviewJson.get("timestamp", "null"))
    reviewStr = f"""({reviewJson["user_id"]}{reviewJson["timestamp"]}:REVIEW{{
    rating: {reviewJson.get("rating", "null")},
    title: "{reviewJson.get("title", "null").replace('"', " ")}",
    text: "{reviewJson.get("text", "null").replace('"', " ")}",
    images: "{len(reviewJson.get("images", []))} images",
    asin: "{reviewJson.get("asin", "null")}",
    parent_asin: "{reviewJson.get("parent_asin", "null")}",
    user_id: "{reviewJson.get("user_id", "null")}",
    timestamp: {reviewJson.get("timestamp", "null")},
    verified_purchase: {reviewJson.get("verified_purchase", "null")},
    helpful_vote: {reviewJson.get("helpful_vote", "null")}
    }})"""
    reviews.append({"review_id": reviewid, "item_id": reviewJson["parent_asin"]})
    # print(reviews)
    file.write(reviewStr)
    file.write(",\n")
    # Accessing a specific key
    
    # print(data_json["title"])

# print(reviews)
# Estructura para almacenar el índice
item_to_reviews = {}

# Construcción del índice
for review in reviews:
    item_id = review["item_id"]
    review_id = review["review_id"]
    if item_id not in item_to_reviews:
        item_to_reviews[item_id] = []
    item_to_reviews[item_id].append(review_id)

# Resultado
# print(item_to_reviews)
# Output: {'i1': ['r1', 'r3'], 'i2': ['r2'], 'i3': ['r4']}


#(joel)<-[:TEAMMATES]- (tobias),

len_item = len(item_to_reviews)
i = 0
for item in item_to_reviews:
    i += 1
    j = 0
    for review in item_to_reviews[item]:
        j += 1
        len_reviews = len(item_to_reviews[item])

        if i == len_item and j == len_reviews:
            file.write(f"({review})-[:REVIEWS]->({item})\n")
        else:
            file.write(f"({review})-[:REVIEWS]->({item}),\n")

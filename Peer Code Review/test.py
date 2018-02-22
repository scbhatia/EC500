import run as apiExercise

# Program One - Regular Test
auth = apiExercise.authorise_twitter_api()
api = apiExercise.tweepy.API(auth, wait_on_rate_limit=True)

try:
    isValid = apiExercise.download_images(api, "NatGeo", 5, "output", 1)
        
except Exception as e:
    print(str(e))
else:
    if (isValid):
        apiExercise.doAnalysis("output")
        print("Program successful!")
    else:
        print("Unable to complete program with selected twitter handle. Please try again.")

# Program Two - Tests for a twitter handle with no images (Successful-returns error)
auth = apiExercise.authorise_twitter_api()
api = apiExercise.tweepy.API(auth, wait_on_rate_limit=True)

try:
    isValid = apiExercise.download_images(api, "scbhatia961", 5, "output", 1)
    apiExercise.doAnalysis("output")
    
except Exception as e:
    print(str(e))

if (isValid):
    print("Program successful!")
else:
    print("Selected twitter feed has no images. Please try again.")
    
# Program Three - Tests for an invalid twitter handle (Successful!)
auth = apiExercise.authorise_twitter_api()
api = apiExercise.tweepy.API(auth, wait_on_rate_limit=True)

try:
    isValid = apiExercise.download_images(api, "asgtsegh", 5, "output", 1)
        
except Exception as e:
    print(str(e))
else:
    if (isValid):
        apiExercise.doAnalysis("output")
        print("Program successful!")
    else:
        print("Unable to complete program with selected twitter handle. Please try again.")


from flask import Flask, redirect, render_template, request, url_for
import run as apiExerise

website = Flask(__name__)

@website.route('/')
def form():
    return render_template("index.html")

@website.route('/', methods=["POST"])
def form_post():
    user = request.form["username"]
    folder = request.form["folder"]
    num = int(request.form["num"])

    auth = apiExercise.authorise_twitter_api()
    api = apiExercise.tweepy.API(auth, wait_on_rate_limit=True)

    try:
        isValid = apiExercise.download_images(api, user, num, folder, 1)
        
    except Exception as e:
        print(str(e))

    else:
        if (isValid):
            apiExercise.doAnalysis("output")
            print("Program successful!")
        else:
            print("Unable to complete program with selected twitter handle. Please try again.")

    return redirect(url_for('submission'))

@website.route('/submission')
def submission():
    with open("labels.json") as outfile:
        lines = json.loads(outfile.read())

    return render_template("output.html")

if __name__ == "__main__":
    website.run(debug=True)

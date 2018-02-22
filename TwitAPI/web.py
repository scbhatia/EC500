from flask import Flask, redirect, render_template, request, url_for
import google_analysis
import image_download
import video_converter

website = Flask(__name__)

@website.route('/')
def form():
    return render_template('index.html')

@website.route('/', methods=['POST'])
def form_post():
    api = image_download.authorization()
        
    try:
        user = request.form['username']
        folder = request.form['output']
        num = int(request.form['num'])

        isValid = image_download.download_images(user, api, num, folder)
        print(user, num, folder)
        
    except Exception as e:
        print(str(e))
        
    return redirect(url_for('cat'))

@website.route('/submission')
def cat():
#    apiExercise.doAnalysis(folder)
#    with open("labels.json") as outfile:
#        lines = json.loads(outfile.read())

    return render_template("output.html")

if __name__ == "__main__":
    website.run(host="0.0.0.0", port=8080, threaded=True)

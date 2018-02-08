# Twitter Image Analysis and Video

## Getting Started
Git clone or download this repository to download all of the files to your local computer. 

### Prerequisites 
1. Python 2.7.xx
2. tweepy (API)
3. Google Cloud Vision (API)
4. Homebrew
5. ffmpeg (Installed on Machine)
### Installing Prerequisites
Installing Python
- Follow instructions on: [Python Download](https://www.python.org/downloads/)

Installing tweepy
```
pip install tweepy
```

Installing Google Cloud Vision
```
pip install --upgrade google-cloud-vision
```

Installing Homebrew 
- Follow instructions on: [Homebrew Download](https://docs.brew.sh/Installation.html)

Installing ffmpeg
```
brew install ffmpeg --with-fdk-aac --with-ffplay --with-freetype --with-frei0r --with-libass --with-libvo-aacenc --with-libvorbis --with-libvpx --with-opencore-amr --with-openjpeg --with-opus --with-rtmpdump --with-schroedinger --with-speex --with-theora --with-tools
```
### API Authentication

### Configuring Files 
config.cfg
```
[API]
consumerKey = 'your key goes here'
consumerSecret = 'your key goes here'
accessToken = 'your key goes here'
accessTokenSecret = 'your key goes here'
```
google_analysis.py
```
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] "\path\to\google\json\file\googleapi.json"
```

## Usage

## Author
Shivani Bhatia 

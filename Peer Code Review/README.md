# Testing @gvikram31's API
A copy of this repository can be found at [GVikram31's Reposity](https://github.com/gvikram31/EC500/blob/miniproj2/)

## test.py
This file contains 3 tests to test the API. In order to use, comment all but one out. The tests are as follows:
 1. Regular test. Retrieves tweets from National Geographic (@NatGeo). This was successful! 
 2. Tries to test program with a twitter handle with no pictures. This was successful!
 3. Tries to test program with an invalid twitter handle. This was successful! 
 
## Code Review
The code review has been finished. All review comments regarding the API are under the 'Issues' section. 7 code review issues have been found.
 1. Exception Handling - Number of Tweets
 2. Unicode Error
 3. Comments
 4. Writing image name to file
 5. Long runtime
 6. Running program multiple times leaves old images
 7. Program freezes
 
Program performance is synchronus. All descriptions are written to terminal and file after the images are downloaded and the video has been made. 

## Website
The website was built using Flask for Python and can be run using the command:
```python web.py```

After running the command above, open your browser and enter '0.0.0.0:8080/' in the address bar. Doing this will load the home screen, as defined in index.html. There, you will be prompted to enter a twitter handle, the destnation folder, and the number of images you would like in the video. Clicking the submit button runs the program with @gvikram31's API. After the processing is completed, you will be directed to '0.0.0.0:8080/submission', whose HTML is defined in output.html. This page will display the video and the descriptions of the images below the video. One thing to note is that the implementation of this website runs slowly when the user is close to exceeding the rate limit, as well as when more images are added. 

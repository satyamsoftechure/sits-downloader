SITS DOWNLOADER

Overview

The SITS Downloader is a tool that allows users to download videos from YouTube, Facebook, Instagram , Twitter, Snapchat or linkedin and more in different formats (including audio, video). The tool supports various quality options, allowing users to choose their preferred format and quality for download with best quality audio. 

URL - "http://{domain}/"

It provides two main API endpoints: one to display available media formats and another to download the selected media file.

1. Display Available Formats

    URL: http://{domain}/api/get-media-format/

            Method: POST
            Body: form-data
            Key: url (required)
            Value: The URL of the YouTube video to download.
            Key: format_type (optional)
            Value: The type of format to retrieve. Accepts values: all (default), audio, or video.

            Description: This endpoint returns a list of available formats for a given YouTube, Facebook, Instagram video URL. Users can specify whether they want to see all formats, only audio formats, or only video formats.


            Request Headers

            Authorization - fhbwrygyg34788fgwryf2348vf
            Origin  - 127.0.0.1:8000

            Body - form-data
            url - https://www.example.com/video/C_ir8-uo0_L/?igsh=amcxOHdwM2JsZzcz
            format_type - all, audio , video


2. Download Media File

    URL: http://{domain}/api/get-media-file/

            Method: POST
            Body: form-data
            Key: url (required)
            Value: The URL of the YouTube video to download.
            Key: format_id (required)
            Value: The ID of the format selected from the list provided by the get-media-format endpoint.

            Description: This endpoint initiates the download of the specified media file in the selected format and quality. Provide the format_id obtained from the get-media-format endpoint to specify the desired format.


            Request Headers

            Authorization - fhbwrygyg34788fgwryf2348vf
            Origin - 127.0.0.1:8000

            Body - form-data
            url - https://www.example.com/video/C_ir8-uo0_L/?igsh=amcxOHdwM2JsZzcz
            format_id - 123






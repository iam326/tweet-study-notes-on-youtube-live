#!/usr/bin/env python3

import urllib.parse

from youtube_live_streaming_api_client import YoutubeLiveStreamingApiClient

YOUTUBE_CLIENT_SECRETS_FILE = 'client_secrets.json'
YOUTUBE_CLIENT_SCOPES = [
    'https://www.googleapis.com/auth/youtube.readonly']


def main():
    youtube = YoutubeLiveStreamingApiClient(
        YOUTUBE_CLIENT_SECRETS_FILE, YOUTUBE_CLIENT_SCOPES)

    url = input('YouTube Live URL: ')
    live_id = urllib.parse.urlparse(url).path[1:]
    live_chat_id = youtube.get_live_chat_id(live_id)

    next_page_token = None

    while True:
        live_chat_messages = youtube.get_live_chat_messages(
            live_chat_id=live_chat_id, forMine=True, next_page_token=next_page_token)

        if len(live_chat_messages['messages']) == 0:
            break

        for message in live_chat_messages['messages']:
            print(message)

        next_page_token = live_chat_messages['next_page_token']

    print('done!')


if __name__ == '__main__':
    main()

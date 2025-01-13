import json

def load_json(file_path):
    with open(file_path) as f:
        data = json.load(f)

    for name, value in data.items():
        for video in value:
            if video:
                for transcript_type in ['generated', 'manual']:
                    if type(video[transcript_type]) == list:
                        for item in video[transcript_type]:
                            item['text'] = item['text'].replace('\xa0\n', ' ').replace('\u2019', "'")
    return data
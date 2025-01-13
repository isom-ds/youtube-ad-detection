import pandas as pd

def convert_to_df(data):
    output = {
        'channel': [],
        'video_id' : [],
        'ads' : [],
        'kw_generated' : [],
        'kw_manual' : [],
        'gpt_generated' : [],
        'gpt_manual' : [],
        'generated': [],
        'manual': []
    }
    for channel, value in data.items():
        for video in value:
            output['channel'].append(channel)
            output['video_id'].append(video['metadata']['videoId'])
            if 'ads' in video['metadata'].keys():
                output['ads'].append(video['metadata']['contains_ad'])
            if video['metadata']['kw']['generated']:
                output['kw_generated'].append(video['metadata']['kw']['generated'])
            else:
                output['kw_generated'].append(None)
            if video['metadata']['kw']['manual']:
                output['kw_manual'].append(video['metadata']['kw']['manual'])
            else:
                output['kw_manual'].append(None)
            if video['metadata']['gpt']['generated']:
                output['gpt_generated'].append(video['metadata']['gpt']['generated'])
            else:
                output['gpt_generated'].append(None)
            if video['metadata']['gpt']['manual']:
                output['gpt_manual'].append(video['metadata']['gpt']['manual'])
            else:
                output['gpt_manual'].append(None)
            if video['manual']:
                output['manual'].append(video['manual'])
            else:
                output['manual'].append(None)
            if video['generated']:
                output['generated'].append(video['generated'])
            else:
                output['generated'].append(None)
    if len(output['ads']) == 0:
        del output['ads']
    return pd.DataFrame(output)
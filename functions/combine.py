from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# Get the list of English stopwords
stop_words = set(stopwords.words('english'))
# Lemmatizer
lemmatizer = WordNetLemmatizer()

def combine_timestamps(data):
    strings = [i['text'] for i in data if i and i['text']]
    tokenised = [word_tokenize(text) for text in strings]
    filtered = [' '.join([word for word in words if word.lower() not in stop_words]) for words in tokenised]
    lemmatized_words = [lemmatizer.lemmatize(word) for word in ' '.join(filtered).split()]
    single_string = ' '.join(lemmatized_words)

    return single_string

# Transcripts
def combine_transcripts(data, print_stats=False):
    combined_transcripts = {}
    for channel, value in data.items():
        combined_transcripts[channel] = []
        for video in value:
            if video and video['manual']:
                manual_combined = combine_timestamps(video['manual'])
            else:
                manual_combined = None
            if video and video['generated']:
                generated_combined = combine_timestamps(video['generated'])
            else:
                generated_combined = None
            if 'metadata' in video.keys():
                x = 'metadata'
            else:
                x = 'videoId'
            combined_transcripts[channel].append(
                {
                    x: video[x],
                    'manual': manual_combined,
                    'generated': generated_combined
                }
            )

    if print_stats:
        for name in ['SciShow', 'Johnny Harris', 'PBS Space Time', '3Blue1Brown', 'DamiLee', 'Fireship']:
            n_generated = len([i['generated'] for i in combined_transcripts[name] if i and i.get('generated')])
            n_manual = len([i['manual'] for i in combined_transcripts[name] if i and i.get('manual')])
            print(f"{name}: Generated = {n_generated} Manual = {n_manual}")

    return combined_transcripts
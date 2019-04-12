from collections import Counter

def get_word_frequencies_from_column(review_text):
  word_frequencies = Counter()
  for _, text in review_text.iteritems():
    tokens = text.split()
    word_frequencies.update(tokens)

  return word_frequencies
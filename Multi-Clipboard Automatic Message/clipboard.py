import sys
from pyperclip import copy

TEXT = {
    "agree": "Yes, I agree. That sounds fine to me.",
    "busy": "Sorry, can we do this later this week or next week?",
    "upsell": "Would you consider making this a monthly donation?",
}

if len(sys.argv) < 2:
    print("Usage: python clipboard.py [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    copy(TEXT[keyphrase])
    print(f"Text for the keyphrase has been copied to clipboard: {keyphrase}")
else:
    print(f"No text for the keyphrase: {keyphrase}")

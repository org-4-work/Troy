import re
def replace_special_chars_in_list(sentences_list, lang='en'):
    return sentences_list
# noticed not change in the output, but maybe implement this later
    cleaned_list = []
    if lang == 'en':
        # English special characters
        special_chars = r'!@#$%^&*()_+{}|:"<>?-=[];\',./`~\\'
    elif lang == 'zh':
        # Chinese special characters
        special_chars = r'！@#¥%……&*（）——+{}|：“《》？【】、；‘’，。、/~·【】'

    # Replace special characters with spaces
    for sentence in sentences_list:
        cleaned_text = re.sub(f"[{special_chars}]", ' ', sentence)
        cl = cleaned_text.strip()
        if cl is None:
            cleaned_list.append("")
        else:
            cleaned_list.append(cl)
    return cleaned_list
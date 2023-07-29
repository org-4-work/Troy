import re
def get_numbers_in_text(text):
    pattern = r'[0-9]+(?:[.,][0-9]*)?'
    numbers = re.findall(pattern, text)
    numbers_in_text = []
    for num in numbers:
        num = num.replace(',', '').replace('，', '')  # Remove commas and other special characters
        if '.' in num:
            numbers_in_text.append(float(num))
        else:
            numbers_in_text.append(int(num))
    return numbers_in_text

def numbers_matching_score(translated, original):
    # Regular expression pattern to match both integers and floats
    # Find all occurrences of the pattern in the text
    numbers_in_original = get_numbers_in_text(original)
    numbers_in_translated = get_numbers_in_text(translated)   
    
    # Initialize the results list to store numbers that don't match
    results = []
    
    # Determine the length of the shortest array
    min_length = min(len(numbers_in_original), len(numbers_in_translated))
    
    # Loop through the shortest array and compare elements
    for i in range(min_length):
        if numbers_in_translated[i] != numbers_in_original[i]:
            results.append(numbers_in_original[i])
    
    # If numbers_in_translated has more elements than numbers_in_original, cut those extra elements
    missing_element = []
    if len(numbers_in_translated) > min_length:
        missing_element = numbers_in_translated[min_length:]
    

    
    return {"missing_numbers":missing_element, "incorrect_numbers":results}
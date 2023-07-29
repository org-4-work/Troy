import re
def extract_numerical_values(text):
    """
    Extract Numerical Values from English and Chinese Text
    Args:
        text: The input text
    Returns:
        A list of tuples containing the numerical value and its index in the paragraph.
    """
    numerical_values = re.findall(r'\d+', text)
    indices = [m.start() for m in re.finditer(r'\d+', text)]
    extracted_values = list(zip(numerical_values, indices))
    return extracted_values


# en = 'Fund launch date: 28 February 1995'
# ch =  '基金推出日期：1995年2 月28 日'
en = 'Class 1:	GBP 2,000 initial, GBP 1,000 additional'

ch =  '第1 類：首次投資額為2,000 英鎊，其後認購額為1,000 英鎊'
# ['# The ongoing charges figure is based on the total asset management fee and operating expenses in accordance with the interim financial statement for the 6-month period ended 7 September 2021 and is expressed as a percentage of the average net asset value of the share class over the same period. This figure may vary from year to year.', '持續費用數額是基於截至2021年9 月7 日止6個月期間的中期財務 報表的年化資產管理費及經營開支總額計算，，並根據所佔該股份類別同期估計平均資產淨值的百分比列示。此數額可能每年皆有出入。', 0.822]  
# ['Class 1: Up to 5.00% of the gross amount invested', '第1 類：最高為投資總額的5.00%', 0.806]
en_nu = extract_numerical_values(en)
ch_nu = extract_numerical_values(ch)

print(en_nu,ch_nu)

diff_numerical = []
for en in en_nu:
    flag = 1
    for ch in ch_nu:
        if en[0] == ch[0]:
            flag = 0
            break
    if flag :
        diff_numerical.append(en)

print(diff_numerical)




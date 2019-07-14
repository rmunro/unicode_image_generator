# -*- coding: utf-8 -*-

"""UNICODE CHARACTER GENERATOR

A script to generate image files for each character in the
first plane of Unicode

"""

import sys
import os
import unicodedata as ucd
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import filecmp
import numpy as np
from random import shuffle

xsize = 128 # size of images
ysize = 128
xoffset=32 # offset to centralize characters in image
yoffset=32
font = "Arial Unicode.ttf"  # font file to use
fontsize=64

# number of characters to randomly select per block
# set to a v. high number to generate every character
total_per_block = 256 


directory = "unicode_jpgs"
if not os.path.exists(directory):
    os.makedirs(directory)
directory += "/"

letter = chr(10)
empty = directory+"empty.jpg" # get empty to use a reference for when the script didn't render a character
image = Image.new('RGB', (xsize, ysize), (256,256,256))
draw = ImageDraw.Draw(image)
draw.text((xoffset, yoffset), letter, font=ImageFont.truetype(font, fontsize), fill=(0,0,0))
image.save(empty, "JPEG")

letter = chr(1)
unsupported = directory+"unsupported.jpg" # get unsupported to use a reference for when the script didn't render a character
image = Image.new('RGB', (xsize, ysize), (256,256,256))
draw = ImageDraw.Draw(image)
draw.text((xoffset, yoffset), letter, font=ImageFont.truetype(font, fontsize), fill=(0,0,0))
image.save(unsupported, "JPEG")

# Array of all the blocks within the first plane of unicode. 
# Note: Array was generated programmatically from wikipedia page 
unicode_ranges = ["0000", "007F", "Basic Latin[g]", "128", "128", "Latin (52 characters), Common (76 characters)"], ["0080", "00FF", "Latin-1 Supplement[h]", "128", "128", "Latin (64 characters), Common (64 characters)"], ["0100", "017F", "Latin Extended-A", "128", "128", "Latin"], ["0180", "024F", "Latin Extended-B", "208", "208", "Latin"], ["0250", "02AF", "IPA Extensions", "96", "96", "Latin"], ["02B0", "02FF", "Spacing Modifier Letters", "80", "80", "Bopomofo (2 characters), Latin (14 characters), Common (64 characters)"], ["0300", "036F", "Combining Diacritical Marks", "112", "112", "Inherited"], ["0370", "03FF", "Greek and Coptic", "144", "135", "Coptic (14 characters), Greek (117 characters), Common (4 characters)"], ["0400", "04FF", "Cyrillic", "256", "256", "Cyrillic (254 characters), Inherited (2 characters)"], ["0500", "052F", "Cyrillic Supplement", "48", "48", "Cyrillic"], ["0530", "058F", "Armenian", "96", "91", "Armenian (90 characters), Common (1 character)"], ["0590", "05FF", "Hebrew", "112", "88", "Hebrew"], ["0600", "06FF", "Arabic", "256", "255", "Arabic (237 characters), Common (6 characters), Inherited (12 characters)"], ["0700", "074F", "Syriac", "80", "77", "Syriac"], ["0750", "077F", "Arabic Supplement", "48", "48", "Arabic"], ["0780", "07BF", "Thaana", "64", "50", "Thaana"], ["07C0", "07FF", "NKo", "64", "62", "Nko"], ["0800", "083F", "Samaritan", "64", "61", "Samaritan"], ["0840", "085F", "Mandaic", "32", "29", "Mandaic"], ["0860", "086F", "Syriac Supplement", "16", "11", "Syriac"], ["08A0", "08FF", "Arabic Extended-A", "96", "74", "Arabic (73 characters), Common (1 character)"], ["0900", "097F", "Devanagari", "128", "128", "Devanagari (122 characters), Common (2 characters), Inherited (4 characters)"], ["0980", "09FF", "Bengali", "128", "96", "Bengali"], ["0A00", "0A7F", "Gurmukhi", "128", "80", "Gurmukhi"], ["0A80", "0AFF", "Gujarati", "128", "91", "Gujarati"], ["0B00", "0B7F", "Oriya", "128", "90", "Oriya"], ["0B80", "0BFF", "Tamil", "128", "72", "Tamil"], ["0C00", "0C7F", "Telugu", "128", "98", "Telugu"], ["0C80", "0CFF", "Kannada", "128", "89", "Kannada"], ["0D00", "0D7F", "Malayalam", "128", "117", "Malayalam"], ["0D80", "0DFF", "Sinhala", "128", "90", "Sinhala"], ["0E00", "0E7F", "Thai", "128", "87", "Thai (86 characters), Common (1 character)"], ["0E80", "0EFF", "Lao", "128", "82", "Lao"], ["0F00", "0FFF", "Tibetan", "256", "211", "Tibetan (207 characters), Common (4 characters)"], ["1000", "109F", "Myanmar", "160", "160", "Myanmar"], ["10A0", "10FF", "Georgian", "96", "88", "Georgian (87 characters), Common (1 character)"], ["1100", "11FF", "Hangul Jamo", "256", "256", "Hangul"], ["1200", "137F", "Ethiopic", "384", "358", "Ethiopic"], ["1380", "139F", "Ethiopic Supplement", "32", "26", "Ethiopic"], ["13A0", "13FF", "Cherokee", "96", "92", "Cherokee"], ["1400", "167F", "Unified Canadian Aboriginal Syllabics", "640", "640", "Canadian Aboriginal"], ["1680", "169F", "Ogham", "32", "29", "Ogham"], ["16A0", "16FF", "Runic", "96", "89", "Runic (86 characters), Common (3 characters)"], ["1700", "171F", "Tagalog", "32", "20", "Tagalog"], ["1720", "173F", "Hanunoo", "32", "23", "Hanunoo (21 characters), Common (2 characters)"], ["1740", "175F", "Buhid", "32", "20", "Buhid"], ["1760", "177F", "Tagbanwa", "32", "18", "Tagbanwa"], ["1780", "17FF", "Khmer", "128", "114", "Khmer"], ["1800", "18AF", "Mongolian", "176", "157", "Mongolian (154 characters), Common (3 characters)"], ["18B0", "18FF", "Unified Canadian Aboriginal Syllabics Extended", "80", "70", "Canadian Aboriginal"], ["1900", "194F", "Limbu", "80", "68", "Limbu"], ["1950", "197F", "Tai Le", "48", "35", "Tai Le"], ["1980", "19DF", "New Tai Lue", "96", "83", "New Tai Lue"], ["19E0", "19FF", "Khmer Symbols", "32", "32", "Khmer"], ["1A00", "1A1F", "Buginese", "32", "30", "Buginese"], ["1A20", "1AAF", "Tai Tham", "144", "127", "Tai Tham"], ["1AB0", "1AFF", "Combining Diacritical Marks Extended", "80", "15", "Inherited"], ["1B00", "1B7F", "Balinese", "128", "121", "Balinese"], ["1B80", "1BBF", "Sundanese", "64", "64", "Sundanese"], ["1BC0", "1BFF", "Batak", "64", "56", "Batak"], ["1C00", "1C4F", "Lepcha", "80", "74", "Lepcha"], ["1C50", "1C7F", "Ol Chiki", "48", "48", "Ol Chiki"], ["1C80", "1C8F", "Cyrillic Extended-C", "16", "9", "Cyrillic"], ["1C90", "1CBF", "Georgian Extended", "48", "46", "Georgian"], ["1CC0", "1CCF", "Sundanese Supplement", "16", "8", "Sundanese"], ["1CD0", "1CFF", "Vedic Extensions", "48", "43", "Common (16 characters), Inherited (27 characters)"], ["1D00", "1D7F", "Phonetic Extensions", "128", "128", "Cyrillic (2 characters), Greek (15 characters), Latin (111 characters)"], ["1D80", "1DBF", "Phonetic Extensions Supplement", "64", "64", "Greek (1 character), Latin (63 characters)"], ["1DC0", "1DFF", "Combining Diacritical Marks Supplement", "64", "63", "Inherited"], ["1E00", "1EFF", "Latin Extended Additional", "256", "256", "Latin"], ["1F00", "1FFF", "Greek Extended", "256", "233", "Greek"], ["2000", "206F", "General Punctuation", "112", "111", "Common (109 characters), Inherited (2 characters)"], ["2070", "209F", "Superscripts and Subscripts", "48", "42", "Latin (15 characters), Common (27 characters)"], ["20A0", "20CF", "Currency Symbols", "48", "32", "Common"], ["20D0", "20FF", "Combining Diacritical Marks for Symbols", "48", "33", "Inherited"], ["2100", "214F", "Letterlike Symbols", "80", "80", "Greek (1 character), Latin (4 characters), Common (75 characters)"], ["2150", "218F", "Number Forms", "64", "60", "Latin (41 characters), Common (19 characters)"], ["2190", "21FF", "Arrows", "112", "112", "Common"], ["2200", "22FF", "Mathematical Operators", "256", "256", "Common"], ["2300", "23FF", "Miscellaneous Technical", "256", "256", "Common"], ["2400", "243F", "Control Pictures", "64", "39", "Common"], ["2440", "245F", "Optical Character Recognition", "32", "11", "Common"], ["2460", "24FF", "Enclosed Alphanumerics", "160", "160", "Common"], ["2500", "257F", "Box Drawing", "128", "128", "Common"], ["2580", "259F", "Block Elements", "32", "32", "Common"], ["25A0", "25FF", "Geometric Shapes", "96", "96", "Common"], ["2600", "26FF", "Miscellaneous Symbols", "256", "256", "Common"], ["2700", "27BF", "Dingbats", "192", "192", "Common"], ["27C0", "27EF", "Miscellaneous Mathematical Symbols-A", "48", "48", "Common"], ["27F0", "27FF", "Supplemental Arrows-A", "16", "16", "Common"], ["2800", "28FF", "Braille Patterns", "256", "256", "Braille"], ["2900", "297F", "Supplemental Arrows-B", "128", "128", "Common"], ["2980", "29FF", "Miscellaneous Mathematical Symbols-B", "128", "128", "Common"], ["2A00", "2AFF", "Supplemental Mathematical Operators", "256", "256", "Common"], ["2B00", "2BFF", "Miscellaneous Symbols and Arrows", "256", "252", "Common"], ["2C00", "2C5F", "Glagolitic", "96", "94", "Glagolitic"], ["2C60", "2C7F", "Latin Extended-C", "32", "32", "Latin"], ["2C80", "2CFF", "Coptic", "128", "123", "Coptic"], ["2D00", "2D2F", "Georgian Supplement", "48", "40", "Georgian"], ["2D30", "2D7F", "Tifinagh", "80", "59", "Tifinagh"], ["2D80", "2DDF", "Ethiopic Extended", "96", "79", "Ethiopic"], ["2DE0", "2DFF", "Cyrillic Extended-A", "32", "32", "Cyrillic"], ["2E00", "2E7F", "Supplemental Punctuation", "128", "80", "Common"], ["2E80", "2EFF", "CJK Radicals Supplement", "128", "115", "Han"], ["2F00", "2FDF", "Kangxi Radicals", "224", "214", "Han"], ["2FF0", "2FFF", "Ideographic Description Characters", "16", "12", "Common"], ["3000", "303F", "CJK Symbols and Punctuation", "64", "64", "Han (15 characters), Hangul (2 characters), Common (43 characters), Inherited (4 characters)"], ["3040", "309F", "Hiragana", "96", "93", "Hiragana (89 characters), Common (2 characters), Inherited (2 characters)"], ["30A0", "30FF", "Katakana", "96", "96", "Katakana (93 characters), Common (3 characters)"], ["3100", "312F", "Bopomofo", "48", "43", "Bopomofo"], ["3130", "318F", "Hangul Compatibility Jamo", "96", "94", "Hangul"], ["3190", "319F", "Kanbun", "16", "16", "Common"], ["31A0", "31BF", "Bopomofo Extended", "32", "27", "Bopomofo"], ["31C0", "31EF", "CJK Strokes", "48", "36", "Common"], ["31F0", "31FF", "Katakana Phonetic Extensions", "16", "16", "Katakana"], ["3200", "32FF", "Enclosed CJK Letters and Months", "256", "255", "Hangul (62 characters), Katakana (47 characters), Common (146 characters)"], ["3300", "33FF", "CJK Compatibility", "256", "256", "Katakana (88 characters), Common (168 characters)"], ["3400", "4DBF", "CJK Unified Ideographs Extension A", "6,592", "6,582", "Han"], ["4DC0", "4DFF", "Yijing Hexagram Symbols", "64", "64", "Common"], ["4E00", "9FFF", "CJK Unified Ideographs", "20,992", "20,976", "Han"], ["A000", "A48F", "Yi Syllables", "1,168", "1,165", "Yi"], ["A490", "A4CF", "Yi Radicals", "64", "55", "Yi"], ["A4D0", "A4FF", "Lisu", "48", "48", "Lisu"], ["A500", "A63F", "Vai", "320", "300", "Vai"], ["A640", "A69F", "Cyrillic Extended-B", "96", "96", "Cyrillic"], ["A6A0", "A6FF", "Bamum", "96", "88", "Bamum"], ["A700", "A71F", "Modifier Tone Letters", "32", "32", "Common"], ["A720", "A7FF", "Latin Extended-D", "224", "174", "Latin (169 characters), Common (5 characters)"], ["A800", "A82F", "Syloti Nagri", "48", "44", "Syloti Nagri"], ["A830", "A83F", "Common Indic Number Forms", "16", "10", "Common"], ["A840", "A87F", "Phags-pa", "64", "56", "Phags Pa"], ["A880", "A8DF", "Saurashtra", "96", "82", "Saurashtra"], ["A8E0", "A8FF", "Devanagari Extended", "32", "32", "Devanagari"], ["A900", "A92F", "Kayah Li", "48", "48", "Kayah Li (47 characters), Common (1 character)"], ["A930", "A95F", "Rejang", "48", "37", "Rejang"], ["A960", "A97F", "Hangul Jamo Extended-A", "32", "29", "Hangul"], ["A980", "A9DF", "Javanese", "96", "91", "Javanese (90 characters), Common (1 character)"], ["A9E0", "A9FF", "Myanmar Extended-B", "32", "31", "Myanmar"], ["AA00", "AA5F", "Cham", "96", "83", "Cham"], ["AA60", "AA7F", "Myanmar Extended-A", "32", "32", "Myanmar"], ["AA80", "AADF", "Tai Viet", "96", "72", "Tai Viet"], ["AAE0", "AAFF", "Meetei Mayek Extensions", "32", "23", "Meetei Mayek"], ["AB00", "AB2F", "Ethiopic Extended-A", "48", "32", "Ethiopic"], ["AB30", "AB6F", "Latin Extended-E", "64", "56", "Latin (54 characters), Greek (1 character), Common (1 character)"], ["AB70", "ABBF", "Cherokee Supplement", "80", "80", "Cherokee"], ["ABC0", "ABFF", "Meetei Mayek", "64", "56", "Meetei Mayek"], ["AC00", "D7AF", "Hangul Syllables", "11,184", "11,172", "Hangul"], ["D7B0", "D7FF", "Hangul Jamo Extended-B", "80", "72", "Hangul"], ["D800", "DB7F", "High Surrogates", "896", "0", "Unknown"], ["DB80", "DBFF", "High Private Use Surrogates", "128", "0", "Unknown"], ["DC00", "DFFF", "Low Surrogates", "1,024", "0", "Unknown"], ["E000", "F8FF", "Private Use Area", "6,400", "6,400", "Unknown"], ["F900", "FAFF", "CJK Compatibility Ideographs", "512", "472", "Han"], ["FB00", "FB4F", "Alphabetic Presentation Forms", "80", "58", "Armenian (5 characters), Hebrew (46 characters), Latin (7 characters)"], ["FB50", "FDFF", "Arabic Presentation Forms-A", "688", "611", "Arabic (609 characters), Common (2 characters)"], ["FE00", "FE0F", "Variation Selectors", "16", "16", "Inherited"], ["FE10", "FE1F", "Vertical Forms", "16", "10", "Common"], ["FE20", "FE2F", "Combining Half Marks", "16", "16", "Cyrillic (2 characters), Inherited (14 characters)"], ["FE30", "FE4F", "CJK Compatibility Forms", "32", "32", "Common"], ["FE50", "FE6F", "Small Form Variants", "32", "26", "Common"], ["FE70", "FEFF", "Arabic Presentation Forms-B", "144", "141", "Arabic (140 characters), Common (1 character)"], ["FF00", "FFEF", "Halfwidth and Fullwidth Forms", "240", "225", "Hangul (52 characters), Katakana (55 characters), Latin (52 characters), Common (66 characters)"], ["FFF0", "FFFF", "Specials", "16", "5", "Common"]


# Color mappings for each block
# Note: mapping was generated programmatically
color_mapping = {}
color_mapping[0]=[0,0,0]
color_mapping[1]=[50,0,0]
color_mapping[2]=[100,0,0]
color_mapping[3]=[150,0,0]
color_mapping[4]=[200,0,0]
color_mapping[5]=[250,0,0]
color_mapping[6]=[0,50,0]
color_mapping[7]=[50,50,0]
color_mapping[8]=[100,50,0]
color_mapping[9]=[150,50,0]
color_mapping[10]=[200,50,0]
color_mapping[11]=[250,50,0]
color_mapping[12]=[0,100,0]
color_mapping[13]=[50,100,0]
color_mapping[14]=[100,100,0]
color_mapping[15]=[150,100,0]
color_mapping[16]=[200,100,0]
color_mapping[17]=[250,100,0]
color_mapping[18]=[0,150,0]
color_mapping[19]=[50,150,0]
color_mapping[20]=[100,150,0]
color_mapping[21]=[150,150,0]
color_mapping[22]=[200,150,0]
color_mapping[23]=[250,150,0]
color_mapping[24]=[0,200,0]
color_mapping[25]=[50,200,0]
color_mapping[26]=[100,200,0]
color_mapping[27]=[150,200,0]
color_mapping[28]=[200,200,0]
color_mapping[29]=[250,200,0]
color_mapping[30]=[0,250,0]
color_mapping[31]=[50,250,0]
color_mapping[32]=[100,250,0]
color_mapping[33]=[150,250,0]
color_mapping[34]=[200,250,0]
color_mapping[35]=[250,250,0]
color_mapping[36]=[0,0,50]
color_mapping[37]=[50,0,50]
color_mapping[38]=[100,0,50]
color_mapping[39]=[150,0,50]
color_mapping[40]=[200,0,50]
color_mapping[41]=[250,0,50]
color_mapping[42]=[0,50,50]
color_mapping[43]=[50,50,50]
color_mapping[44]=[100,50,50]
color_mapping[45]=[150,50,50]
color_mapping[46]=[200,50,50]
color_mapping[47]=[250,50,50]
color_mapping[48]=[0,100,50]
color_mapping[49]=[50,100,50]
color_mapping[50]=[100,100,50]
color_mapping[51]=[150,100,50]
color_mapping[52]=[200,100,50]
color_mapping[53]=[250,100,50]
color_mapping[54]=[0,150,50]
color_mapping[55]=[50,150,50]
color_mapping[56]=[100,150,50]
color_mapping[57]=[150,150,50]
color_mapping[58]=[200,150,50]
color_mapping[59]=[250,150,50]
color_mapping[60]=[0,200,50]
color_mapping[61]=[50,200,50]
color_mapping[62]=[100,200,50]
color_mapping[63]=[150,200,50]
color_mapping[64]=[200,200,50]
color_mapping[65]=[250,200,50]
color_mapping[66]=[0,250,50]
color_mapping[67]=[50,250,50]
color_mapping[68]=[100,250,50]
color_mapping[69]=[150,250,50]
color_mapping[70]=[200,250,50]
color_mapping[71]=[250,250,50]
color_mapping[72]=[0,0,100]
color_mapping[73]=[50,0,100]
color_mapping[74]=[100,0,100]
color_mapping[75]=[150,0,100]
color_mapping[76]=[200,0,100]
color_mapping[77]=[250,0,100]
color_mapping[78]=[0,50,100]
color_mapping[79]=[50,50,100]
color_mapping[80]=[100,50,100]
color_mapping[81]=[150,50,100]
color_mapping[82]=[200,50,100]
color_mapping[83]=[250,50,100]
color_mapping[84]=[0,100,100]
color_mapping[85]=[50,100,100]
color_mapping[86]=[100,100,100]
color_mapping[87]=[150,100,100]
color_mapping[88]=[200,100,100]
color_mapping[89]=[250,100,100]
color_mapping[90]=[0,150,100]
color_mapping[91]=[50,150,100]
color_mapping[92]=[100,150,100]
color_mapping[93]=[150,150,100]
color_mapping[94]=[200,150,100]
color_mapping[95]=[250,150,100]
color_mapping[96]=[0,200,100]
color_mapping[97]=[50,200,100]
color_mapping[98]=[100,200,100]
color_mapping[99]=[150,200,100]
color_mapping[100]=[200,200,100]
color_mapping[101]=[250,200,100]
color_mapping[102]=[0,250,100]
color_mapping[103]=[50,250,100]
color_mapping[104]=[100,250,100]
color_mapping[105]=[150,250,100]
color_mapping[106]=[200,250,100]
color_mapping[107]=[0,0,150]
color_mapping[108]=[50,0,150]
color_mapping[109]=[100,0,150]
color_mapping[110]=[150,0,150]
color_mapping[111]=[200,0,150]
color_mapping[112]=[250,0,150]
color_mapping[113]=[0,50,150]
color_mapping[114]=[50,50,150]
color_mapping[115]=[100,50,150]
color_mapping[116]=[150,50,150]
color_mapping[117]=[200,50,150]
color_mapping[118]=[250,50,150]
color_mapping[119]=[0,100,150]
color_mapping[120]=[50,100,150]
color_mapping[121]=[100,100,150]
color_mapping[122]=[150,100,150]
color_mapping[123]=[200,100,150]
color_mapping[124]=[250,100,150]
color_mapping[125]=[0,150,150]
color_mapping[126]=[50,150,150]
color_mapping[127]=[100,150,150]
color_mapping[128]=[150,150,150]
color_mapping[129]=[200,150,150]
color_mapping[130]=[250,150,150]
color_mapping[131]=[0,200,150]
color_mapping[132]=[50,200,150]
color_mapping[133]=[100,200,150]
color_mapping[134]=[150,200,150]
color_mapping[135]=[200,200,150]
color_mapping[136]=[0,250,150]
color_mapping[137]=[50,250,150]
color_mapping[138]=[100,250,150]
color_mapping[139]=[150,250,150]
color_mapping[140]=[0,0,200]
color_mapping[141]=[50,0,200]
color_mapping[142]=[100,0,200]
color_mapping[143]=[150,0,200]
color_mapping[144]=[200,0,200]
color_mapping[145]=[250,0,200]
color_mapping[146]=[0,50,200]
color_mapping[147]=[50,50,200]
color_mapping[148]=[100,50,200]
color_mapping[149]=[150,50,200]
color_mapping[150]=[200,50,200]
color_mapping[151]=[250,50,200]
color_mapping[152]=[0,100,200]
color_mapping[153]=[50,100,200]
color_mapping[154]=[100,100,200]
color_mapping[155]=[150,100,200]
color_mapping[156]=[200,100,200]
color_mapping[157]=[250,100,200]
color_mapping[158]=[0,150,200]
color_mapping[159]=[50,150,200]
color_mapping[160]=[100,150,200]
color_mapping[161]=[150,150,200]
color_mapping[162]=[200,150,200]
color_mapping[163]=[0,200,200]
color_mapping[164]=[50,200,200]

# get rgb for this unicode range (block)
def get_range(decimal):
    index = 0
    for range in unicode_ranges:        
        lower = int(range[0], 16)
        if decimal >= lower:
            upper = int(range[1], 16)
            if decimal <= upper:
                return index
        index += 1
    return index


range_count = {}


letters = []

# everything in first plane (up to 65536, hexadecimal = 10000)
for i in range(65536):
    letters.append(i)

shuffle(letters) # shuffle so we have a random selection in each range/block

for i in letters:
    letter = chr(i)
    name = directory+str(i)+".jpg"

    image = Image.new('RGB', (xsize, ysize), (256,256,256))
    draw = ImageDraw.Draw(image) 
    draw.text((xoffset, yoffset), letter, font=ImageFont.truetype(font, fontsize), fill=(0,0,0))

    image.save(name, "JPEG")

    if filecmp.cmp(name, empty) or filecmp.cmp(name, unsupported):
        os.remove(name)
    else:
        # rewrite as correct color
        image = Image.new('RGB', (xsize, ysize), (256,256,256))
        draw = ImageDraw.Draw(image)
        range = get_range(i)

        if range not in range_count:
            range_count[range] = 0

        if range_count[range] < total_per_block:
            colors = color_mapping[range]
            draw.text((xoffset, yoffset), letter, font=ImageFont.truetype(font, fontsize), fill=(colors[0],colors[1],colors[2]))
            image.save(name, "JPEG")
            range_count[range] += 1
        else:
            # print("skipping for range "+str(i))
            os.remove(name)

os.remove(empty)
os.remove(unsupported)


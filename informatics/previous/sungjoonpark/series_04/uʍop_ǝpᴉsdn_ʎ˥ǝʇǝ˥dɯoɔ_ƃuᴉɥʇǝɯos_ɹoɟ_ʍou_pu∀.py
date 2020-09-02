number_of_lines = int(input())

word_list = {"A":"∀", "B":"q", "C":"Ɔ", "D":"p", "E":"Ǝ", "F":"Ⅎ", "G":"פ", "H":"H", "I":"I", "J":"ſ", "K":"ʞ", "L":"˥", "M":"W", "N":"N", "O":"O", "P":"Ԁ", "Q":"Ό", "R":"ɹ", "S":"S", "T":"┴", "U":"∩", "V":"Λ", "W":"M", "X":"X", "Y":"⅄", "Z":"Z", "a":"ɐ", "b":"q", "c":"ɔ", "d":"p", "e":"ǝ", "f":"ɟ", "g":"ƃ", "h":"ɥ", "i":"ᴉ", "j":"ɾ", "k":"ʞ", "l":"˥", "m":"ɯ", "n":"u", "o":"o", "p":"d", "q":"b", "r":"ɹ", "s":"s", "t":"ʇ", "u":"n", "v":"ʌ", "w":"ʍ", "x":"x", "y":"ʎ", "z":"z", "0":"0", "1":"Ɩ", "2":"ᄅ", "3":"Ɛ", "4":"ㄣ", "5":"ϛ", "6":"9", "7":"ㄥ", "8":"8", "9":"6", "?":"¿", "!":"¡", ".":"˙", "-":"-", "(":")", ")":"(", "<":">", ">":"<", "%":"%", "$":"$", "'":",", ",":"'", ":":":", "_":"‾", " ":" " }

message = ""

for i in range(number_of_lines):
    previous_message = input()
    message += "\n"
    
    for last_message in previous_message:
        
        for j in range(0, len(last_message)):
            list_of_words = word_list[last_message[j]]
            message += list_of_words
            
print(message[::-1].strip())
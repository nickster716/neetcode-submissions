class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for s in strs:
            length = len(s)
            encodedString+= str(length)+ '#' + s

        print(encodedString)
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedStringArr = []
        if len(s) == 0:
            return decodedStringArr
        length = 0
        string = ''

        currLen= ''

        for i in range(len(s)):
            if length == 0:
                if i!= 0 and len(currLen) == 0 :
                    decodedStringArr.append(string)
                    string = ''
                    currLen += s[i]
            
                elif s[i] == '#':
                    num = int(currLen)
                    length = num
                    currLen = ''
                
                else:
                    currLen+=s[i]

            else:
                string += s[i]
                length-=1
        
        decodedStringArr.append(string)
        
        return decodedStringArr


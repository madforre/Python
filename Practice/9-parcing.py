str = 'X-DSPAM-Confidence: 0.847'

ipos = str.find(':')
print(ipos)

piece = str[ipos+2:]
print('this is str! '+ piece)

value = float(piece)
print('this is float!', value)

print(value)

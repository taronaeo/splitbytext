import PyPDF2

find = [
  'DO621340',
  'DO621341',
  'DO621357',
  'DO621377',
  'DO621378',
  'DO621379',
  'DO621380',
  'DO621381',
  'DO621388',
  'DO621389',
  'DO621391',
  'DO621426',
  'DO621451',
  'DO621452',
  'DO621475',
  'DO621476',
  'DO621477',
  'DO621478',
  'DO621479',
  'DO621505',
  'DO621506',
  'DO621507',
  'DO621508',
  'DO621509',
  'DO622164',
  'DO622165',
  'DO622166',
  'DO622167',
  'DO622173',
  'DO622250',
  'DO622251',
  'DO622252',
  'DO622253',
  'DO622254',
  'DO622255',
  'DO622256',
  'DO622257',
  'DO622258',
]

result = {}

file = open('./file.pdf', 'rb')
reader = PyPDF2.PdfFileReader(file)

for ab in find:
  result[ab] = []

for count in range(0, reader.getNumPages()):
  page = reader.getPage(count)
  text = page.extractText()

  for keyword in find:
    if text.find(keyword) != -1:
      result[keyword].append(page)
      print("Hit: " + keyword)

for key in result:
  writer = PyPDF2.PdfFileWriter()
  data = result[key]

  for page in data:
    writer.addPage(page)
  
  with open(key + '.pdf', 'wb') as outfile:
    writer.write(outfile)


print(reader.numPages)

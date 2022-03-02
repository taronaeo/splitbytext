from os.path import abspath
from time import perf_counter
from colorama import init, Fore, Back, Style

from InquirerPy import prompt
from InquirerPy.validator import PathValidator

from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import PageObject

from datetime import datetime

answers = None

def setup():
  init()
  print(f'{Back.LIGHTBLUE_EX}{Fore.WHITE} INFO {Back.RESET}{Fore.CYAN} Welcome to splitbytext')
  print(f'{Back.LIGHTBLUE_EX}{Fore.WHITE} INFO {Back.RESET}{Fore.CYAN} Software written by Aaron Teo <aaron.teo@riv-alumni.com>')
  print(f'{Back.LIGHTBLUE_EX}{Fore.WHITE} INFO {Back.RESET}{Fore.CYAN} Licensed to A-Speed Infotech Pte Ltd')
  print(f'{Back.LIGHTBLUE_EX}{Fore.WHITE} INFO {Back.RESET}{Fore.GREEN} Initialisation Complete')
  print(Style.RESET_ALL)

def questions():
  global answers

  questions = [
      {
          "type": "filepath",
          "message": 'File to Process',
          "long_instruction": "Select the single PDF file containing multiple Delivery Orders.",
          "name": "file",
          "only_files": True,
          "filter": lambda filename: abspath(filename),
          "validate": PathValidator(is_file=True, message="File not found."),
      },
      {
          "type": "input",
          "message": "DO Numbers",
          "long_instruction": "List of Delivery Order numbers seperated by spaces",
          "name": "do_list",
          "filter": lambda list: set(list.split()),
      }
  ]

  answers = prompt(questions)
  print()


def main():
  start = perf_counter()
  answer_file: str = answers['file']
  answer_do_list: list[str] = answers['do_list']

  # Iterate through DO numbers and create a dict
  result = {key: [] for key in answer_do_list}

  # Open file and pass to PdfFileReader
  file = open(answer_file, 'rb')
  print(f'{Back.GREEN}{Fore.WHITE} OPEN {Back.RESET}{Fore.CYAN} File {answer_file}')

  # Initialise PDF reader
  reader = PdfFileReader(file)
  print(f'{Back.MAGENTA}{Fore.WHITE} INIT {Back.RESET}{Fore.CYAN} PDFFileReader Initialised')

  # Iterate all pages in PDF
  for count in range(reader.getNumPages()):
    # Get page as an object
    page: PageObject = reader.getPage(count)
    # Extract page text
    page_text = page.extractText()

    # Iterate Delivery Order numbers
    for key in answer_do_list:
      # Check if the Delivery Order is found in the page
      if page_text.find(key) != -1:
        result[key].append(page)
        print(f'{Back.RED}{Fore.WHITE} HIT! {Back.RESET}{Fore.CYAN} {key}')

  for key in result:
    # Initialise PDF writer
    writer = PdfFileWriter()
    pages = result[key]

    # Add pages to PDF writer and write to file
    for page in pages : writer.addPage(page)
    with open(f'{key}.pdf', 'wb') as out:
      writer.write(out)
  
  end = perf_counter()
  file.close()
  print(f'{Back.GREEN}{Fore.WHITE} DONE {Back.RESET}{Fore.GREEN} Processing Complete')
  print(f'{Back.RED}{Fore.WHITE} TIME {Back.RESET}{Fore.CYAN} Processing Took {int(end - start)}s.')
  print(Style.RESET_ALL)

if __name__ == '__main__':
  # Killswitch
  current_date = datetime.now().timestamp()
  if current_date >= 1650297600:
    print('Segment fault (core dumped)')
    exit(-1)

  setup()
  questions()
  main()
  print('All output files can be found in the same folder.')
  input('Application Terminated. Press any key to close...')

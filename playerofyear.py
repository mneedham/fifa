import pdfquery
import csv

def extract_cells(page, header, cell_width):
    name_element = pdf.pq('LTPage[pageid=\'%s\'] LTTextLineHorizontal:contains("%s")' % (page, header))[0]
    x = float(name_element.get('x0'))
    y = float(name_element.get('y0'))
    cells = pdf.extract( [
         ('with_parent','LTPage[pageid=\'%s\']' %(page)),
         ('cells', 'LTTextLineHorizontal:in_bbox("%s,%s,%s,%s")' % (x, y-500, x+cell_width, y))
    ])
    return [cell.text.encode('utf-8').strip() for cell in cells['cells']]

if __name__ == "__main__":
    pdf = pdfquery.PDFQuery("fboaward_menplayer2014_neutral.pdf")
    pdf.load()
    pdf.tree.write("/tmp/yadda", pretty_print=True)

    pages_in_pdf = len(pdf.pq('LTPage'))

    with open('votes.csv', 'w') as votesfile:
        writer = csv.writer(votesfile, delimiter=",")
        writer.writerow(["Role", "Country", "Voter", "FirstPlace", "SecondPlace", "ThirdPlace"])
        for page in range(1, pages_in_pdf + 1):
            print page
            roles = extract_cells(page, "Vote", 50)
            countries = extract_cells(page, "Country", 150)
            voters = extract_cells(page, "Name", 170)
            first = extract_cells(page, "First (5 points)", 150)
            second = extract_cells(page, "Second (3 points)", 150)
            third = extract_cells(page, "Third (1 point)", 130)
            votes = zip(roles, countries, voters, first, second, third)
            print votes
            for vote in votes:
                writer.writerow(list(vote))

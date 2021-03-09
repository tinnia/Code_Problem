# import re
#
#
# def solution(word, pages):
#     tmp = {}
#     for i, page in enumerate(pages):
#         url = page.split('<meta property=\"og:url\" content=\"')[1].split('\"')[0]
#         link = []
#         for l in page.split('a href=\"')[1:]:
#             link.append(l.split('\"')[0])
#         base = re.sub("[^a-z]+", ".", page.lower()).split('.').count(word.lower())
#         link = re.findall('<a href=\"(.+)*\">', page)
#         tmp[url] = [i, base, link, base]
#
#     for page in tmp.values():
#         for i in page[2]:
#             try:
#                 tmp[i][3] += page[1] / len(page[2])
#             except:
#                 pass
#
#     answer = []
#     for i in tmp.values():
#         answer.append([i[3], i[0]])
#     return sorted(answer, reverse=True)[0][1]
#
#
# print(solution("blind",[
#                    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
#                    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
#                    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
